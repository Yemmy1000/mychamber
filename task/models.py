from django.db import models
# from django.contrib.auth.models import User
from base.models import CustomUser
# from django import forms

# Create your models here.
# User = settings.AUTH_USER_MODE


class Task(models.Model):
    TASK_PRIORITY = [
        ('Urgent', 'Urgent'),
        ('Important', 'Important'), 
        ('Normal', 'Normal'),              
    ]
    host = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    title: str = models.CharField(max_length=200)
    description = models.TextField(null=False, blank=True)
    status = models.CharField(
        max_length=12,
        choices=TASK_PRIORITY,
    )
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self) -> str:
        return self.title
