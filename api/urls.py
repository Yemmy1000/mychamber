from django.urls import path
from . import views
from .views import getAllEvent, getEventDetail, getAllMatter, getAMatter, getUsers, getUserProfile, \
    getPersonContactList, getUserTasks, getAllCurrentEvents
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    path('', views.getRoutes),
    path('users/<int:id>/profile/', getUserProfile.as_view(), name='all-user-profile'),
    path('users/', getUsers.as_view(), name='all-users'),
    path('person-contact-list/', getPersonContactList.as_view(), name='person-contact-list'),
    path('tasks/', views.getTasks),
    path('tasks/<int:hostid>', getUserTasks.as_view(), name='user-tasks'),
    # path('events/<int:pk>', views.getEvent),
    # path('events/', views.getAllEvent),
    path('events/', getAllEvent.as_view(), name='events'),
    # path('current-events/', getAllCurrentEvents.as_view(), name='current-events'),
    path('events/<int:pk>', getEventDetail.as_view(), name='event-detail'),

    path('matters/', getAllMatter.as_view(), name='all-matters'),
    path('matters/<pk>', getAMatter.as_view(), name='user-matter'),
    # path('notifications/<int:receiver>', getNotifications.as_view(), name='notif'),
]


