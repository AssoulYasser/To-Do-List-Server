from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=15, primary_key=True)
    password = models.TextField()
    email = models.TextField()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []


class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=False, null=False)
    time = models.TimeField(auto_now_add=False)
    isDone = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
