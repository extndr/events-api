
# Events API

A production-ready, fully containerized Django REST API for managing city-based events.

---

## Tech Stack

- Django 5.2
- Django REST Framework 3.16.0
- djangorestframework-simplejwt 5.5.0 (JWT authentication)
- drf-spectacular 0.28.0 (OpenAPI/Swagger schema generation)
- django-filter 25.1 (advanced filtering)
- django-sendgrid-v5 1.3.0 (SendGrid email integration)
- psycopg2-binary 2.9.10 (PostgreSQL adapter)
- whitenoise 6.9.0 (static files handling)
- gunicorn 23.0.0 (production WSGI server)
- pytest-django 4.11.1 (testing)
- django-environ 0.12.0 (environment variables management)
- flake8 7.2.0 (code style checking)

---

## Key Features

- User authentication: JWT-based login, registration, and password reset via email  
- Event management: create, update, attend, and leave events with capacity limits  
- Role-based permissions: organizers manage their own events, users can join or leave  
- Advanced filtering: filter events by country, city, organizer, etc.  
- Django Admin interface for managing users and locations  
- API documentation generated with drf-spectacular, available locally (Swagger / Redoc)  
- Email handling: MailHog for local development, SendGrid in production  

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/extndr/events-api.git
cd events-api
```

### 2. Environment configuration

Prepare environment variable files:

- `.env.local` — for local development  
- `.env.prod` — for production  

Example `.env.local`:

```ini
DJANGO_ENV=local
SECRET_KEY=your-secret-key

EMAIL_HOST=mailhog
EMAIL_PORT=1025
DEFAULT_FROM_EMAIL=dev@example.com
```

Example `.env.prod`:

```ini
DJANGO_ENV=prod
SECRET_KEY=your-prod-secret-key

ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com

DATABASE_URL=postgres://postgres:your-secure-db-password@db:5432/postgres

POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your-secure-db-password

SENDGRID_API_KEY=your-sendgrid-api-key
DEFAULT_FROM_EMAIL=no-reply@yourdomain.com
```

---

### 3. Running the project

Run using Docker Compose with the appropriate profile:

- Local development (includes MailHog):

```bash
docker-compose --profile=local up --build
```

- Production (Gunicorn server, SendGrid, PostgreSQL):

```bash
docker-compose --profile=prod up --build
```

---

### 4. Email testing

- Local environment uses MailHog for capturing emails at: [http://localhost:8025](http://localhost:8025)  
- Production environment sends emails through SendGrid  

---

### 5. Running tests

Run tests inside the Django container:

```bash
docker-compose exec web pytest
```

---

## API Documentation

Available only in the local environment:

- Swagger UI: [http://localhost:8000/api/docs/](http://localhost:8000/api/docs/)  
- Redoc: [http://localhost:8000/api/docs/redoc/](http://localhost:8000/api/docs/redoc/)  

---

## Future improvements

- Tracking event attendance details (status, joined_at, left_at)  
- Background tasks with Celery (email notifications, event reminders)  
- Frontend integration for event discovery and interaction  
- Enhanced filtering and recommendation system  

---

## Project purpose

This project demonstrates solid backend development skills with Django, including containerization, JWT authentication, real-world email service integration, and automated API documentation — ready for production environments.

---

