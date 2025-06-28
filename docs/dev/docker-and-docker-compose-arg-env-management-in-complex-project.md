# Docker Compose Environment Variables and Build Arguments Management in Complex Projects


## Scope of the document

The scope of this document is to explain the different ways to manage environment variables and build arguments in complex projects, to make easy to create development, testing and production mode with docker compose.

It's divided into the following sections:

* [General considerations](#general-considerations): describes the general considerations for managing environment variables and build arguments in complex projects.
* [Opinionated strategies](#opinionated-strategies): describes some opinionated strategies for managing environment variables and build arguments in complex projects.



## General considerations

### Glossary

**MODE**: A set of scripts, instructions, and configurations that creates specific conditions to achieve a defined goal. Each MODE must have clear, documented purpose and justification for its existence.

### Embracing a DevOps Mentality: Consistency, Automation, and Collaboration

A DevOps mentality emphasizes consistency, automation, and collaboration, aiming to bridge the gap between development and operations for streamlined deployment and faster iteration. This mindset involves viewing every service as part of a cohesive system, where standardized interfaces and predictable configurations reduce friction and enable seamless integration. By adhering to immutability principles in our Docker Compose structure, we empower teams to:

- **Automate Configuration and Deployment**: Leveraging Docker Compose and predefined service interfaces minimizes manual setup, enabling automated, repeatable deployments that align with CI/CD practices.
- **Promote Cross-Functional Collaboration**: Clear, documented service interfaces and consistent configuration standards allow developers, sysadmins, and other stakeholders to work effectively across teams, reducing miscommunication and simplifying troubleshooting.
- **Enable Rapid, Reliable Releases**: Standardizing configuration interfaces allows changes to be rolled out quickly, with reduced risk of unexpected conflicts. This consistency accelerates testing, feedback loops, and deployment, driving continuous improvement.
  
With this DevOps approach, teams can focus on delivering value, continuously improving workflows, and building a robust, scalable infrastructure that evolves alongside business needs.

### Service Interface Standards: 12-Factor and File-Based Configuration

Each service we run needs to be viewed as its own isolated component, with predefined, unalterable interfaces. This setup is essential for maintaining consistency, flexibility, and reliability across our application ecosystem. Here’s how we apply this in practical terms:

1. **Service Interface Standards**
   - Every service exposes two main interfaces: the **12-factor interface** (configurable through environment variables) and the **file-based interface** (configured through volume mounts or Dockerfile specifications).
   - The rule: these interfaces are immutable. Our Docker Compose files should respect these fixed points, focusing on configuring the service, not altering its underlying behavior or code.
   - Most Docker images on Docker Hub adhere to this model, utilizing environment variables for runtime configuration and supporting file-based interface setups through volume mounts. When deeper customization is needed, we can extend a service by building a new image based on the existing one. This approach allows for a high level of flexibility, balancing customization needs with the consistency and reliability of the original service structure.

2. **Configuring the 12-Factor Interface**
   - Environment variables allow us to tailor services without altering their code. We do this by setting configurations within the `environment` node or linking an `env_file` in the Docker Compose file. This approach aligns with the 12-factor app principles, giving us configuration flexibility while ensuring separation of service code and runtime setup.
   - When preparing a service, avoid the temptation to re-engineer its environment variable expectations. Instead, work within the constraints of what’s already provided by the service, especially when using official, upstream Docker images. Modifications are possible when building custom services, but standardized interfaces keep deployment predictable and reliable.

3. **File-Based Interface Setup**
   - For services that rely on files, such as configuration files or directories, we manage these through volume mounts specified in Docker Compose or by tailoring the Dockerfile to suit file dependencies. This allows the code to remain untouched, with configuration adjustments handled at the container level.
   - Many Docker Hub images support this file-based interface approach, allowing for straightforward configuration via volume mounts. For more extensive changes, a new Docker image can be built, extending the existing one to customize configuration while respecting the original file-based interface.

4. **Design Intent in Docker Compose**
   - Our Docker file structure is designed around the principle that a **service’s interface is constant**. This assumption serves to prevent accidental changes to critical configurations. For instance, if we are using an official Postgres image, it’s best to assume that the 12-factor interface is fixed and immutable, keeping our setup focused on deployment configurations, not core service modifications.
   - This mindset also builds a balance between flexibility and clarity. Developers can quickly understand the configuration without delving into undocumented interface changes. 

5. **Documentation Requirement**
   - Every service **must** clearly document its interfaces. This documentation should cover the required environment variables, expected file-based inputs or volumes, and any critical configuration instructions. This transparency helps developers use services effectively while respecting the design constraints of Docker Compose and the interfaces set by each service.

By adhering to these principles, we create a stable and predictable environment that developers can rely on, minimizing surprises during deployments and ensuring compatibility across different setups.






### Environment variables precedence in Docker Compose

This official Docker Compose documentation page explains the precedence of environment variables in Docker Compose: [Environment variables precedence in Docker Compose](https://docs.docker.com/compose/how-tos/environment-variables/envvars-precedence/)




You can set default values for environment variables using a [`.env` file](https://docs.docker.com/compose/env-file/), which Compose automatically looks for in project directory (parent folder of your Compose file). Values set in the shell environment override those set in the `.env` file.



## WIP 
- Considerazioni su notion
- Collegarsi alle considerazioni sui Settings di Djiango e fare una pensata anche per fastapi


Provare a fare un diagramma che spieghi la metafora del wiring 




## Opinionated Strategies

### Variable wiring 








