# Printshop Project Setup & Run Roadmap

This roadmap provides a comprehensive, step-by-step guide to setting up, running, and developing the Printshop project, synthesizing all instructions and referenced links from the README. It covers local development, environment configuration, AWS, Docker, database, testing, API docs, and deployment.

---

## 1. Prerequisites

- **Docker & Docker Compose** (install [Docker Desktop](https://www.docker.com/products/docker-desktop/) for Mac/Windows)
- **Yarn** (see [Yarn installation guide](https://classic.yarnpkg.com/en/docs/install/))
- **AWS CLI** ([Install & configure](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html))
- **Text Editor** (VSCode, Cursor, etc.)
- **Git**

---

## 2. Clone the Repository

```sh
git clone <repo-url>
cd printshop
```

---

## 3. Environment Configuration

### 3.1. Environment Files Overview

- **.env** (project root):
  - Used at the docker-compose (build) stage. Required for private gem access.
  - **Required variable:**
    ```
    BUNDLE_GEMS__CONTRIBSYS__COM=<USERNAME:PASSWORD>
    ```
- **.envs/development/aws**:
  - Initially blank. Will be populated by the AWS MFA authentication script.
- **.envs/development/web**:
  - Application secrets for the web container.
- **.envs/development/database**:
  - Database credentials for the database container.

### 3.2. Create and Populate Environment Files

- Download the [Credentials File](https://trevipay-my.sharepoint.com/:w:/p/jrsimmons/EWCVzNXBe-vkRrw8_JHd-SsBNhEB3KEUa0QMYkcinxuFEw?e=CJvQ39) and follow its instructions.
- Create the following files (if not present):
  - `.env` (at project root)
  - `.envs/development/aws` (blank)
  - `.envs/development/web`
  - `.envs/development/database`

#### Example `.env` (project root):
```
BUNDLE_GEMS__CONTRIBSYS__COM=<USERNAME:PASSWORD>
```

#### Example `.envs/development/web`:
```
DATABASE_HOST=database
DEVELOPER_EMAIL=<your_email_here!!!>@msts.com
DEVELOPER_PASSWORD=<enter a value here if you want seeds.rb to handle development user setup for you>
LOCKBOX_MASTER_KEY=<to_be_filled_in_later; see Lockbox instructions>
PWS_PORT=<opdev04 port>
PWS_SERVICE_USER_TOKEN=<add test service user token here; optional>
REDIS_URL=redis://redis:6379/0
RW_SERVICE_USER_CREDS=X-API-Key:<GET CREDS FROM LINK>
LIBELLUS_TOKEN=Token:<GET CREDS FROM LINK>
```

#### Example `.envs/development/database`:
```
POSTGRES_USER=postgres
POSTGRES_PASSWORD=<password you make up or generate>
POSTGRES_DB=printshop_development
```

---

## 4. AWS MFA Authentication

- Follow the [AWS_MFA README](https://gitlab.com/msts-enterprise/printshop/aws_mfa) to populate `.envs/development/aws`.

---

## 5. System Configuration: Transparent Huge Page (THP)

- **Linux:**
  - Add `echo never > /sys/kernel/mm/transparent_hugepage/enabled` to `/etc/rc.local`.
- **Mac:**
  - Run inside Docker VM:
    ```sh
    docker run -it --privileged --pid=host debian nsenter -t 1 -m -u -n -i sh
    echo never > /sys/kernel/mm/transparent_hugepage/enabled
    echo never > /sys/kernel/mm/transparent_hugepage/defrag
    exit
    ```
- **Windows:**
  - SSH into Docker VM and run the above commands.

---

## 6. Install Dependencies

```sh
yarn install
```

---

## 7. Build Docker Images

```sh
docker-compose build web
# Build Sidekiq workers
for svc in sidekiq-main sidekiq-render sidekiq-gather; do docker-compose build $svc; done
```

---

## 8. Start Services

```sh
docker-compose up -d
```

---

## 9. Generate Lockbox Key

```sh
docker-compose exec web bin/rails c
# In the Rails console:
Lockbox.generate_key
```
- Copy the generated key into `LOCKBOX_MASTER_KEY` in `.envs/development/web`.
- Rebuild and restart the web container:
```sh
docker-compose stop web
docker-compose build web
docker-compose up -d --force-recreate web
```

---

## 10. Database Setup

```sh
docker-compose exec web bin/rails db:create
docker-compose exec web bin/rails db:migrate
docker-compose exec web bin/rails db:seed
# Or run all at once (including test env):
docker-compose exec web bin/rails run_all:db_new
```

---

## 11. Running Tests

```sh
docker-compose exec web bin/rails test
docker-compose exec web bundle exec rubocop
# Or all tests:
docker-compose exec web bin/rails run_all:tests
```

---

## 12. API Documentation

- Access API docs at: `http://<host_url>/api-docs`
- [rswag-api & rwag-ui](https://github.com/rswag/rswag)
- [mini-apivore](https://github.com/alekseyl/mini-apivore)
- Validate OpenAPI spec with [Swagger Editor](http://editor.swagger.io/#):
  ```sh
  docker pull swaggerapi/swagger-editor
  docker run -d -p 80:8080 swaggerapi/swagger-editor
  # Access at http://localhost
  ```
- To generate combined swagger.json:
  ```sh
  ./docker_build_api_docs
  ```

---

## 13. Development Tips

- **Rebuilding the web image:**
  ```sh
  docker-compose stop web
  docker-compose build web
  docker-compose up -d --force-recreate web
  ```
- **Install/update gems:**
  ```sh
  docker-compose exec web bundle install
  docker-compose exec web bundle update [GEM]
  ```
- **If gem_cache volume is corrupted:**
  ```sh
  docker-compose down
  docker volume rm printshop_gem_cache
  ```
- **Connect to the database:**
  ```sh
  docker-compose run --rm database psql -U postgres -h database
  # Then: \c printshop_development
  ```

---

## 14. API Authentication

- Use headers:
  - `X-User-Email: <developer_email_address_used_in_env_vars>`
  - `X-User-Token: <token from User.first.authentication_token in rails console>`

---

## 15. Deployment & Kubernetes

- **CI/CD:** Uses GitLab CI/CD and Helm charts for k8s deployment.
- **Helm files:**
  - `Chart.yaml`, `values.yaml`, `chart/`, `chart/templates/`
- **kubectl setup:**
  - [Install kubectl](https://msts.gitlabpages.msts.com/kubernetes-guidelines/authentication/#download-and-install-kubectl)
  - [EKS Client Checklist](https://gitlab.com/msts-enterprise/devops/kubernetes/blob/master/eks/EKS-CLIENT-CHECKLIST.md#client-steps)
  - Create config:
    ```sh
    touch ~/.kube/config
    export KUBECONFIG=$HOME/.kube/config
    export TILLER_NAMESPACE=printshop
    ```
  - Create EKS context:
    ```sh
    # Staging
    aws eks --region us-east-1 update-kubeconfig --name staging-green --alias printshop-staging-green --role-arn arn:aws:iam::434875166128:role/MstsPrintshopStagingEKSRole
    # Production
    aws eks --region us-east-1 update-kubeconfig --name production-green --alias printshop-production-green --role-arn arn:aws:iam::434875166128:role/MstsPrintshopProductionEKSRole
    ```
  - Switch context:
    ```sh
    kubectl config set-context printshop-staging-green --namespace=printshop
    kubectl config set-context printshop-production-green --namespace=printshop
    ```
  - Useful aliases:
    ```sh
    alias k=kubectl
    alias kcs='kubectl config use-context printshop-staging-green'
    alias kcp='kubectl config use-context printshop-production-green'
    ```
  - View pods/logs:
    ```sh
    kubectl get pods
    kubectl logs <podname>
    kubectl describe pod <podname>
    kubectl get jobs
    kubectl delete job <job_name>
    ```
  - [kubectl command reference](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#describe)

---

## 16. Miscellaneous

- **Ubuntu file ownership:**
  ```sh
  sudo chown <your_username>:<your_username> -R *
  ```

---

## 17. References & Further Reading

- [AWS_MFA README](https://gitlab.com/msts-enterprise/printshop/aws_mfa)
- [Disable Transparent Huge Page (THP)](https://redis.io/docs/management/latency/#linux-transparent-huge-pages-thp)
- [Swagger Editor](http://editor.swagger.io/#)
- [Kubernetes kubectl command reference](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#describe)

---

**You are now ready to develop, test, and deploy the Printshop project!** 