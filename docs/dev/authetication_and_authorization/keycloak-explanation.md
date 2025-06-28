
[Keycloak Discourse](https://keycloak.discourse.group/)
HOWTOS: [Keycloak Howtos](./keycloak-howtos.md)

## Server Configuration

### Config Keycloak - General Overview

> [!NOTE] For specific configuration we commonly use the HOWTOS: [Keycloak Howtos](./keycloak-howtos.md)

Guide: [Keycloak - Server Configuration](https://www.keycloak.org/server/configuration)

**All config options (and their corresponding environment variables):** [Keycloak - All configuration](https://www.keycloak.org/server/all-config)

As Keycloak can be configured independently from how it is deployed/operated, you won't find a deployment-specific config document. No matter how Keycloak is deployed, one can use all options to configure Keycloak.

For specific configuration see the HOWTOS: [Keycloak Howtos](./keycloak-howtos.md)

### Config Keycloak - Logging

Guide: [Keycloak - Configuration - Logging](https://www.keycloak.org/server/logging)

Keycloak is a tool that manages authentication for applications, allowing you to set up login screens, user permissions, and more. Understanding logging in Keycloak is helpful for tracking errors, monitoring activity, and managing system performance. Here’s a guide to setting up and understanding Keycloak logging.

#### Key Concepts

1. **Logging Levels**: Different levels of logging allow you to control how much detail is recorded. The most common levels are:
   - **ERROR**: Logs only serious issues that need immediate attention.
   - **WARN**: Logs potentially harmful situations but may not require immediate action.
   - **INFO**: Logs general information about system processes, like server start-up.
   - **DEBUG**: Logs detailed diagnostic information (useful for developers).
   - **TRACE**: Logs even more detail than DEBUG, including specific steps in processing.

2. **Log Handlers**: Handlers are components that manage the way log messages are displayed or stored.
   - **Console Handler**: Displays logs in the terminal or command line.
   - **File Handler**: Stores logs in a file for later review.
   - **Syslog Handler**: Sends logs to a system log server.
   - **Socket Handler**: Sends logs to a specific network location.

   Each handler type can be configured for different logging levels, so you can direct specific kinds of messages to the console or save others to a file.

#### Configuring Logging in Keycloak

To set up logging in Keycloak, you can configure the **standalone.xml** or **standalone-ha.xml** file (these are configuration files used by the server).

##### Steps:

1. **Locate the Config File**:
   - Go to the folder where Keycloak is installed.
   - Open the **standalone/configuration** folder and locate **standalone.xml**.

2. **Adjust Logging Levels**:
   - In the configuration file, you’ll see sections for various handlers.
   - Set the level (ERROR, WARN, INFO, etc.) as needed.

   Example:
   ```xml
   <logger category="org.keycloak">
       <level name="INFO"/>
   </logger>