---
title: Aws New Customer Account Bootstrap SOP
---
# HOWTO Bootstrap a AWS Organization Management Account

## Basic info you need in advance

Estimated time: 4h to collect info and follow the procedure.

To create the root 

What you need at least:

* Customer e-mail and an email dedicated to the AWS root account (DLs recommended)
* OTP device (1password is recommended)
* Customer invoicing data (SDI)
* Customer Credit Card data (or do the setup with the customer). You need this data at the very beginning of the registration.
* Customer phone number
* Access to the activation code that will arrive to the customer phone and email. Access to the credit card OTP.

> NOTE: Each AWS account must have a unique email address associated with it.

Regardless as to whether you create a new management AWS account or reuse an existing management AWS account, you’ll need to prepare a set of email addresses to represent the root user of each of the new AWS accounts that will be created. In later steps, when you create AWS accounts, you’ll be referring to these email addresses.

**Use either email distribution lists (DLs) or shared mailboxes.** Instead of using a person’s email address, it’s recommended that you use either email distribution lists (DLs) or shared mailboxes so that you can enable at least several trusted people, for example, your Cloud Administrators, access to email messages associated with each AWS account.

> **Carefully control access to the email accounts** Since the email address associated with an AWS account is used as the root user login for the account, anyone with access to that email account will have access to password reset process for the account.

Internally we choose to use google groups emails (the Google version of `email distribution lists (DLs)` and we could suggest a similar strategy to our customer. This is the **naming convention**:

```
aws-<CLIENT-CODE>+<ACCOUNT-NAME>@company.com
```

For example:

| AWS Account Name | Purpose | Email Address Example |
|------------------|---------|-----------------------|
| management | You’ll either create a new management AWS account or reuse an existing compatible AWS account. | aws-management@example.com |
| Audit | Created by AWS Control Tower. | aws-audit@example.com |
| Log archive | Created by AWS Control Tower. | aws-log-archive@example.com |

> **Use alternate Email for Billing, Security**

To keep other people in the notification loop without giving them root access to the account we use alternate email, As described here [AWS Doc: alternate email Accounts](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-contact-alternate.html#manage-acct-update-contact-alternate-orgs)

Our policy is to create an email distribution list for each organization:

```
aws-notification@company.com
```

> On Google To read the history of a group go to: https://groups.google.com/my-groups?pli=1

## Procedure - Portal, Users, Permission Sets

Glossary:

* `CLIENT-DOMAIN` dominio del cliente ex: techstationpadova.it
* `CLIENT-CODE` codice usato per il cliente per abbreviare ex: TS

Step 0: Choose the Ireland Region

> see Ireland is the cheapest and the most modern AWS in EU, [see concurrencylabs blog](https://www.concurrencylabs.com/blog/choose-your-aws-region-wisely/)

Step 1: secure the root user and set payment info

- [ ] Create a root account with `Root user email address = aws-management@<CLIENT-DOMAIN>` and `AWS account name = <CLIENT_CODE>-management` Choose a name for your account. You can change this name in your account settings after you sign up.

> If you are migrating an existing organization you can edit both to follow this naming convention (`Menu on the top right -> Account -> Acccount Settings`). WARNING: Don't create any resource into the root org

- [ ] Setup OTP for the root account and store credential using a company password manager (ie. 1Password)
- [ ] Setup tax information. For Italy SDI, VAT number, and business details https://aws.amazon.com/tax-help/european-union/

Step 2: create IAM users for the root account

- [ ] Idendify which users will need the `AdministratorAccess` AWS managed policy in the root account. TODO: how do we choose how will have this VERY critical permission???
- [ ] Idendify which users will need the `Billing` AWS managed policy in the root account.
- [ ] Enable [IAM Identity Center](https://us-east-1.console.aws.amazon.com/singlesignon/identity/home). This procedure will create the an AWS Organization (with the same name of the AWS account) and will register the current `<CLIENT_CODE>-management` AWS Account as the root of your organization, it will become the `management account`: each month AWS charges your management account for all the accounts of the organization (consolidated bill).
- [ ] OPTIONALLY customize the `AWS access portal URL` to something short and easier to remember with the pattern `<CLIENT_CODE>-management`. OR Keep the default setting if there aren't special requirement form the customer.
- [ ] Copy the `AWS access portal URL` from the `Settings summary` tab, you will needed it later to let your user sing-in into AWS accounts.

> WARNING: the AWS UI will ask you to do `Step 1: Choose your identity source` but the default AWS Identity source is already choosen, skip this step if you don't have special requirement (ex: connect to an external IdP).

- [ ] **AdministratorAccess** Create a `Permission Set` for user associated with the `AdministratorAccess` AWS managed policy, follow [the step 2 of the AWS guide](https://docs.aws.amazon.com/singlesignon/latest/userguide/get-started-create-an-administrative-permission-set.html).

> By convention the `Permission Set` name will be the same of the managed policy associated. The name that you specify for this permission set appears in the AWS access portal as an available role. After users in IAM Identity Center sign in to the AWS access portal and select an AWS account, they can choose the role. This convention makes easier to remember which permission has the role you are selecting.

TODO : How should we enforce MFA for all users?

- [ ] !!! Sign out from the AWS Console session where you used the initial root credentials. From now you will use only the IAM user you've just created above.
- [ ] To create users with `Billing` permission set in the management account `<CLIENT_CODE>-management` [repeat this step of the AWS guide](https://docs.aws.amazon.com/singlesignon/latest/userguide/get-started-create-an-administrative-permission-set.html) but select `Billing` AWS managed policy and name the permission set `Billing`.
- [ ] \[OPTIONAL\] Add other permission set. This is a list of the most common [Predefined permissions](https://docs.aws.amazon.com/singlesignon/latest/userguide/permissionsetpredefined.html)
- [ ] [Add users](https://eu-central-1.console.aws.amazon.com/singlesignon/identity/home?region=eu-central-1#!/users). Users will receive an invitation email `Invitation to join AWS Single Sign-On`
- [ ] Set alternate email for each aws account to `aws-notification@<CLIENT-DOMAIN>` (billing and security). Sign in to the AWS Organizations console with the organization's management account credentials. From AWS accounts, select the account that you want to update. Choose Contact info, and under Alternate contacts, locate the type of contact: Billing contact, Security contact, or Operations contact. Important: For professional AWS accounts, it's a best practice to enter a company phone number and email address rather than one belonging to an individual.

## Procedure - Create AWS Accout Hierarchy

Step XXX Consolidated billing

https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/useconsolidatedbilling-procedure.html

Open the `AWS Organization` page

Step 3: set budget alarms

- [ ] Define montly budget
- [ ] Define who will get notifications

Step 4: Setup OU

- [ ] Define at leat one production OU with one production account
- [ ] Activate `Consolidated billing`
- [ ] Repeat `step 1` for each account (or use `IAM Identify Center` with SSO)

> WARNING as oct 2022 we still don't have a full knowledge of `IAM Identify Center` so the advice is to create IAM users

Step : Budget alarms and monitoring

- [ ] To Enable cost explorer: just visit the `AWS Cost Explorer` page (it needs 24h to be ready)
- [ ] From here clik on `Aws Cost Anomaly Detection` (if need to wait the activation of the `AWS Cost Explorer`) and enable the service.
- [ ] Set Aws Budget: use the `Zero spend budget` template if you want to use only the free tier. Or set a monthly threshold

## \[OPTIONAL\] Use GSuite as IdP

TODO:

* https://blogs.halodoc.io/aws-sso-using-g-suite/
* https://docs.aws.amazon.com/singlesignon/latest/userguide/get-started-connect-id-source-ad-idp.html
* https://aws.amazon.com/blogs/security/how-to-set-up-federated-single-sign-on-to-aws-using-google-workspace/

Pro:

* less credential to manage

## \[OPTIONAL\] Enable single sign-on access to Amazon EC2 Linux instances

TODO

## FAQ

\### User sees only "You do not have any applications." This user doens't have any permission.

## \[WIP\] Enable IAM Identity Center

TODO:

* How to force MFA

# Required knowledge to perform this SOP

Although in-depth knowledge of the following topics is not absolutely required to make use of this SOP, it’s recommended that your initial Cloud Foundation team members achieve at least an introductory level of knowledge of these topics prior to using this guide:

* Core AWS Concepts
* AWS Identity and Access Management (IAM)
* AWS Single Sign-on (AWS SSO)
* AWS Cost Management
* AWS SNS
* [AWS IAM Identity Center DOC](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html), [Addicitve Guide](https://gitlab.com/addictivedev/ad-internals/examples-and-wiki/-/wikis/Aws/aws-iam-identity-center)
* [AWS Organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html), [Addicitve Guide](https://gitlab.com/addictivedev/ad-internals/examples-and-wiki/-/wikis/Aws/Aws-Organizations)

This is an useful workshop by AWS https://getstarted.awsworkshop.io/00-intro.html