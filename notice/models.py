from django.db import models
from notifications.base.models import AbstractNotification


# class Notification(AbstractNotification):
#     # custom field example
#     category = models.ForeignKey('myapp.Category', on_delete=models.CASCADE)

#     class Meta(AbstractNotification.Meta):
#         abstract = False