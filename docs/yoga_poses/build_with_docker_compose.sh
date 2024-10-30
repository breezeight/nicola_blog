#!/usr/bin/env bash
set -e
set -o pipefail
#set -x
STARTTIME=$(date +%s)

usage() { echo "Usage: $0 [-f to force the images rebuild] [-e <chamber_env>] [-p <docker_registry_uri>] [-r to push to the registry]" 1>&2; exit 1; }

while getopts ":p:e:rfh" opts; do
    case "${opts}" in
        r)
            r="true"
            ;;
        p)
            p=${OPTARG}
            ;;
        e)
            e=${OPTARG}
            ;;
        f)
            f="-f"
            ;;
        h)
            usage
            ;;
    esac
done

#removes all the options that have been parsed by getopts from the parameters list
shift "$((OPTIND-1))"

# Populate SOURCEDIR env var with the absolute path of the current script
get_script_dir() {
     SOURCE="${BASH_SOURCE[0]}"
     # While $SOURCE is a symlink, resolve it
     while [ -h "$SOURCE" ]; do
          DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"
          SOURCE="$( readlink "$SOURCE" )"
          # If $SOURCE was a relative symlink (so no "/" as prefix, need to resolve it relative to the symlink base directory
          [[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE"
     done
     SOURCEDIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"
}
get_script_dir

source ${SOURCEDIR}/../docker.env.prod
source ${SOURCEDIR}/scripts/common.sh

$(aws ecr get-login --no-include-email);

export TMP_BUILDER_DIR=${SOURCEDIR}/tmp_builder
# We need TMP_BUILDER_RELATIVE_TO_DOCKER_CONTEXT_DIR
export TMP_BUILDER_RELATIVE_TO_DOCKER_CONTEXT_DIR=docker/tmp_builder

#SET ERLANG ELIXIR NODEJS versions
export $(${SOURCEDIR}/scripts/toolversion_to_env.sh -o dotenv -f ${SOURCEDIR}/../.tool-versions)

echo USER id: $(id)
echo TMP_BUILDER_VOLUMES PERMISSION: $(ls -la ${SOURCEDIR}/../tmp_builder_volumes|head -n 2|tail -n 1)
echo MOUNTED DIRECTORY PERMISSION: $(${SOURCEDIR}/compose.builder run -u root --rm api-builder bash -c "ls -la /app/_build|head -n 2|tail -n 1")
# BUILD Builder image
# export NODE_VERSION=`grep nodejs ${SOURCEDIR}/../.tool-versions|awk '{print $2}'` \
#   ERLANG_VERSION=`grep erlang ${SOURCEDIR}/../.tool-versions|awk '{print $2}'` \
#   ELIXIR_VERSION=`grep elixir ${SOURCEDIR}/../.tool-versions|awk '{print $2}'`

# BUILD or PULL base images
export build_or_pull_base_images_args="-p $p "

if [ -n "${r}" ]; then
  export build_or_pull_base_images_args="$build_or_pull_base_images_args -r"
fi

${SOURCEDIR}/build_or_pull_base_images.sh ${build_or_pull_base_images_args} ${f}


export RUNTIME_BASE_IMAGE=$(runtime_image $p)
echo RUNTIME_BASE_IMAGE=${RUNTIME_BASE_IMAGE}
export BUILDER_IMAGE=$(builder_image $p)
echo BUILDER_IMAGE=${BUILDER_IMAGE}

export CHECKSUMS_DIR=checksums

# Install dependencies2
if ${SOURCEDIR}/compose.builder run --rm api-builder bash -c "md5sum --status -c ${CHECKSUMS_DIR}/mix_checklist.chk";
then
  echo SKIP MIX DEPS: md5sum mix.exs mix.lock are not changed
else
  echo EXCUTING MIX DEPS
  ${SOURCEDIR}/compose.builder run -u root --rm api-builder bash -c "mix local.hex --force --if-missing && mix local.rebar --force && HEX_HTTP_CONCURRENCY=1 HEX_HTTP_TIMEOUT=120 mix deps.get"
  ${SOURCEDIR}/compose.builder run -u root --rm api-builder bash -c "md5sum mix.exs mix.lock > ${CHECKSUMS_DIR}/mix_checklist.chk";
fi
echo "Elapsed: $(($(date +%s) - $STARTTIME)) seconds"

## TODO Probabilment non ci ci serve
## && mix deps.compile
if [ -n "${NODE_VERSION}" ];
then
  if ${SOURCEDIR}/compose.builder run --rm api-builder bash -c "md5sum --status -c ${CHECKSUMS_DIR}/npm_checklist.chk";
  then
    echo SKIP YARN INSTALL: ${SOURCEDIR}/../assets/package* are not changed
  else
    echo EXCUTING YARN INSTALL
    ${SOURCEDIR}/compose.builder run -u root --rm api-builder bash -c "cd assets && yarn install --frozen-lockfile"
    ${SOURCEDIR}/compose.builder run -u root --rm api-builder bash -c "md5sum assets/package.json assets/yarn.lock > ${CHECKSUMS_DIR}/npm_checklist.chk";
  fi
  echo "Elapsed: $(($(date +%s) - $STARTTIME)) seconds"

  if ${SOURCEDIR}/compose.builder run --rm api-builder bash -c "md5sum --status -c ${CHECKSUMS_DIR}/assets_checklist.chk";
  then
    echo SKIP ASSETS BUILDING: ${SOURCEDIR}/../assets/{css,js,static} are not changed
  else
    echo EXCUTING ASSETS BUILDING
    ${SOURCEDIR}/compose.builder run -u root --rm api-builder bash -c "cd assets && ./node_modules/brunch/bin/brunch b -p && cd .. && mix phx.digest"
    ${SOURCEDIR}/compose.builder run -u root --rm api-builder bash -c "find assets/{css,js,static} -type f -exec md5sum {} \; > ${CHECKSUMS_DIR}/assets_checklist.chk";
  fi
  echo "Elapsed: $(($(date +%s) - $STARTTIME)) seconds"
fi

#READ ENV params from chamber
export COMPOSE_BUILD_ENV=""
for i in $(chamber export --format dotenv $e); do
  COMPOSE_BUILD_ENV=$COMPOSE_BUILD_ENV" -e $i"
done

${SOURCEDIR}/compose.builder run  -u root --rm $COMPOSE_BUILD_ENV api-builder bash -c "mix release --env=prod"
echo "Elapsed: $(($(date +%s) - $STARTTIME)) seconds"

## Copy the Content
# Create a container to bind the volume

#HACK on CircleCI we still have the old docker compose that donot' support --no-start
#docker-compose -f docker-compose/prod.yml up --no-start api-builder
${SOURCEDIR}/compose.builder create api-builder
echo "Elapsed: $(($(date +%s) - $STARTTIME)) seconds"

mkdir -p $TMP_BUILDER_DIR
#HACK we need to get RELEASE from somewhere else
docker cp $(${SOURCEDIR}/compose.builder ps -q api-builder):/app/_build/prod/rel/$APPLICATION_NAME/releases/$RELEASE/$RELEASE_TAR  $TMP_BUILDER_DIR
echo "Elapsed: $(($(date +%s) - $STARTTIME)) seconds"

### BUILD AND PUSH
echo "Creating RELEASE $p:$(git rev-parse HEAD)"

# CHOOSE docker tags
DOCKER_TAGS=()
GIT_TAG="$(git_tag)"
if [ -n "${GIT_TAG}" ]; then
  DEPLOY_TAG="$p:tag_${GIT_TAG}.$(git rev-parse HEAD)"
  DOCKER_TAGS+=( "$DEPLOY_TAG" )
  DOCKER_TAGS+=( "$p:production" )
fi

GIT_BRANCH=$(git_branch)
if [ -n "${GIT_BRANCH}" ]; then
  DOCKER_TAGS+=( "$p:${GIT_BRANCH//\//-}.$(git rev-parse HEAD)" )
fi

DOCKER_TAGS_ARG=""
for i in "${DOCKER_TAGS[@]}"
do
	DOCKER_TAGS_ARG="-t ${i} "$DOCKER_TAGS_ARG
done

docker build -f ${SOURCEDIR}/runtime.dockerfile . $(${SOURCEDIR}/scripts/toolversion_to_env.sh -f .tool-versions -o buildargs) --build-arg RUNTIME_BASE_IMAGE=$(runtime_image $p) --build-arg TMP_BUILDER_RELATIVE_TO_DOCKER_CONTEXT_DIR=$TMP_BUILDER_RELATIVE_TO_DOCKER_CONTEXT_DIR --build-arg RELEASE_TAR=$RELEASE_TAR ${DOCKER_TAGS_ARG} --build-arg APPLICATION_NAME=$APPLICATION_NAME
echo "Elapsed: $(($(date +%s) - $STARTTIME)) seconds"

echo "Built image ${DOCKER_TAGS}"

#Optionally Login to ECR and PUSH
if [ -n "${r}" ]; then
  echo "-r was triggered, PUSHING to the registry" >&2;
  for i in "${DOCKER_TAGS[@]}"
  do
    docker push $i;
  done
fi

#DEPLOY automatically only on tags
#if [ -n "${GIT_TAG}" ]; then
#  cd devops
#  DOCKER_IMAGE_TAG=$DEPLOY_TAG stack_master apply --yes eu-west-1 bt-ecs-task-def
#  stack_master apply --yes eu-west-1 bt-ecs-service
#fi
