from django.apps import AppConfig
from django.db.utils import OperationalError, ProgrammingError
from apps.articles.models import Post
from django.contrib.auth import get_user_model
from django.utils.timezone import now

class ArticlesConfig(AppConfig):
    name = 'articles'

    def ready(self):
        try:
            User = get_user_model()

            # Check if any posts exist; if not, create sample data
            if not Post.objects.exists():
                author, created = User.objects.get_or_create(
                    username='sample_author', defaults={'email': 'author@example.com'}
                )
                Post.objects.create(
                    author=author,
                    title='Welcome to the Blog',
                    text='This is a sample blog post automatically created on startup.',
                    created_date=now(),
                    published_date=now(),
                )
                Post.objects.create(
                    author=author,
                    title='Getting Started',
                    text='Learn how to use our blogging platform effectively.',
                    created_date=now(),
                )
        except (OperationalError, ProgrammingError):
            print("Something went wrong")
            pass

from django.contrib.auth import get_user_model
from apps.articles.models import Post
from django.utils.timezone import now

User = get_user_model()
author, created = User.objects.get_or_create(
    username='sample_author', defaults={'email': 'author@example.com'}
)
Post.objects.create(
    author=author,
    title='Test Post',
    text='This is a test post.',
    created_date=now(),
    published_date=now(),
)