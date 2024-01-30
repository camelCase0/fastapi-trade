

# FastAPI demo backend app 
[![Deploy buy runner](https://github.com/camelCase0/fastapi-trade/actions/workflows/deploy-job.yml/badge.svg?branch=master)](https://github.com/camelCase0/fastapi-trade/actions/workflows/deploy-job.yml)

Brief project description and what it does.

## Features
- **FastAPI** Backend with Swagger documentation
- **Registration and Authorization:** Users can register and log in securely using FastAPI authentication.
- **Email Sending:** Integration with an email sending service for user notifications.
- **Celery Workers Task Queuing:** Asynchronous task execution using Celery for background processing.
- **Flower Manager:** Monitoring and management of Celery workers with Flower.
- **Persistence:** Data storage in PostgreSQL using SQLAlchemy.
- **Docker and Docker Compose:** Easy deployment and management of containers.
- **Redis:** Usage of Redis for caching or other purposes.
- **Unit Tests:** Comprehensive unit tests using PyTest.
- **GitHub Actions Workflows:** Automated workflows for running tests in development and production environments.

## Prerequisites

- Python (version)
- Docker and Docker Compose
- PostgreSQL
- Redis

## Getting Started
**Setup without docker:**
For this you need to config database redis and celery workers manually!

1. Clone the repository:

   ```bash
   git clone https://github.com/camelCase0/fastapi-trade.git

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
4. Copy the .env.example file to .env and configure the environment variables:
   ```bash
   cp .env.example .env
 ## Docker setup
 1. Install docker
    ```bash
    docker compose version # check version of docker compose
 2. Start containers
    ```bash
    docker compose up -d
 3. Open your web browser and access the application at http://localhost:{PORT}.
    At http://localhost:{PORT}/docs you can find Swagger documentation
