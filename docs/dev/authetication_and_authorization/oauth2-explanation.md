---
title: "OAuth 2.0 - Developer Guide"
description: "A practical developer guide to OAuth 2.0 with real-world examples from Google, GitHub, and Azure"
abstract: "Understand OAuth 2.0 from zero using modern practices, with concrete examples from major providers"
type: explanation
date: 2026-04-21 00:00:00 +0200
comments: true
categories: ["Authentication", "Authorization"]
---

# OAuth 2.0

*A Practical Beginner's Guide (2026)*

This guide is written for developers, product teams, and anyone who wants to **understand OAuth 2.0 from zero** using modern, secure practices. It proposes a practical mental model + a few concrete rules of thumb you can use while reading any OAuth RFC or vendor docs.
From here are linked some valuable resources that you can use to learn more about OAuth 2.0 (ex: OIDC, some legacy flows, some vendor-specific documentation and examples).

### What you will learn
- Why OAuth 2.0 exists and how it protects user passwords
- The essential concepts (roles, scopes, tokens, grants, and flows)
- In 2026, **Authorization Code + PKCE** is the default and recommended OAuth flow for almost all user-facing apps — but other scenarios (machine-to-machine communication, input-limited devices) call for different grant types, and this guide covers those too
- How consent screen and token exchange actually work the real-world with concrete examples that you can easily test (some tutorials are linked here)

### What this guide is *not*
It is **not** a rewrite of the RFCs (but technical specification language is used) nor an implementation manual.
We focus only on the core ideas and the most common real-world patterns.
More advanced or niche topics (such as token introspection, DPoP, or legacy flows) are mentioned briefly and/or linked for further reading.

By the end of this guide you'll have a clear mental model of OAuth 2.x and feel confident reading, discussing, and working with it in modern applications.

## What is OAuth 2.x?

**OAuth 2.0** and its extensions (ex: OAuth 2.1 draft, ... ) are a secure **authorization framework** that lets third-party applications access a user's data on another service **without ever needing the user's credentials** (typically username and password). 

Imagine you want to let a time-management app automatically add focus-time blocks to your Google Calendar —  **but without ever giving it your Google password.**

**OAuth 2.x** is the secure, modern way to make that possible.

Instead of sharing your username and password (the old, risky way), OAuth lets you safely grant an app **limited and temporary access** to your data. You decide exactly what the app can do, how long it can do it, and you can revoke that permission at any time.

### How the Google Calendar example works (user perspective)
The following steps are the user perspective of the flow in one of the most common user experience:

1. You’re on a third‑party website (not Google), and you see a button like “Connect Google Calendar”. You click it to let that app access your calendar.
2. The browser **redirects** to the service that store the resources (The Google Calendar, in the example) using a **special authorization URL**.
   This URL contains all the details the Google Calendar service needs to identify the app. We will explain them in detail later in this document the meaning of each parameter. These are the more common ones:
   - `client_id` → identifies the app
   - `redirect_uri` → where to send you back after approval
   - `scope` → exactly which resources/permissions the app wants (e.g. `calendar.events.read calendar.events.create`)
  
3. If you are not already logged in, you log into the service (Google in this example), then see a **consent form/screen** that clearly lists the exact permissions the app is requesting.  
   **Typical consent form looks like this:**
   - App name + logo  
   - “This app would like to:”  
     • View your calendar events  
     • Create and edit events in your calendar  
     • See your email address  
   - “Do you want to allow this app to do these things?”  
   - **[Allow]** **[Cancel]** buttons  
   After you click **Allow**, Google redirects your browser back to the app with all the information that the app needs to gain access to your Calendar.
4. The app’s backend swaps the above information for an **access_token**, then uses the token to call the **Resource Server** (the API interface for the Google Calendar).

Behind the scenes what happens is called the **Authorization Code Flow**, which is more complex. We will explain it in detail later in this document. Here is a high-level overview of the flow:
```mermaid
sequenceDiagram
    participant User as User (Browser)
    participant App as Third-party App (Server)
    participant Auth as Google (Authorization Server)
    participant API as Google Calendar API (Resource Server)

    Note over App,API: OAuth 2.0 Authorization Code Flow ("Connect with Google")

    User->>App: 1. Clicks "Connect Google Calendar"
    App-->>User: 2. Redirect to Google /authorize<br/>client_id + redirect_uri + scope + response_type=code + state
    User->>Auth: 3. Opens Google /authorize
    Auth-->>User: 4. Login (if needed) + consent screen
    User->>Auth: 5. Approves
    Auth-->>User: 6. Redirect back to redirect_uri<br/>with one-time code + state
    User->>App: 7. Browser follows redirect with code + state

    Note over App,Auth: Code is exchanged server-to-server
    App->>Auth: 8. POST /token with code<br/>(+ client_secret or PKCE code_verifier)
    Auth-->>App: 9. Returns Access Token (+ optional Refresh Token)

    App->>API: 10. Calls Calendar API with Authorization: Bearer ACCESS_TOKEN
    API-->>App: 11. Returns calendar data
    App-->>User: 12. Updates the UI
```

## Key Benefits of OAuth 2.0

- **No password sharing**: The app gets permission without ever seeing your password.
- **Limited access**: Users can limit what the app can do (scopes) and revoke access later.
- **Standard approach**: It’s widely used across major services.

## WARNING Recent Changes in OAuth 2.1 (Draft)

> [!WARNING] 
> There are some changes in OAuth 2.1 (Draft) that are not yet implemented by all major OAuth 2.0 providers.

This section is placed here to warn you about the changes in OAuth 2.1 (Draft) that are not yet implemented by all major OAuth 2.0 providers. If it's the first time you are reading this guide focus on the main concepts and come back here later to read the details.

The bottom line: it doesn't introduce new functionality — **it removes risky patterns** and makes previously optional best practices mandatory (ref [WorkOS](https://workos.com/blog/oauth-2-1-vs-oauth-2-0)).

- **PKCE is required** for Authorization Code flow (not optional anymore).
- **Implicit flow is removed** (no more `response_type=token`).
- **Password flow (ROPC) is removed** (apps should not collect user passwords).
- **Redirect URIs must match exactly** (no wildcards).
- **Access tokens must not be put in URLs** (for example, not in query strings).
- **Refresh tokens must be safer** (rotation or sender-constrained tokens).

Notable: Anthropic adopted OAuth 2.1 as the foundation for MCP’s authorization spec ([WorkOS](https://workos.com/blog/oauth-2-1-vs-oauth-2-0)).

Sources:

* https://oauth.net/2.1/
* https://datatracker.ietf.org/doc/draft-ietf-oauth-v2-1/ (draft-15)
* https://stytch.com/blog/oauth-2-1-vs-2-0/

## Main Concepts

Now let’s quickly understand more formally the **key building blocks** of OAuth 2.0. Think of these as the basic “ingredients” you’ll see in every OAuth interaction.

### The Four Roles

OAuth always involves four different **actors**:

- **Resource Owner**: An entity capable of granting access to a protected resource, typically the end-user.
- **Client**: An application making protected resource requests on behalf of the resource owner and with its authorization.  
- **Resource Server**: The server hosting the protected resources, capable of accepting and responding to protected resource requests using access tokens.
- **Authorization Server**: The server issuing access tokens to the client after successfully authenticating the resource owner and obtaining authorization.

### Authorization Grant – The user’s “yes”

In simple terms: the grant refers to the abstract concept of the user having granted authorization to the app.

Ex: In the The authorization code flow, when the user clicks **Allow** on the consent screen, they are giving the app an **authorization grant** that will be exchanged for an access token.

[Source: Aaron Parecki](https://aaronparecki.com/2024/03/29/3/oauth-terminology)

### Scopes – “What exactly are you allowed to do?”

Usually, users don’t give the app **full** access to their account.  
Instead, users choose **specific permissions** called **scopes**.

Examples:
- `calendar.read` → only read the user's events
- `calendar.events.create` → can create new events in the user's calendar
- `email.read` → can read the user's email address

Users see these listed clearly on the consent screen. They can always revoke or change them later.

### Access Token – The “temporary key”

After the user clicks **Allow**, the app receives a special key called an **access token**.  
This token acts like a temporary digital key that lets the app talk to the API **on your behalf**.

- It is **short-lived** (usually 1 hour or less)
- It only works for the scopes you approved
- The app must send this token with every API request

### Refresh Token – The “long-term spare key”

When the access token expires, the app can use a **refresh token** to get a brand-new access token **without asking the user to log in again**.

- Stored securely on the app’s server
- Much longer-lived (days, weeks, or months)
- Can be revoked by the user at any time

### Client ID and Client Secret

Every app must register with the service (ex: Google, GitHub, etc.) first.  
After registration, the service gives the app two pieces of information:
- **Client ID** → like a public username for the app (safe to show in browser)
- **Client Secret** → like a password for the app (must stay secret on the server)
These are used to prove the app is legitimate.

### Flows, Grants Types and Grants – The different ways OAuth happens

A **flow** is the complete end-to-end process that shows how all the pieces above work together. In the specifications you will find several flows. 

Each flow is formally defined as a **grant type** — the specification's name for the mechanism (e.g., "Authorization Code grant type", "Client Credentials grant type"). Within a flow, the specific POST request to the token endpoint is called a **grant** (e.g., "the authorization code grant includes the PKCE code verifier").

In short: the **grant type** is what the spec defines, the **flow** is what you implement, and the **grant** is the actual token exchange that happens inside it.

> **Note:** In practice, "flow" and "grant type" are often used interchangeably — saying "Authorization Code flow" or "Authorization Code grant type" will be understood the same way. The distinction matters mostly when writing precise documentation or spec-level text.


## A more formal definition of what OAuth is from the RFC

OAuth introduces an authorization layer by **separating the role of the client from that of the resource owner**. In OAuth, the client requests access to resources controlled by the resource owner and hosted by the resource server, and is issued a **different set of credentials** than those of the resource owner.

Instead of using the resource owner's credentials to access protected resources, the client obtains an **access token** -- a string denoting a specific scope, lifetime, and other access attributes. Access tokens are issued to third-party clients by an **authorization server** with the approval of the resource owner. The client uses the access token to access the protected resources hosted by the resource server.

[RFC 6749](https://datatracker.ietf.org/doc/html/rfc6749)

## Overview of an OAuth 2.0 Flow (Grant Type)

A **flow** is an end-to-end process  **between actors (client, authorization server, resource owner, resource server)**, consisting of ordered protocol steps, each bound to specific endpoints, parameters, and security guarantees.

Common **Endpoints**, are:

* `/authorize` → front-channel (browser redirect)
* `/token` → back-channel (server-to-server)
* `/introspect`, `/revocation` (optional)
* `/userinfo` → identity retrieval (in the case of OIDC extensions)

Common **requests/responses** contain:
  * required parameters (`client_id`, `redirect_uri`, `scope`, etc.)
  * response artifacts (`code`, `access_token`, `id_token`)

**State & correlation** are maintained via:
  * `state` (CSRF protection)
  * `nonce` (OIDC replay protection)
  * `code_verifier` / `code_challenge` (PKCE)


**Channel separation** is very important, a modern flow explicitly separates:
  * **Front-channel** (via browser) like:
    * redirects
    * user interaction
    * less trusted
  * **Back-channel** (direct server to server):
    * token exchange
    * trusted server communication
  * NOTE: This distinction is core to why some flow is more secure than others.


To make it concrete, a simplified overview of the “Authorization Code Flow + PKCE” flow is this sequence:

1. Browser → `/authorize` (front-channel)
2. User logs in (interaction)
3. Redirect → client with `code` (front-channel)
4. Client → `/token` (back-channel) and receive the access-token

When you design or review a system, treat a flow as:

* a **state machine**
* executed over HTTP
* involving both:

  * user agent (browser)
  * backend channels
* with explicit **security invariants**





## Application Registration

Before using OAuth with your application, you must register your application with the service. This is done through a registration form in the **developer** or **API** portion of the service's website, where you will provide the informations needed to identify your application. For example in the case of the Authorization Code flow, you will need to provide:

-   Application Name
-   Application Website
-   Redirect URI or Callback URL

The redirect URI is where the service will redirect the user after they authorize (or deny) your application, and therefore the part of your application that will handle authorization codes or access tokens.

### Where to Register Your App (Real-World Providers)

| Provider | Developer Console | What You Get |
|----------|------------------|--------------|
| **Google** | [Google Cloud Console > APIs & Services > Credentials](https://console.cloud.google.com/apis/credentials) | OAuth 2.0 Client ID + Client Secret |
| **GitHub** | [Settings > Developer settings > OAuth Apps](https://github.com/settings/developers) | Client ID + Client Secret |
| **Azure / Microsoft** | [Azure Portal > App registrations](https://portal.azure.com/#blade/Microsoft_AAD_RegisteredApps/ApplicationsListBlade) | Application (client) ID + Client Secret (or certificate) |

Each provider uses slightly different terminology, but the concept is the same: you register your app, get credentials, and configure redirect URIs.

### Client ID and Client Secret

Once your application is registered, the service will issue *client credentials* in the form of a **client identifier** and a (optional) **client secret**. 

The Client ID is a publicly exposed string that is used by the service API to identify the application, and is also used to build authorization URLs that are presented to users.

The Client Secret is used to authenticate the identity of the application  to the Authorization Server (e.g., during a token request), and must be kept private between the application and the Authorization Server. It applies only to confidential clients — applications that can securely store the secret, such as server-side backends.

For example, when a server-side app exchanges an authorization code for a token with Google or GitHub, it includes the Client Secret in the POST request to prove its identity. A mobile app or a browser-based application cannot safely store a secret, so not all applications will have one.

## Authorization Grant Types

The **authorization grant type** determines how an application obtains an access token.

The recommended grant type depends on the application type:

- **Web App (server-side):** Authorization Code + PKCE — the server can securely store a `client_secret`, but PKCE is still required. Defined in [OAuth 2.1 §4.1](https://datatracker.ietf.org/doc/draft-ietf-oauth-v2-1/).
- **SPA (browser-based):** Authorization Code + PKCE — as a public client, the SPA cannot store a `client_secret` and relies entirely on PKCE. Defined in [OAuth 2.1 §4.1](https://datatracker.ietf.org/doc/draft-ietf-oauth-v2-1/).
- **Mobile / Native App:** Authorization Code + PKCE — same as SPA, plus the app must use the system browser, not an embedded webview ([RFC 8252](https://datatracker.ietf.org/doc/html/rfc8252)).
- **CLI:** Device Code ([RFC 8628](https://datatracker.ietf.org/doc/html/rfc8628)) if the CLI cannot open a browser; otherwise Authorization Code + PKCE with a localhost redirect.
- **Smart TV / IoT:** Device Code ([RFC 8628](https://datatracker.ietf.org/doc/html/rfc8628)) — designed for devices with no browser or limited input.
- **Server-to-server (M2M):** Client Credentials — no user involved, the app authenticates with its own credentials. Defined in [OAuth 2.1 §4.2](https://datatracker.ietf.org/doc/draft-ietf-oauth-v2-1/).


In 2026, OAuth 2 defines three primary grant types, each suited to different scenarios:  **Authorization Code**, **Client Credentials** and **Device Code**.

> [!Warning]: The OAuth framework specifies two additional grant types: the [**Implicit**](https://oauth.net/2/grant-types/implicit/) and the [**Password**](https://oauth.net/2/grant-types/password/) grant types. Both are considered insecure and are no longer recommended.

Now we will describe grant types in more detail, their use cases and flows, in the following sections.

#### Grant Type: Authorization Code + PKCE

The **authorization code** grant type is the most commonly used because it is optimized for *server-side applications*, where source code is not publicly exposed, and *Client Secret* confidentiality can be maintained. 

This is a **redirection-based flow**, which means that the application must be capable of interacting with the *user-agent* (i.e. the user's web browser) and receiving API authorization codes that are routed through the user-agent.

Example:

- Google uses the Authorization Code Grant to enable third-party applications to access services like Google Calendar on behalf of users.
- If you want to connect a productivity app to Google Calendar, the app will redirect you to a Google authorization page where you log in and grant access. Google then issues an authorization code to the app, which it exchanges for an access token to interact with your Google Calendar data.

Now we will describe the authorization code flow:

```mermaid
sequenceDiagram
    participant User as User (Browser)
    participant App as Third-party App (Server)
    participant Auth as Google (Authorization Server)
    participant API as Google Calendar API (Resource Server)

    Note over App,API: OAuth 2.0 Authorization Code Flow ("Connect with Google")

    User->>App: 1. Clicks "Connect Google Calendar"
    App-->>User: 2. Redirect to Google /authorize<br/>client_id + redirect_uri + scope + response_type=code + state
    User->>Auth: 3. Opens Google /authorize
    Auth-->>User: 4. Login (if needed) + consent screen
    User->>Auth: 5. Approves
    Auth-->>User: 6. Redirect back to redirect_uri<br/>with one-time code + state
    User->>App: 7. Browser follows redirect with code + state

    Note over App,Auth: Code is exchanged server-to-server
    App->>Auth: 8. POST /token with code<br/>(+ client_secret or PKCE code_verifier)
    Auth-->>App: 9. Returns Access Token (+ optional Refresh Token)

    App->>API: 10. Calls Calendar API with Authorization: Bearer ACCESS_TOKEN
    API-->>App: 11. Returns calendar data
    App-->>User: 12. Updates the UI
```

> [!TIP] 🌟⏩
> Experiment with Google's OAuth 2.0 playground to see how the flow works in practice: [OAuth 2.0 Playground](https://developers.google.com/oauthplayground).


##### Authorization Code Link

In the Authorization Code Grant flow, the **Authorization Code Link** is loaded by the user when the client application redirects them to the Authorization Server to initiate the authorization process.

The **Authorization Code Link** is generated by the client application and redirects the user’s browser to this link. This redirection initiates the authorization process.

Here is an explanation of a typical authorization link's components:

-   The **authorization endpoint URL**: the provider's `/authorize` endpoint
-   **client\_id=CLIENT_ID**: the application's *client ID* (how the API identifies the application)
-   **redirect\_uri=CALLBACK_URL**: where the service redirects the user-agent after an authorization code is granted
-   **response\_type=code**: specifies that your application is requesting an authorization code grant
-   **scope=...**: specifies the level of access that the application is requesting

##### Real-World Authorization URLs

Here is what the authorization URL looks like for the three major providers:

**Google** (e.g., requesting Calendar access):
```
https://accounts.google.com/o/oauth2/v2/auth?
  client_id=YOUR_CLIENT_ID
  &redirect_uri=https://yourapp.com/callback
  &response_type=code
  &scope=https://www.googleapis.com/auth/calendar.events.readonly
  &state=RANDOM_STATE
  &code_challenge=HASHED_CODE_VERIFIER
  &code_challenge_method=S256
```

**GitHub** (e.g., requesting repo and email access):
```
https://github.com/login/oauth/authorize?
  client_id=YOUR_CLIENT_ID
  &redirect_uri=https://yourapp.com/callback
  &scope=repo user:email
  &state=RANDOM_STATE
```

> [!NOTE]
> GitHub does not yet support PKCE for OAuth Apps (only for GitHub Apps). Check the [GitHub OAuth docs](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/authorizing-oauth-apps) for the latest status.

**Azure / Microsoft** (e.g., requesting user profile and mail access):
```
https://login.microsoftonline.com/{tenant-id}/oauth2/v2.0/authorize?
  client_id=YOUR_CLIENT_ID
  &redirect_uri=https://yourapp.com/callback
  &response_type=code
  &scope=User.Read Mail.Read
  &state=RANDOM_STATE
  &code_challenge=HASHED_CODE_VERIFIER
  &code_challenge_method=S256
```

##### Provider Comparison Table

| | Google | GitHub | Azure / Microsoft |
|---|---|---|---|
| **Authorize endpoint** | `accounts.google.com/o/oauth2/v2/auth` | `github.com/login/oauth/authorize` | `login.microsoftonline.com/{tenant}/oauth2/v2.0/authorize` |
| **Token endpoint** | `oauth2.googleapis.com/token` | `github.com/login/oauth/access_token` | `login.microsoftonline.com/{tenant}/oauth2/v2.0/token` |
| **Scope format** | URL-based (e.g., `googleapis.com/auth/calendar`) | Space-separated keywords (e.g., `repo user:email`) | Microsoft Graph permissions (e.g., `User.Read Mail.Read`) |
| **PKCE support** | Required | GitHub Apps only (not OAuth Apps) | Required |
| **Docs** | [Google OAuth 2.0](https://developers.google.com/identity/protocols/oauth2) | [GitHub OAuth](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/authorizing-oauth-apps) | [Microsoft identity platform](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-auth-code-flow) |

More resources:

-   [What is the OAuth 2.0 Authorization Code Grant?](https://developer.okta.com/blog/2018/04/10/oauth-authorization-code-grant-type) (developer.okta.com)
-   [Authorization Code](https://www.oauth.com/oauth2-servers/access-tokens/authorization-code-request/) (oauth.com)
-   [Web Server Apps](https://aaronparecki.com/oauth-2-simplified/#web-server-apps) (aaronparecki.com)
-   [Authorization Code Grant on the OAuth 2.0 Playground](https://www.oauth.com/playground/authorization-code.html)


##### Step 2: User Authorizes Client Application Access

When the user clicks the link, they must first log in to the service to authenticate their identity (unless they are already logged in). Then they will be prompted by the service to *authorize* or *deny* the application access to their account. Each provider shows a consent screen listing the requested permissions.

##### Step 3 — Application Receives Authorization Code

If the user clicks **Allow**, the service redirects the user-agent to the application **redirect URI**, which was specified during the client registration, along with an *authorization code*. The redirect would look something like this:

```
https://yourapp.com/callback?code=AUTHORIZATION_CODE&state=RANDOM_STATE
```

##### Step 4 — Application Requests Access Token

The application requests an access token from the API by passing the authorization code along with authentication details, including the *client secret*, to the API token endpoint. Here are real-world `POST` request examples:

**Google:**
```bash
curl -X POST https://oauth2.googleapis.com/token \
  -d "code=AUTHORIZATION_CODE" \
  -d "client_id=CLIENT_ID" \
  -d "client_secret=CLIENT_SECRET" \
  -d "redirect_uri=https://yourapp.com/callback" \
  -d "grant_type=authorization_code" \
  -d "code_verifier=ORIGINAL_CODE_VERIFIER"
```

**GitHub:**
```bash
curl -X POST https://github.com/login/oauth/access_token \
  -H "Accept: application/json" \
  -d "client_id=CLIENT_ID" \
  -d "client_secret=CLIENT_SECRET" \
  -d "code=AUTHORIZATION_CODE" \
  -d "redirect_uri=https://yourapp.com/callback"
```

**Azure / Microsoft:**
```bash
curl -X POST https://login.microsoftonline.com/{tenant-id}/oauth2/v2.0/token \
  -d "client_id=CLIENT_ID" \
  -d "client_secret=CLIENT_SECRET" \
  -d "code=AUTHORIZATION_CODE" \
  -d "redirect_uri=https://yourapp.com/callback" \
  -d "grant_type=authorization_code" \
  -d "code_verifier=ORIGINAL_CODE_VERIFIER"
```

##### Step 5 — Application Receives Access Token

If the authorization is valid, the API will send a response containing the access token (and optionally, a refresh token) to the application. Here is an example response (Google):

```json
{
    "access_token": "ya29.a0AeDClZC...",
    "token_type": "Bearer",
    "expires_in": 3599,
    "refresh_token": "1//04XqEBsQXBryd...",
    "scope": "https://www.googleapis.com/auth/calendar.events.readonly"
}
```

Now the application is authorized. It may use the token to access the user's account via the service API, limited to the scope of access, until the token expires or is revoked.

If a **refresh token** was issued, it may be used to request new access tokens if the original token has expired.


##### PKCE - Note Regarding Proof Key for Code Exchange

If a public client is using the Authorization Code grant type, there's a chance that the authorization code could be intercepted. The *Proof Key for Code Exchange* (or *PKCE*, pronounced like "pixie") is an extension to the Authorization Code flow that helps to mitigate this kind of attack.

The PKCE extension involves the client creating and recording a secret key — known as a *code verifier* — for every authorization request. The client then transforms the code verifier into a *code challenge* **using a hashing mechanism (usually SHA-256)**. This transformation provides an added layer of security by ensuring that even if the code challenge is exposed, it cannot be reverse-engineered to reveal the original code verifier. The client sends the hashed *code challenge* (not the code verifier) and the transformation method to the authorization endpoint in the same authorization request.

The authorization endpoint records the code challenge and the transformation method, and responds with the authorization code as outlined previously. The client then sends in the access token request, **which includes the original, unmodified code verifier**.

Upon receiving the code verifier, the authorization server **hashes it with the specified algorithm (e.g., SHA-256) to recreate the code challenge**. It compares this recreated code challenge with the one initially sent by the client. **If they don’t match, the authorization server denies access,** preventing the completion of the authorization flow.

In short, PKCE protects against authorization code interception by requiring a *code verifier*, which only the original client possesses. When a client sends an authorization request, it includes a **hashed version of the code verifier (the *code challenge*)**. Later, to complete the exchange, the client provides **the original code verifier (without hashing it again)**, allowing the authorization server to hash it and verify its authenticity. This verification ensures that only the original client that initiated the authorization request can exchange the code for an access token, effectively preventing authorization code interception attacks.

> [!Note]: It's recommended that every client use the PKCE extension for improved security.



###### PKCE Example in attack scenario

You’re absolutely right; in practice, if an attacker is capable of intercepting one request (the authorization code), they’d likely be able to intercept the second request (the token exchange) as well. Here’s a breakdown of why PKCE is still valuable despite this:

1. **Different Attack Vectors**:  
   In most scenarios, an attacker might exploit weaknesses specifically at one point in the flow, rather than across the whole flow. Here are a few cases where interception of only the authorization code could happen:
   - **Browser-Based Redirect Attacks**: An attacker might intercept the authorization code by tricking the browser into redirecting to a malicious URI, capturing the authorization code without being able to monitor the token exchange, which usually takes place over a backend-to-backend communication.
   - **Open Redirect Vulnerabilities**: If the client application is vulnerable to open redirects, an attacker could exploit this vulnerability to capture the authorization code by having the user redirect to a malicious URL during the authorization flow. But they would still lack access to the secure backend where the token exchange occurs.

2. **Network and Device Vulnerabilities**:  
   In cases of **network vulnerabilities** (e.g., open Wi-Fi networks) or **device vulnerabilities** (e.g., compromised browser extensions), an attacker could intercept front-channel communication in the browser (which is how the authorization code is typically sent back to the client) without having access to the backend-to-backend channel where the token request is securely sent.

3. **Intercepting Only the Code Is Useless with PKCE**:  
   PKCE protects the authorization code by making it useless on its own. Without PKCE, an attacker intercepting the authorization code could directly exchange it for an access token. With PKCE, however, even if an attacker intercepts the authorization code, they still need the code verifier, which was generated by the original client and never sent in the initial authorization request.

```mermaid
sequenceDiagram
    participant Client
    participant User
    participant AuthServer as Authorization Server
    participant API

    User->>Client: Requests access to protected resource
    Client->>AuthServer: Redirects user with Authorization Code Link<br/>(includes code challenge)
    AuthServer->>User: Prompts user to login and authorize
    User->>AuthServer: Logs in and authorizes access
    AuthServer->>Client: Redirects back with Authorization Code
    Client->>AuthServer: Sends Authorization Code with code verifier to request access token
    AuthServer->>Client: Returns Access Token (if verifier matches challenge)
    Client->>API: Accesses protected resource with Access Token
    API->>Client: Returns requested resource
```

###### Why PKCE and Backend Security Together Are Powerful
The PKCE flow is highly effective for public clients, especially those that perform part of the OAuth flow in a front channel (e.g., a mobile app or single-page app). By using PKCE and HTTPS together, it’s challenging for attackers to intercept both the authorization code and the code verifier, particularly since the verifier is only sent in the backend-to-backend request where intercepting it is even harder.

```mermaid
sequenceDiagram
    participant User
    participant ApplicationClient as ApplicationClient (Front-End)
    participant ApplicationBackend as ApplicationBackend (Server)
    participant AuthServer as Authorization Server
    participant API

    User->>ApplicationClient: Requests access to protected resource
    ApplicationClient->>AuthServer: Redirects user with Authorization Code Link<br/>(includes code challenge)
    AuthServer->>User: Prompts user to login and authorize
    User->>AuthServer: Logs in and authorizes access
    AuthServer->>ApplicationClient: Redirects back with Authorization Code

    rect rgb(0, 100, 0)
    note right of ApplicationBackend: This happens in a safer and controlled network
    ApplicationClient->>ApplicationBackend: Sends Authorization Code to ApplicationBackend securely
    ApplicationBackend->>AuthServer: Requests Access Token with Authorization Code<br/>and code verifier
    AuthServer->>ApplicationBackend: Verifies and returns Access Token
    end

    ApplicationBackend->>ApplicationClient: Sends Access Token to ApplicationClient
    ApplicationClient->>API: Accesses protected resource with Access Token
    API->>ApplicationClient: Returns requested resource
```



#### Grant Type: Client Credentials
The **client credentials** grant type provides an application a way to access resources on its own behalf, without a user involved (machine-to-machine). Common use cases include backend services calling APIs, CI/CD pipelines, microservice-to-microservice communication, and batch processing jobs.

##### Client Credentials Flow

The application requests an access token by sending its credentials, its client ID and client secret, to the authorization server. Here are real-world examples:

**Google** (using a service account with JWT assertion):
```bash
# Google uses service account JSON keys rather than client_id/client_secret.
# The Google client libraries handle JWT creation automatically.
# With the gcloud CLI:
gcloud auth application-default print-access-token

# Or programmatically, the library exchanges a signed JWT for an access token:
# POST https://oauth2.googleapis.com/token
#   grant_type=urn:ietf:params:oauth:grant-type:jwt-bearer
#   assertion=SIGNED_JWT
```

**GitHub** (GitHub App installation token):
```bash
# GitHub Apps use a JWT signed with the app's private key
# to request an installation access token:
curl -X POST https://api.github.com/app/installations/{installation_id}/access_tokens \
  -H "Authorization: Bearer YOUR_JWT" \
  -H "Accept: application/vnd.github+json"
```

**Azure / Microsoft:**
```bash
curl -X POST https://login.microsoftonline.com/{tenant-id}/oauth2/v2.0/token \
  -d "client_id=CLIENT_ID" \
  -d "client_secret=CLIENT_SECRET" \
  -d "scope=https://graph.microsoft.com/.default" \
  -d "grant_type=client_credentials"
```

If the application credentials check out, the authorization server returns an access token to the application. Now the application is authorized to access the resources it has been granted permissions for.

> [!NOTE]
> Each provider handles M2M authentication differently. Google prefers service account keys with JWT assertions, GitHub uses app-level JWTs, and Azure uses the standard `client_credentials` grant type directly.

#### Grant Type: Device Code

The **device code** grant type provides a means for devices that lack a browser or have limited inputs to obtain an access token and access a user's account. The purpose of this grant type is to make it easier for users to more easily authorize applications on such devices to access their accounts. Examples of when this might be useful include if a user wants to sign into a video streaming application on a device that doesn't have a typical keyboard input, such as a smart television or a video game console.

##### Example of an application using the device code flow

This grant type is employed by applications on devices with limited input capabilities or without a browser. Examples include:

-   Smart TVs and Media Consoles: Applications on platforms like Apple TV or Roku use the Device Code flow to allow users to authenticate via a secondary device, such as a smartphone or computer. (OAuth)
-   IoT Devices: Devices like printers or smart home gadgets utilize this flow to enable user authentication through another device with a browser. (Melman M)
-   Command-Line Interface (CLI) Applications: Tools running in terminal environments, such as certain Azure CLI commands, implement the Device Code flow to facilitate user authentication without launching a browser. (Microsoft Learn)

These applications prompt users to **visit a specific URL on a secondary device and enter a code displayed on the primary device**, enabling authentication without direct input on the device itself.

For example in this tutorial, when you run the application on your terminal, it will prompt you to visit a URL and enter a code displayed on your terminal ([A Node headless application using MSAL Node to authenticate users with the device code flow against Microsoft Entra External ID](https://learn.microsoft.com/en-us/samples/azure-samples/ms-identity-ciam-javascript-tutorial/ms-identity-ciam-javascript-tutorial-4-sign-in-device-code/) )

This the application prompts you to when you run it:

1.  Copy the suggested URL `https://microsoft.com/devicelogin` from the message in the terminal and open it in the browser. Then copy the device code from the message in the terminal. ![Screenshot](https://learn.microsoft.com/en-us/samples/azure-samples/ms-identity-ciam-javascript-tutorial/ms-identity-ciam-javascript-tutorial-4-sign-in-device-code/media/code.png)
2.  Past the code in the Enter code prompt to sign in.
    ![Screenshot](https://learn.microsoft.com/en-us/samples/azure-samples/ms-identity-ciam-javascript-tutorial/ms-identity-ciam-javascript-tutorial-4-sign-in-device-code/media/prompt.png)
3.  Head back to the terminal to see your authentication information.




##### Device Code Flow

First, watch this video for a more interactive explanation of the device code flow: [https://www.youtube.com/watch?v=QdFjaOb-KTs](https://www.youtube.com/watch?v=QdFjaOb-KTs)


The user starts an application on their browserless or input-limited device, such as a television or a set-top box. The application submits a `POST` request to a *device authorization endpoint*.



Here are real-world device code `POST` request examples:

**GitHub CLI** (`gh auth login`):
```bash
POST https://github.com/login/device/code
  client_id=YOUR_CLIENT_ID
  scope=repo user
```

**Azure CLI** (`az login --use-device-code`):
```bash
POST https://login.microsoftonline.com/{tenant-id}/oauth2/v2.0/devicecode
  client_id=YOUR_CLIENT_ID
  scope=User.Read
```


The device authorization endpoint is different from the authentication server, as the device authorization endpoint doesn't actually authenticate the device. Instead, it returns a unique *device code*, which is used to identify the device; a *user code*, which the user can enter on a machine on which it's easier to authenticate, such as a laptop or mobile device; and the URL the user should visit to enter the user code and authenticate their device.

Here's what an example response from the device authorization endpoint might look like (GitHub):

```json
{
  "device_code": "3584d83530557fdd1f46af8289938c8ef79f9dc5",
  "user_code": "WDJB-MJHT",
  "verification_uri": "https://github.com/login/device",
  "interval": 5,
  "expires_in": 900
}
```

Note that the device code could also be a QR code which the reader can scan on a mobile device.

The user then enters the user code at the specified URL and signs into their account. They are then presented with a consent screen where they can authorize the device to access their account.

While the user visits the verification URL and enters their code, the device will poll the access endpoint until it returns an error or an authentication token. The access endpoint will return errors if the device is polling too frequently (the `slow_down` error), if the user hasn't yet approved or denied the request (the `authorization_pending` error), if the user has denied the request (the `access_denied` error), or if the token has expired (the `expired_token` error).

If the user approves the request, though, the access endpoint will return an authentication token.

##### Real-World Device Code Examples

Two of the most common real-world uses of the device code flow that developers encounter daily:

- **GitHub CLI** (`gh`): When you run `gh auth login`, it displays a code and asks you to visit `https://github.com/login/device`. This is the device code flow in action. [GitHub Device Flow docs](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/authorizing-oauth-apps#device-flow)
- **Azure CLI** (`az`): Running `az login --use-device-code` displays a code and directs you to `https://microsoft.com/devicelogin`. [Azure Device Code docs](https://learn.microsoft.com/en-us/cli/azure/authenticate-azure-cli#sign-in-with-a-device-code)

## Claims and Identity Tokens

For details on claims (structured key-value pairs embedded in tokens like JWTs) and how they are used for identity verification, see [OIDC Protocol Explanation](oidc-protocol-explanation.md).

## Example Access Token Usage

Once the application has an access token, it may use the token to access the user's account via the API, limited to the scope of access, until the token expires or is revoked.

Here are examples of API requests using `curl` with an access token:

**Google Calendar API:**
```bash
curl -H "Authorization: Bearer ACCESS_TOKEN" \
  "https://www.googleapis.com/calendar/v3/calendars/primary/events"
```

**GitHub API:**
```bash
curl -H "Authorization: Bearer ACCESS_TOKEN" \
  -H "Accept: application/vnd.github+json" \
  "https://api.github.com/user/repos"
```

**Microsoft Graph API:**
```bash
curl -H "Authorization: Bearer ACCESS_TOKEN" \
  "https://graph.microsoft.com/v1.0/me/messages"
```

Assuming the access token is valid, the API will process the request according to its API specifications. If the access token is expired or otherwise invalid, the API will return an error (typically `401 Unauthorized`).

## Refresh Token Flow

After an access token expires, using it to make a request from the API will result in an `Invalid Token Error`. At this point, if a refresh token was included when the original access token was issued, it can be used to request a fresh access token from the authorization server.

Here is an example `POST` request using a refresh token to obtain a new access token (Google):

```bash
curl -X POST https://oauth2.googleapis.com/token \
  -d "client_id=CLIENT_ID" \
  -d "client_secret=CLIENT_SECRET" \
  -d "refresh_token=REFRESH_TOKEN" \
  -d "grant_type=refresh_token"
```

## Conclusion

By following this guide, you will have gained an understanding of how OAuth 2 works, and when a particular authorization flow should be used.

If you want to learn more about OAuth 2, check out these valuable resources:

-   [The OAuth 2.0 Authorization Framework - RFC 6749](https://datatracker.ietf.org/doc/html/rfc6749)
-   [OAuth 2.0 Simplified](https://aaronparecki.com/oauth-2-simplified/) (Aaron Parecki)
-   [Google OAuth 2.0 Documentation](https://developers.google.com/identity/protocols/oauth2)
-   [GitHub OAuth Apps Documentation](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/authorizing-oauth-apps)
-   [Microsoft Identity Platform and OAuth 2.0](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-auth-code-flow)
-   [OAuth 2.0 Playground (Google)](https://developers.google.com/oauthplayground)



## OIDC

OpenID Connect extends OAuth 2.0 by adding identity information in a standardized way, see [OIDC Protocol Explanation](oidc-protocol-explanation.md).
