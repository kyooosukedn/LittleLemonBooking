# Little Lemon Restaurant API

This is the API for the Little Lemon Restaurant booking system. It provides endpoints for menu management and table bookings.

## Setup Instructions

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Unix/MacOS: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Set up the MySQL database:
   - Create a database named `littlelemon`
   - Update database settings in `settings.py` if needed
6. Run migrations: `python manage.py migrate`
7. Create a superuser: `python manage.py createsuperuser`
8. Run the server: `python manage.py runserver`

## API Endpoints

### Authentication
- `POST /api/users/`: Register a new user
- `GET /api/auth/login/`: Login page
- `POST /api/auth/login/`: Login
- `GET /api/auth/logout/`: Logout

### Menu Items
- `GET /api/menu/`: List all menu items
- `POST /api/menu/`: Create a new menu item (auth required)
- `GET /api/menu/{id}/`: Get menu item details
- `PUT /api/menu/{id}/`: Update menu item (auth required)
- `DELETE /api/menu/{id}/`: Delete menu item (auth required)

### Bookings
- `GET /api/bookings/`: List all bookings (auth required)
- `POST /api/bookings/`: Create a new booking (auth required)
- `GET /api/bookings/{id}/`: Get booking details (auth required)
- `PUT /api/bookings/{id}/`: Update booking (auth required)
- `DELETE /api/bookings/{id}/`: Delete booking (auth required)
- `GET /api/bookings/my_bookings/`: List user's bookings (auth required)

## Testing

Run the tests using:
```bash
python manage.py test
```

## API Testing with Insomnia

1. Download and install Insomnia REST Client
2. Import the provided Insomnia collection
3. Create a new user using the registration endpoint
4. Login using the credentials
5. Use the token for authenticated requests

## Notes

- The API uses token-based authentication
- All booking-related endpoints require authentication
- Menu items can be viewed without authentication but require auth for modifications
