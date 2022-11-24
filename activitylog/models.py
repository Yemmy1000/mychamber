from django.conf import settings
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Action(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='activities', db_index=True, on_delete=models.CASCADE)
    verb = models.CharField(max_length=255)
    target_ct = models.ForeignKey(ContentType, blank=True, null=True, related_name='target_obj', on_delete=models.CASCADE)
    target_id = models.PositiveIntegerField(null=True, blank=True,db_index=True)
    target = GenericForeignKey('target_ct', 'target_id')

    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created',)


class ActionMatter(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='matter_activities', db_index=True, on_delete=models.CASCADE)
    verb = models.CharField(max_length=255)
    target_ct = models.ForeignKey(ContentType, blank=True, null=True, related_name='matter_target_obj', on_delete=models.CASCADE)
    target_id = models.CharField(null=True,  max_length=200, blank=True, db_index=True)
    target = GenericForeignKey('target_ct', 'target_id')

    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created',)