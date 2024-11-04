# How to Use 1Password to Securely Store Your AWS credentials

## Nicola's Day by Day Usage

### Use the credentials for a new customer

After you follows the instructions below to setup the credentials for a new customer, you can just:

```
cd ~/SRC/CUSTOMER_DIR
# run any aws command, e.g.
aws sts get-caller-identity
```

### Setup AWS Credentials for a new customer

1. create the aws credentials on the web and store them in 1Password: see the first part of the [1password aws cli plugin docs](https://developer.1password.com/docs/cli/shell-plugins/aws) and additionally:
    * save the credentials in the Employee Vault
    * add a tag that the company already has in 1Password: `idr-channelguard/aws-credentials`, this allows you to find them quickly later.
2. cd intro the project directory: `cd ~/SRC/CUSTOMER_DIR`
3. `op signin` > `op plugin init aws` > find the key > `Use automatically when in this directory or subdirectories`
4. The last step is to set up an alias for aws. You can do so by running the following command:

```
echo "source /Users/nicolabrisotto/.config/op/plugins.sh" >> ~/.zshrc && source ~/.zshrc
```

## Explanation

Why Use 1Password for AWS Credentials?

The standard practice of storing AWS credentials in `~/.aws/credentials` presents a security risk:

- Credentials are stored in plain text
- Multiple IAM user profiles are kept locally
- Even with disk encryption, credentials remain vulnerable

This howto demonstrates how to use 1Password as a more secure alternative for managing AWS access keys across multiple IAM accounts.


### 1Password CLI Shell Plugin for AWS

1Password provides CLI plugins that integrate with various development tools. The AWS CLI plugin allows secure credential management directly from 1Password:

https://developer.1password.com/docs/cli/shell-plugins/aws

### does the aws 1password plugin integrate also with the AWS VScode extension?
- [ ] TODO: check if this is true https://www.perplexity.ai/search/what-are-1password-plugins-SghHvYnoSPS1sGorcr.XVw

### How does the plugin know which vault and item to use?

As you can see in the file `op` created an local config file that maps to a specific vault and item in 1Password: `~/SRC/CUSTOMER_DIR/.op/plugins/aws.json`:

```json
{
	"account_id": "PQE4CI62WZC7DBNEXR66UWHO3U",
	"entrypoint": [
		"aws"
	],
	"credentials": [
		{
			"plugin": "aws",
			"credential_type": "access_key",
			"usage_id": "access_key",
			"vault_id": "abyevombrivlqkczbbmgf3hene",
			"item_id": "w66npczfzitjfrxautx4zv7c6a"
		}
	]
}
```