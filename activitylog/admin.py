from django.contrib import admin
from .models import Action, ActionMatter

# Register your models here.

@admin.register(Action)
class ActivitiesAdmin(admin.ModelAdmin):
    list_display = ('user', 'verb', 'target', 'created')
    list_filter = ('created',)
    search_fields = ('verb',)


@admin.register(ActionMatter)
class ActivitiesMatterAdmin(admin.ModelAdmin):
    list_display = ('user', 'verb', 'target', 'created')
    list_filter = ('created',)
    search_fields = ('verb',)