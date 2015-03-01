from django.db import models
from django.contrib.auth.models import User

class Session(models.Model):
    """Represents e.g a training session for which we want to register attendees"""

    date = models.DateField()
    description = models.CharField(max_length=100)

    # A user can attend many sessions, and a session can have many users attending
    attendees = models.ManyToManyField(User)

    def __str__(self):
        return "{0} - {1}".format(self.date, self.description)
