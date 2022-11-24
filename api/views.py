import datetime
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from task.models import Task
from event.models import Event, event_participants
from matter.models import MatterInfo, MatterAttorney
from base.models import CustomUser, CustomUserProfile
from contact.models import cPerson
from .serializers import TaskSerializer, EventSerializer, MatterAttorneySerializer, MatterInfoSerializer, UserProfileSerializer, \
    UserSerializer, PersonContactLstSerializer, EventParticipantSerializer, EventSerializertb
from django.shortcuts import get_object_or_404
from django.core import serializers
from django.http import HttpResponse, JsonResponse


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/users',
        'GET /api/user/:id',
        'GET /api/users/:id/profile',   
        'GET /api/person-contact-list',     
        'GET /api/tasks',
        'GET /api/task/:host',
        'GET /api/matters',
        'GET /api/matter/:id',
        'GET /api/persons',
        'GET /api/person/:id',
        'GET /api/events',
        'GET /api/events/:id',
        # 'GET /api/event/:id',
    ]
    return Response(routes)

@api_view(['GET'])
def getTasks(request):
    tasks = Task.objects.all()   
    taskSerializer = TaskSerializer(tasks, many=True) 
    return Response(taskSerializer.data)

@api_view(['GET'])
def getTask_old(request, pk):
    task = Task.objects.get(id=pk)   
    taskSerializer = TaskSerializer(task, many=False) 
    return Response(taskSerializer.data)

class getUsers(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class getUserProfile_old(generics.ListCreateAPIView):
    queryset = CustomUserProfile.objects.all()
    serializer_class = UserProfileSerializer

class getUserTasks(generics.ListCreateAPIView):
    # queryset = Task.objects.all()
    # serializer_class = TaskSerializer
    def get_queryset(self):
        queryset = Task.objects.filter(host_id=self.kwargs["hostid"])
        return queryset
    serializer_class = TaskSerializer

class getUserProfile(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = CustomUserProfile.objects.filter(user=self.kwargs["id"])
        return queryset
    serializer_class = UserProfileSerializer

class getPersonContactList(generics.ListCreateAPIView):
    queryset = cPerson.objects.all()
    serializer_class = PersonContactLstSerializer

# @api_view(['GET'])
class getAllEvent_old(APIView):
    def get(self, request):
        # print(request.GET)
        my_event = Event.objects.all()
        event = EventSerializer(my_event, many=True)
        return Response(event.data)

# class getAllMatter_old(APIView):
#     def get(self, request):
#         matter_e = MatterInfo.objects.select_related('client_contact').all()
#         matter = MatterInfoSerializer(matter_e, many=True)
#         return Response(matter.data)

class getAllEvent(generics.ListCreateAPIView):   
    # ids = Event.objects.values('participant').distinct()
    # print(ids)
    queryset = Event.objects.all()
    serializer_class = EventSerializertb


class getAllCurrentEvents(generics.ListCreateAPIView):  
    def get_queryset(self):
        queryset = Event.objects.filter(start__gt=datetime.datetime.today())
        return queryset
    serializer_class = EventSerializer


def getAllCurrentEvents_old(request):
    events = Event.objects.all()   
    events = Maca.objects.filter(start__contains > datetime.today())
    taskSerializer = TaskSerializer(tasks, many=True) 
    return Response(taskSerializer.data)

# @api_view(['GET'])
class getEventDetail(generics.RetrieveDestroyAPIView):
    queryset = Event.objects.all()
    # queryset = event_participants.objects.filter(Event)
    # queryset_1 = EventParticipantSerializer(event_participants)
    # queryset = Event.objects.filter(id__in=queryset_1).prefetch_related('event__participants')
    # queryset = Event.objects.select_related('participant').all()
    serializer_class = EventSerializer

class getAllMatter(generics.ListCreateAPIView):
    queryset = MatterInfo.objects.select_related('client_contact').all()
    # queryset = MatterInfo.objects.select_related('client_contact').values('pk', 'file_no', 'title', 'author', 'author_id', 'claim_no','client_contact')
    serializer_class = MatterInfoSerializer

class getAMatter(generics.RetrieveDestroyAPIView):
    queryset = MatterInfo.objects.all()
    serializer_class = MatterInfoSerializer
    # def get_queryset(self):
    #     queryset = MatterInfo.objects.filter(file_no=self.kwargs["file_no"])
    #     return queryset
    # serializer_class = MatterInfoSerializer

class getNotifications(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = CustomUserProfile.objects.filter(user=self.kwargs["id"])
        return queryset
    serializer_class = UserProfileSerializer


def getTimeDifference(t):
    # datetime(year, month, day, hour, minute, second)
    now  = datetime.now() 
    later = datetime.datetime(t)
    # b = datetime.datetime(2017, 5, 16, 8, 21, 10)
    c = later - now
    # if c
    return c

