# Events API

[![CI](https://github.com/extndr/events-api/actions/workflows/ci.yml/badge.svg)](https://github.com/extndr/events-api/actions)
![Python](https://img.shields.io/badge/python-3.12+-blue)
![Docker](https://img.shields.io/badge/docker-ready-blue)

> Modular, containerized Django REST API for city-based event management with JWT authentication, role-based permissions, and flexible filtering.

## Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Quick Start](#-quick-start)
- [Roadmap](#-technical-roadmap)
- [Project Purpose](#-project-purpose)
- [Contact](#-contact)

## 🚀 Features

- **Authentication:** JWT-based login/registration with secure password reset workflows
- **Event Management:** CRUD operations with capacity tracking and attendance management
- **Permissions:** Role-based access control (organizers manage events, users join/leave)
- **Service Layer:** Clean business logic separation with dedicated service classes
- **API Documentation:** Auto-generated OpenAPI 3.0 docs via drf-spectacular
- **Security:** Short-lived JWT tokens, input validation, email verification
- **Testing:** 90%+ coverage with pytest-django and factory pattern
- **CI:** GitHub Actions pipeline with automated testing and linting

## 🛠 Tech Stack

- **Backend:** Django 5.2, DRF, PostgreSQL
- **Authentication:** JWT tokens with secure email workflows
- **Architecture:** Service layer pattern, clean separation of concerns
- **Testing:** pytest-django, factory-based fixtures, 90%+ coverage
- **Quality:** Black, Flake8, GitHub Actions
- **Infrastructure:** Docker, Docker Compose

## 📘 API Documentation

- OpenAPI schema: [localhost:8000/api/schema/](http://localhost:8000/api/schema/)
- Interactive docs: [localhost:8000/api/docs/](http://localhost:8000/api/docs/)

## ⚡ Quick Start

```bash
git clone https://github.com/extndr/events-api.git
cd events-api
cp .env.example .env
docker-compose up --build -d
docker-compose exec web python manage.py load_initial_data

# Create superuser for full access to API endpoints
docker-compose exec web python manage.py createsuperuser
```

## 🚀 Technical Roadmap

- [ ] Basic React frontend for API consumption and user interaction
- [ ] AWS ECS deployment with Terraform infrastructure-as-code
- [ ] Background task processing with Celery for email notifications

## 📝 Project Purpose

This project is under active development in my free time to demonstrate backend skills with Django, containerization, JWT authentication, real-world email integration, and automated API docs — production-ready and extensible.

## 📧 Contact
**📧** bogdanzaharchenko7@gmail.com **🔗** [GitHub](https://github.com/extndr)
