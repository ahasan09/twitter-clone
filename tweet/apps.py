from django.apps import AppConfig


class TweetConfig(AppConfig):
    # Keep AutoField for this pre-Django-3.2 app so existing migrations
    # are not churned by the project-wide BigAutoField default.
    default_auto_field = 'django.db.models.AutoField'
    name = 'tweet'
