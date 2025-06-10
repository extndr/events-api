# Events API

A fully containerized Django REST API for managing city-based events.  
Designed to be extendable and production-ready - future enhancements are easy to integrate.

## Tech Stack

- Django==5.2
- django-filter==25.1
- djangorestframework==3.16.0
- djangorestframework-simplejwt==5.5.0
- drf-spectacular==0.28.0
- python-decouple==3.8
- pytest-django==4.11.1
- psycopg2-binary==2.9.10
- whitenoise==6.9.0

## Key Features

- **User Authentication** - JWT-based login, registration, and **password reset via email**
- **Event Management** - Create, update, attend, and leave events with capacity limits
- **Role-Based Permissions** - Organizers can manage their events; users can join or leave  
- **Advanced Filtering** - Filter events by country, city, organizer, etc.
- **Admin interface** - Manage locations and users with Django Admin

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/extndr/events-api.git
   cd events-api
   ```

2. **Configure environment variables**  
   Create a `.env` file in the root directory:
   ```env
   
      # Django environment: 'local' for development, 'prod' for production
      DJANGO_ENV=local

      # Django secret key
      SECRET_KEY=your-secret-key

      # Database settings (production)
      DB_NAME=postgres
      DB_USER=postgres
      DB_PASSWORD=your-db-password
      DB_HOST=db
      DB_PORT=5432

      # Email settings
      EMAIL_HOST_USER=your_email@example.com
      EMAIL_HOST_PASSWORD=your_secure_app_password
      DEFAULT_FROM_EMAIL=${EMAIL_HOST_USER}

   ```

## Running the Project

```bash
docker-compose up --build
```

## API Documentation

- **Swagger UI**: [http://localhost:8000/api/docs/](http://localhost:8000/api/docs/)  
- **Redoc**: [http://localhost:8000/api/docs/redoc/](http://localhost:8000/api/docs/redoc/)

**Note:** documentation is only available in the `local` environment, not in `prod`.

## Testing

```bash
docker exec -it django pytest
```

## Future plans (what should be added)

- Event attendance (recording user participation: `status`, `joined_at`, `left_at`, etc.)  
- Upcoming events
- Celery for background tasks (e.g. email notifications, event reminders)  
- Frontend integration (event discovery, participation, and interaction)

---
