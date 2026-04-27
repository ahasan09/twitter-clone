# Improvement Plan: twitterclone

## Overview
Django 3 Twitter clone with tweets, follows, and notifications. Likely uses Django 3.x (EOL), has no tests, no REST/GraphQL API, and limited security hardening.

## Improvements

### Security (High Priority)
- Ensure `SECRET_KEY` is loaded from environment variables and not committed to the repo — rotate if it has been committed
- Enable `DEBUG=False` in any staging/production environment and set `ALLOWED_HOSTS`
- Add CSRF protection verification (Django has it by default, but ensure it's not disabled anywhere)
- Add rate limiting on tweet posting to prevent spam

### Modernization
- Upgrade from Django 3 to Django 5.x (LTS) — Django 3.x reached EOL in April 2024
- Add a REST API layer using Django REST Framework to enable a future frontend SPA or mobile app
- Add `django-environ` for environment variable management

### Testing
- Add pytest + `pytest-django` tests for all views (tweet CRUD, follow/unfollow, notifications)
- Add factory_boy fixtures for test data
- Add GitHub Actions CI to run tests on every PR
- Target ≥80% coverage

### Features
- Add retweet and quote-tweet functionality
- Add hashtag support with a trending topics page
- Add image/media attachment to tweets
- Add direct messaging
- Add tweet likes (not just follows)
- Add infinite scroll for the timeline feed

### Code Quality
- Add `black` + `ruff` for formatting and linting
- Add proper pagination to the timeline query (currently may load all tweets)

### DevOps
- Add a `Dockerfile` and `docker-compose.yml` (app + PostgreSQL + Redis for notifications)
- Switch from SQLite to PostgreSQL
- Add GitHub Actions CI: lint + test + build Docker image
