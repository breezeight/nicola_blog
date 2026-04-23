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


### how to add a user to a project

**Here’s the exact process to add a user to a Google Cloud project** (as of April 2026).

This is done through **IAM (Identity and Access Management)** — the standard and secure way Google Cloud handles access.

**Step-by-step (easiest console method)**:

1. **Open the Google Cloud Console**  
   Go to: [https://console.cloud.google.com/](https://console.cloud.google.com/)

2. **Select the correct project**  
   At the top of the page, click the **project selector dropdown** and choose the project you want to add the user to.

3. **Go to the IAM page**  
   In the left sidebar, click **IAM & Admin** → **IAM**.  
   (Direct link once project is selected: [https://console.cloud.google.com/iam-admin/iam](https://console.cloud.google.com/iam-admin/iam))

4. **Click “Grant access”**  
   At the top of the IAM page, click the **Grant access** button (it has a person+ icon).

5. **Add the user**  
   - In the **New principals** field, enter the user’s **email address** (must be a Google Account or Google Workspace email).  
   - Click **Select a role** and choose the appropriate role(s).

6. **Choose the right role(s)**  
   Common roles for Gemini/API projects:
   - **Viewer** → Can see everything but not make changes (safest for basic access).
   - **Editor** → Can create/delete resources and manage most things (good for developers).
   - **Owner** → Full control (including billing and deleting the project — use sparingly).
   - **AI Platform User** or **Vertex AI User** → Specific for using Gemini models and APIs.
   - **Service Account User** (if they need to use service accounts).

   You can add **multiple roles** to the same user by clicking **Add another role**.

7. **Click Save**  
   The user will receive an email notification and can now access the project.

**Quick tips for your Gemini setup**:

- The user can now go to Google AI Studio, select this project, and create their own API key inside it (no need to share the actual key).
- If you want them to manage billing or quotas, also grant them a billing-related role at the **billing account** level (separate from the project).
- You can always revoke access later by going back to IAM → clicking the three-dot menu next to the user → **Remove**.

**Alternative (gcloud command — for power users)**:
```bash
gcloud projects add-iam-policy-binding PROJECT_ID \
  --member=user:USER_EMAIL@example.com \
  --role=roles/viewer
```
(Replace `PROJECT_ID` and the email/role as needed.)

Would you like me to tell you:
- The best roles for someone who just needs to use the Gemini API?
- How to add them to the billing account too?
- Or how to remove/revoke access later?

Just let me know the use case (e.g., “they should only run the API” or “they need full admin”) and I’ll give you the precise recommendation!


