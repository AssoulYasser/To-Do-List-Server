from django.db import models


class User(models.Model):
    username = models.CharField(max_length=15, primary_key=True)
    password = models.CharField(max_length=16)
    email = models.TextField()
    created = models.DateTimeField(auto_now_add=True)


class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=False, null=False)
    time = models.TimeField(auto_now_add=False)
    isDone = models.BooleanField(default=False)
