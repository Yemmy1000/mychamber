from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import *
 
 
@receiver(post_save, sender=MatterDescription)
def update_UpdateLog(sender, instance, created, **kwargs):
    if created:
        UpdateLog.objects.create(user=instance)
  
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
        instance.profile.save()