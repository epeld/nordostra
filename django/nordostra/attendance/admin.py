from django.contrib import admin
from attendance.models import Session

class SessionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Session)
