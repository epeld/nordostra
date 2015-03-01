from django.db import models
from django.contrib.auth.models import User

from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse


class AdminURLMixin(object):
    def get_admin_url(self):
        content_type = ContentType.objects.get_for_model(self.__class__)
        return reverse("admin:%s_%s_change" % ( content_type.app_label, content_type.model), args=(self.id,))

class Session(models.Model, AdminURLMixin):
    """Represents e.g a training session for which we want to register attendees"""

    date = models.DateField()
    description = models.CharField(max_length=100)

    # A user can attend many sessions, and a session can have many users attending
    attendees = models.ManyToManyField(User)

    def __str__(self):
        return "{0} - {1}".format(self.date, self.description)
