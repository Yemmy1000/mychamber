from django.urls import path
from . import views
# from .views import EventListJson

urlpatterns = [
    path('', views.eventPage, name="event" ), 
    # path('event-list/', EventListJson.as_view(), name='event_list_json'),
    # path('event-card/', views.eventCard, name="event-card" ), 
    # path('event-calendar/', views.eventCalendar, name="event-calendar" ), 
    path('create-event/', views.createEvent, name="create-event" ), 
    path('update-event/<id>', views.UpdateEvent, name="update-event" ),
    path('delete-event/<id>', views.DeleteEvent, name="delete-event" ),
    path('calendar-event/', views.CalendarEventData, name="calendar-data" ),
]
