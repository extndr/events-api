# Events API

[![CI](https://github.com/extndr/events-api/actions/workflows/ci.yml/badge.svg)](https://github.com/extndr/events-api/actions)
![Python](https://img.shields.io/badge/python-3.11+-blue)
![Docker](https://img.shields.io/badge/docker-ready-blue)

> Modular, containerized Django REST API for city-based event management with JWT authentication, role-based permissions, and flexible filtering.

## Features

- **Authentication & Security**: JWT login/registration, password reset, email verification, input validation, role-based access control (RBAC)
- **Event Management**: Create, read, update, delete events; track capacity and attendance.  
- **Clean Architecture**: Business logic separated into service layer for maintainability.  
- **API Documentation**: OpenAPI schema with interactive docs for easy testing.  
- **Testing & Quality**: pytest with factory-based fixtures, high coverage, code style enforcement (Black, Flake8).  

## Quick Start

Open your terminal and run the following commands **one at a time**:

```bash
git clone https://github.com/extndr/events-api.git
cd events-api
cp .env.example .env
docker-compose up --build -d
docker-compose exec web python manage.py load_initial_data
```

After that, open http://localhost:8000/api/docs/ to explore available endpoints.

## Project Purpose

This project is for practicing backend development with Django, JWT authentication, and containerization. It’s a personal playground for learning and experimenting.
