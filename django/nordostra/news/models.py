from django.db import models
from django.contrib.auth.models import User

class NewsItem(models.Model):
    """Represents a news entry"""

    author = models.ForeignKey(User)
    date = models.DateField()
    content = models.TextField()

