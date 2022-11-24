from django.contrib.auth.models import User
from django.contrib.auth import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.db.models.signals import post_save
from notifications.signals import notify
from .models import CustomUser, CustomUserProfile
from event.models import Event


# @receiver(post_save, sender=CustomUser)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         CustomUserProfile.objects.create(user=instance)

# @receiver(post_save, sender=CustomUser)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()



# def my_handler(sender, instance, created, **kwargs):
#     notify.send(instance, verb='was saved')

# post_save.connect(my_handler, sender=Event)


# @receiver(user_logged_in)
# def user_signed_in(request, user, **kwargs):    
#   notify.send(user, recipient=user, verb=_("You signed in"))

# @receiver(user_logged_in)
# def user_signed_out(request, user, **kwargs):    
#   notify.send(user, recipient=user, verb=_("You signed out"))