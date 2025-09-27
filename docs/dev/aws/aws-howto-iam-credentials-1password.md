# How to Use 1Password to Securely Store Your AWS credentials

This guide covers two approaches to managing AWS credentials securely using 1Password: traditional AWS IAM (Identity and Access Management) credentials and the newer AWS IAM Identity Center (formerly AWS Single Sign-On). Each method has its own use cases, advantages, and considerations, which are explained below to help you choose the best option for your environment.

This document is divided in three sections:

1. [HOWTO - IAM Identity Center](#howto-iam-identity-center): the reccomended approach for new customers.
2. [HOWTO - traditional IAM users](#howto-traditional-iam-users)
3. [Explanation: how to choose the best option for your environment](#explanation-how-to-choose-the-best-option-for-your-environment): explain the advantages and disadvantages of each approach and some choices made.

> [!NOTE] 
> This documement cover only how to setup the credentials on the client side, not the server side. For the server side, see:
> * the [AWS IAM Identity Center Nicola's Docs](aws-iam-identity-center.md).
> * the [AWS IAM User Offcial Docs](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html).

## Example of ~/.aws/config file

This is an example of a `~/.aws/config` file that uses both approaches described in this document. Use it as a reference to configure your own `~/.aws/config` file. How to use it is explained in the next sections.

```toml
# Idrostudi AWS Accounts: idr
[profile idr-AdministratorAccess]
region = eu-central-1
credential_process = ${aws1pHelperFullPath} "aws-idr-iam-access-key-nicola.brisotto"

# Addictive aws-ad-lab account
[profile aws-ad-lab-AdministratorAccess]
sso_start_url = https://addictive.awsapps.com/start
sso_region = eu-west-1
sso_account_id = 034362055352
sso_role_name = AdministratorAccess
region = eu-west-1
output = json

# Addictive aws-ad-prod account
[profile aws-ad-prod-AdministratorAccess]
sso_start_url = https://addictive.awsapps.com/start
sso_region = eu-west-1
sso_account_id = 124355679718
sso_role_name = AdministratorAccess
region = eu-west-1
output = json
```

## HOWTO - IAM Identity Center

> [!WARNING] 
> IAM Identity Center is recommended to be used instead of IAM users.

TODO.....

```toml
# Addictive aws-ad-prod account
[profile aws-ad-prod-AdministratorAccess]
sso_start_url = https://addictive.awsapps.com/start
sso_region = eu-west-1
sso_account_id = 124355679718
sso_role_name = AdministratorAccess
region = eu-west-1
output = json
```

## HOWTO - traditional IAM users 

> [WARNING] IAM users should be avoided if possible, use IAM Identity Center instead.

### Initial setup

> [NOTE] this setup is required only once, not per customer.

#### Create Helper Scripts for Using AWS Credentials from 1Password

Create a script like `~/bin/aws-1p-credentials.sh`:

```bash
#!/usr/bin/env bash
ITEM_NAME="$1"

ACCESS_KEY=$(op item get "$ITEM_NAME" --fields label='access key id')
SECRET_KEY=$(op item get "$ITEM_NAME" --reveal --fields label='secret access key')

cat <<EOF
{
  "Version": 1,
  "AccessKeyId": "$ACCESS_KEY",
  "SecretAccessKey": "$SECRET_KEY",
  "SessionToken": null,
  "Expiration": null
}
EOF
```

This script explicitly extracts the AWS credentials from a 1Password item and exports them as environment variables.

Make it executable:

```bash
chmod +x ~/bin/aws-1p-credentials.sh
```

### How-to setup and use the credentials for a new customer

> [NOTE] this setup is required for each new customer.

#### Setup AWS Credentials and store them in 1Password

2. Create the AWS credentials on the web and store them in 1Password by following the "Requirements step 1 and 2" of the [1password aws cli plugin docs](https://developer.1password.com/docs/cli/shell-plugins/aws) and additionally:
    * Always save the credentials in the Employee Vault (this is make it private to you and not shared with the other users of the company)
    * For convenience, Add a tag to the item using the same tag that the company already has in 1Password for the project: `idr-channelguard/aws-credentials`, this allows you to find them quickly later.
	* give the item a name (`ITEM_NAME`) that you will use in the next step in the `~/.aws/config` file, ex: `aws-idr-iam-access-key-nicola.brisotto`. Avoid special characters and spaces.

> [WARNING] DO NOT USE ALIAS as the 1password official guide suggest, see the [Why we avoid alias as the 1password official guide suggest](#why-we-avoid-alias-as-the-1password-official-guide-suggest) section for more details.

#### Create a new profile for the customer

In your `~/.aws/config` add a new profile `YOUR_NEW_PROFILE` for the customer and use and set the `ITEM_NAME` you chose in the previous step:

```toml
[profile YOUR_NEW_PROFILE]
region = us-east-1
credential_process = sh -c "$HOME/test.sh ITEM_NAME"
```

#### Use the credentials for a new customer

After you follow the instructions below to set up the credentials for a new customer, you can just any aws command with the profile you chose in the previous step. For example to test the credentials:

```bash
# show the last part of the credentials so you can check if they are correct
aws --profile=YOUR_NEW_PROFILE configure list
```

Or use the environment variable `AWS_PROFILE` to set the profile:

```bash
export AWS_PROFILE=YOUR_NEW_PROFILE 
aws configure list
```

#### Optionally, direnv

1. Create new directory for the customer, ex: `mkdir -p ~/SRC/CUSTOMER_DIR` 
2 `cd ~/SRC/CUSTOMER_DIR`
3. create a `.envrc` file with the following content:

```bash
export AWS_PROFILE=YOUR_NEW_PROFILE
```
4. run `direnv allow`

Now you can just run any aws command in the directory and the credentials will be automatically set. To test it, run:

```bash
aws configure list
```


## Explanation: how to choose the best option for your environment
### AWS IAM Identity Center vs AWS IAM

AWS IAM Identity Center provides centralized access management for AWS accounts and business applications. It allows users to sign in with their existing corporate credentials and provides single sign-on (SSO) capabilities, making it easier to manage permissions across multiple accounts without sharing long-lived credentials.

**Pros of AWS IAM Identity Center:**
- Centralized user and permission management
- No need to distribute long-lived access keys
- Supports SSO and temporary credentials with automatic rotation
- Simplifies access for large organizations with many accounts

**Cons:**
- Requires AWS Organizations setup
- May have a learning curve for initial configuration
- Some third-party tools may not fully support it yet

**When to use:** Ideal for organizations with multiple AWS accounts and users who prefer centralized, federated access management.

---

AWS IAM is the traditional method where users create IAM users and generate long-lived access keys. These keys are stored locally (often in `~/.aws/credentials`) and used by tools like the AWS CLI.

**Pros of AWS IAM:**
- Simple to set up for individual users or small teams
- Supported by all AWS tools and SDKs
- Allows fine-grained permission control per user or service

**Cons:**
- Managing multiple keys can be cumbersome and insecure
- Keys must be rotated manually to maintain security
- Storing keys in plain text files poses security risks

**When to use:** Suitable for individual developers, small teams, or automated systems requiring programmatic access.
 
### Why Use 1Password for AWS Credentials?

The standard practice of storing AWS credentials in `~/.aws/credentials` presents a security risk:

- Credentials are stored in plain text
- Multiple IAM user profiles are kept locally
- Even with disk encryption, credentials remain vulnerable

This howto demonstrates how to use 1Password as a more secure alternative for managing AWS access keys across multiple IAM accounts.

### Why we avoid alias as the 1password official guide suggest

The 1Password documentation describes an "alias official mode" where you create a shell alias for the `aws` command that automatically injects credentials from 1Password. While this approach is straightforward, it has some limitations:

- Aliases do not propagate to all shells or scripts, which can cause inconsistent behavior.
- Some tools or IDE integrations may not respect shell aliases.
- Managing aliases can become complex when switching between multiple projects or profiles.

1Password provides CLI plugins that integrate with various development tools. The AWS CLI plugin allows secure credential management directly from 1Password:

https://developer.1password.com/docs/cli/shell-plugins/aws

### How AWS Tools Use Profiles

AWS CLI and SDKs use named profiles to manage multiple sets of credentials. Profiles are typically stored in two files within the user's home directory:

- `~/.aws/credentials`: Contains access keys and secret keys for different profiles.
- `~/.aws/config`: Contains configuration settings like default region and output format per profile.

Profiles allow users to switch between different AWS accounts or roles easily by specifying the profile name in commands or environment variables.
