from django.conf import settings
from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from base.models import CustomUser
from matter.models import MatterInfo
from base.widgets import DatePickerInput, TimePickerInput, DateTimePickerInput
from django.utils.timezone import now as timezone_now
# from django import forms

# Create your models here.


class Event(models.Model):
    TASK_CATEGORY = [
        ('Personal', 'Personal'),
        ('Official', 'Official'), 
        ('Business', 'Business'),
    ]
    TASK_PRIORITY = [
        ('Urgent', 'Urgent'),
        ('Important', 'Important'),
        ('Normal', 'Normal'),                       
    ]
    TASK_STATUS = [
        ('Closed', 'Closed'),
        ('Ongoing', 'Ongoing'), 
        ('Scheduled', 'Scheduled'),              
    ]
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="users_event_set")
    participant = models.ManyToManyField(CustomUser, blank=True, through='event_participants')
    matter = models.ForeignKey(MatterInfo, on_delete=models.CASCADE, null=True, related_name="matter_info")
    title = models.CharField('Title', max_length=200)
    category = models.CharField(
        'Category',
        max_length=12,
        choices=TASK_CATEGORY,
        default='Official',
        null=True, blank=True
    )
    
    priority = models.CharField(
        'Priority',
        max_length=12,
        choices=TASK_PRIORITY,
        default='Normal',
        null=True, blank=True
    )

    status = models.CharField(
        'Status',
        max_length=12,
        choices=TASK_STATUS,
        default='Scheduled',
        null=True, blank=True
    )
    # location: str = models.CharField('Location', null=True, blank=True, max_length=500)
    start = models.DateField('Start Date', null=True, blank=True)
    start_time = models.TimeField('Start Time', null=True, blank=True)
    end = models.DateField('End Date', null=True, blank=True)
    end_time = models.TimeField('End Time', null=True, blank=True)    
    description = models.TextField('Description', null=True, blank=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self) -> str:
        return f'{self.author} meets {self.participant}'

class event_participants(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="event_user")
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="user_event")

    


