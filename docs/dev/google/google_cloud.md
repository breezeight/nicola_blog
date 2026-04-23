# Google Cloud

## Administration

For Billing, projects, organizations, sharing, etc, SEE [Google Cloud Administration HOWTO](google_cloud_admin_permission_howto.md)

### How to see all your Google Cloud projects

Go to console.cloud.google.com
→ Click the ☰ menu (top left) → IAM & Admin → Manage Resources.

In alternate ways you can use the direct link: `https://console.cloud.google.com/cloud-resource-manager`

or the command:

```
gcloud projects list
```
### Explanation: create and manage google gemini api key

#### Api key creation and relation to Google Cloud project

The easiest way to get a google gemini api key is to use the [Google AI Studio](https://ai.google.dev/studio): → Project (left menu) → Create New Project → keys → Create Key.


Google AI Studio (where you created your key) is a simplified, developer-friendly interface built on top of Google Cloud.

Behind the scenes, **every API key you generate belongs to one specific project in the Google Cloud ecosystem**.

#### Billing Account

Considerations:

- you can consolidate multiple projects (including multiple Gemini API keys) under a single billing account.
- you can get a detailed breakdown of costs by project, by service (Gemini API), by model/SKU, by time period, and more.
- A single Cloud Billing account can be linked to as many projects as you want (there is no hard limit). This is the standard and recommended way to manage costs across dev, staging, production, different apps, or different teams.

All projects linked to the same billing account share:
- The same payment method
- The same monthly spend caps (at the billing-account level)
- The same usage tier/rates for Gemini API


HOWTO **link a project to a billing account**: 
- Click the ☰ menu (top left) → Billing → click on "your projects tab".
- find your project in the list and click the tree dots action icon, select "change billing".

#### Budget Alerts
Left menu: Billing → "select account" → Budgets & alerts.

https://console.cloud.google.com/billing/01A643-D2A989-1163C2/budgets?authuser=1&organizationId=938075710818

#### Cost Breakdown

You can see a report of the costs by project, by service (Gemini API), by model/SKU, by time period, and more.

Example of a cumulative cost breakdown report:

https://console.cloud.google.com/billing/01A643-D2A989-1163C2/reports;timeRange=YEAR_TO_DATE;chartCostView=CUMULATIVE?organizationId=938075710818&authuser=1