from django.urls import path
from . import views
# from .views import EventListJson

urlpatterns = [
    path('', views.Notification_Home, name="notice_home" ), 
    path('send-notification/', views.SendNotification, name="send_notification" ),

]
