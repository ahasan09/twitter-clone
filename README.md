# Twitter Clone

A Django web application that replicates core Twitter functionality — user authentication, posting tweets, following other users, and a personalized home feed.

## Features

- User registration, login, and logout
- Compose and post tweets
- Follow and unfollow other users
- Personalized home feed showing tweets from followed users
- User profile pages
- Notifications

## Tech Stack

- [Django](https://www.djangoproject.com/) 3.x — web framework
- Python 3.8+
- SQLite (default) — database
- Django Templates — server-side rendering
- [Poetry](https://python-poetry.org/) — dependency management

## Prerequisites

- [Python](https://www.python.org/) 3.8+
- [Poetry](https://python-poetry.org/): `pip install poetry`

## Getting Started

### 1. Install dependencies

```bash
git clone https://github.com/ahasan09/twitter-clone
cd twitter-clone
poetry install
```

### 2. Apply database migrations

```bash
poetry run python manage.py migrate
```

### 3. Create a superuser (optional)

```bash
poetry run python manage.py createsuperuser
```

### 4. Run the development server

```bash
poetry run python manage.py runserver
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

## Alternative: pip install

If you don't use Poetry:

```bash
pip install django
python manage.py migrate
python manage.py runserver
```

## Project Structure

```
twitter-clone/
├── twitterclone/    # Project settings and URL config
├── twitteruser/     # User model, auth, profile
├── tweet/           # Tweet model, views, forms
├── authentication/  # Login/register/logout views
├── notification/    # Notification system
└── manage.py
```

## Admin Panel

Access the Django admin at [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) using your superuser credentials.
