from django.db.models.signals import post_save
from notifications.signals import notify
from django.dispatch import Signal

from task.models import Task

notify = Signal()
# def my_handler(sender, instance, created, **kwargs):
#     notify.send(instance, verb='was saved')

# post_save.connect(my_handler, sender=Task)