# Events API

A fully containerized Django REST API for managing city-based events with user authentication, location-aware filtering, and dynamic permissions.  
Designed to be extendable and production-ready — future enhancements like Celery-based email notifications and background tasks are easy to integrate.

## Key Features

- **User Authentication** — JWT-based login, registration, and password reset via email
- **Event Management** — Create, update, attend, and leave events with capacity limits
- **Role-Based Permissions** — Organizers can manage their events; users can join or leave
- **Geographic Filtering** — Filter events by country, city, or time window
- **Admin Interface** — Manage locations and users with Django Admin
- **API Documentation** — Auto-generated Swagger UI and Redoc
- **Test Coverage** — Pytest test suite with coverage reports
- **Dockerized** — Easy local setup with Docker Compose and PostgreSQL

## Tech Stack

- **Backend**: Python, Django, DRF
- **Databases**: SQLite for local, PostgreSQL for prod
- **Auth**: JWT via `djangorestframework-simplejwt`  
- **DevOps**: Docker, Docker Compose  
- **Docs**: Swagger UI, Redoc  
- **Testing**: Pytest, pytest-cov

## Project Goals

This project was built to demonstrate:

- Clean and scalable REST API design  
- Role-based access control and secure authentication  
- Geographic data modeling (countries, cities)  
- Docker-based local development  
- Maintainable code with auto-generated documentation and tests  

## Quick Start

```bash
git clone https://github.com/extndr/events-api.git
cd events-api
cp .env.example .env          # Configure environment
docker-compose up --build     # Start backend + PostgreSQL
```

Create an admin user to manage countries/cities:

```bash
docker exec -it django python manage.py createsuperuser
```

## API Access

- **Base URL**: `http://localhost:8000/api/`
- **Admin Panel**: `http://localhost:8000/admin/`
- **Swagger Docs**: `http://localhost:8000/api/swagger-ui/`
- **Redoc Docs**: `http://localhost:8000/api/redoc/`

## Authentication & Users

| Endpoint | Description |
|----------|-------------|
| `POST /accounts/token/` | Obtain JWT |
| `POST /accounts/token/refresh/` | Refresh token |
| `POST /accounts/register/` | Register user |
| `POST /accounts/reset-password/` | Request password reset |
| `POST /accounts/reset-password/confirm/?token=xyz` | Confirm password reset |
| `GET /users/me/` | Get my profile |
| `PUT /users/me/` | Update my profile |

## Events API

| Endpoint | Description |
|----------|-------------|
| `GET /events/` | List all events (supports filters) |
| `POST /events/` | Create new event (organizer only) |
| `GET /events/{id}/` | View event details |
| `PUT /events/{id}/` | Update event (organizer only) |
| `DELETE /events/{id}/` | Delete event (organizer only) |
| `POST /events/{id}/attend/` | Join event |
| `POST /events/{id}/unattend/` | Leave event |

## Filtering Examples

```http
GET /events/?country=UK
GET /events/?city=London
GET /events/?start_time=2025-05-26T00:00:00Z
GET /events/?end_time=2025-05-26T00:00:00Z
GET /events/?organizer=john_doe
```

## Development & Testing

**Run tests:**
```bash
pytest
pytest --cov=api   # With coverage report
```

**Django shell:**
```bash
docker exec -it web python manage.py shell
```

## Future Improvements

- Celery integration for async tasks (email reminders, cleanups)  
- Rate limiting & throttling  
- Timezone-aware event scheduling  
- Frontend (React/Vue) for UI testing and demos  
