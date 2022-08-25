from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Task

User = get_user_model()

admin.site.register(Task)