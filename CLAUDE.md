# Twitter Clone

Django 4.2 LTS Twitter clone with tweet posting, user following/followers, and notifications.

## Tech Stack
- Python 3.10+
- Django 4.2 LTS
- SQLite (default) or PostgreSQL
- HTML / Django Templates

## Project Structure
```
twitterclone/
├── tweets/
│   ├── models.py       # Tweet model
│   └── views.py
├── accounts/           # User auth, follow/unfollow
├── notifications/
├── templates/
└── manage.py
```

## Development
```bash
# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run development server
python manage.py runserver
```

## Key Notes
- Create a superuser with `python manage.py createsuperuser`.
