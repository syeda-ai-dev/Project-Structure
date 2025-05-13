# FastAPI Project Structure Template

This repository provides a sample project structure for building scalable FastAPI applications. It's designed as an educational resource to help developers understand best practices for organizing Python backend applications.

## Project Overview

This template demonstrates a modular FastAPI application with the following features:

- Organized package structure with clear separation of concerns
- Containerization with Docker and Docker Compose
- Nginx as a reverse proxy for production deployment
- Environment variable management
- Modular service architecture
- Singleton configuration pattern

## Directory Structure

```
├── com/
│   └── mhire/
│       └── app/
│           ├── config/
│           │   └── config.py           # Configuration management
│           ├── database/
│           │   ├── database_connection.py  # Database connection (placeholder)
│           │   └── database_manager.py     # Database operations (placeholder)
│           ├── main.py                 # Application entry point
│           └── services/
│               ├── feature_1/          # Example service module
│               │   ├── feature_1.py            # Service implementation
│               │   ├── feature_1_router.py     # FastAPI router
│               │   └── feature_1_schema.py     # Pydantic models
│               └── feature_n/          # Template for additional services
│                   ├── feature_n.py
│                   ├── feature_n_router.py
│                   └── feature_n_schema.py
├── .dockerignore
├── .env                        # Environment variables
├── .gitignore
├── Dockerfile                  # Docker configuration
├── docker-compose.yml          # Docker Compose configuration
├── nginx/
│   └── nginx.conf              # Nginx configuration
└── requirements.txt            # Python dependencies
```

## Key Components

### FastAPI Application

- **main.py**: The entry point that configures and starts the FastAPI application
- **services/**: Contains modular service implementations, each with:
  - Service logic (feature_x.py)
  - API routes (feature_x_router.py)
  - Data models (feature_x_schema.py)

### Configuration

- **config/config.py**: Implements a singleton pattern for application configuration
- **.env**: Stores environment variables (API keys, model names, etc.)

### Docker Setup

- **Dockerfile**: Configures the Python application container
- **docker-compose.yml**: Orchestrates the application and Nginx containers
- **nginx/nginx.conf**: Configures Nginx as a reverse proxy

## Getting Started

### Prerequisites

- Python 3.12+
- Docker and Docker Compose (for containerized deployment)

### Local Development

1. Clone this repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file with required environment variables
5. Run the application:
   ```bash
   uvicorn com.mhire.app.main:app --reload
   ```

### Docker Deployment

1. Build and start the containers:
   ```bash
   docker-compose up -d --build
   ```
2. Access the API at http://ipv4-address

## Adding New Features

To add a new feature/service to the application:

1. Create a new directory under `com/mhire/app/services/` (e.g., `new_feature/`)
2. Create the following files:
   - `new_feature.py`: Service implementation
   - `new_feature_router.py`: FastAPI router
   - `new_feature_schema.py`: Pydantic models
3. Import and register the router in `main.py`

## Best Practices Demonstrated

- **Modular Architecture**: Each feature is self-contained with its own router and schemas
- **Dependency Injection**: Services are initialized and injected where needed
- **Configuration Management**: Environment variables are loaded and managed centrally
- **Error Handling**: Consistent error handling with proper HTTP status codes
- **Containerization**: Docker setup for consistent deployment
- **Logging**: Structured logging throughout the application