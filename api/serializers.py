from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from task.models import Task
from event.models import Event, event_participants
from matter.models import MatterAttorney, MatterInfo
from contact.models import cPerson
from base.models import CustomUser, CustomUserProfile
from django.contrib.auth.models import Group, User

class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = CustomUserProfile
        fields = '__all__'

    def to_representation(self, instance):
        rep = super(UserProfileSerializer, self).to_representation(instance)
        rep['user'] = "%s %s" % (
            instance.user.email, 
            instance.user.username, 
            ) 
        return rep


class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
    # def to_representation(self, instance):
    #     rep = super(UserSerializer, self).to_representation(instance)
    #     rep['user_type'] = instance.user_type.id
    #     return rep

class PersonContactLstSerializer(ModelSerializer):
    class Meta:
        model = cPerson
        fields = '__all__'

class EventSerializertb(ModelSerializer):
    # participant = serializers.SerializerMethodField()
    class Meta:
        model = Event
        fields = '__all__'

class EventSerializer(ModelSerializer):
    # participant = serializers.SerializerMethodField()
    class Meta:
        model = Event
        fields = '__all__'
        depth = 1
        

    # def get(self, obj):
    #     """obj is an Event instance. Returns list of dicts"""
    #     qset = event_participants.objects.filter(event=obj)
    #     return [EventParticipantSerializer(m).data  for m in qset]

class EventParticipantSerializer(ModelSerializer):
    class Meta:
        model = event_participants
        # fields = '__all__'       

class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class ClientSerializer(ModelSerializer):
    class Meta:
        model = cPerson
        fields = '__all__'

class MatterAttorneySerializer(ModelSerializer):
    class Meta:
        model = MatterAttorney
        fields = '__all__'

class PersonContactSerializer(ModelSerializer):
    contact = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = cPerson
        fields = ('last_name', 'first_name', 'matter_info')
    #   fields = '__all__'

class MatterInfo_oldSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='all-matters',
        # lookup_field='id'
    )
    client_contact = PersonContactSerializer(read_only=True)
    # client_contact = serializers.PrimaryKeyRelatedField(queryset=cPerson.objects.all(),
    #                                               many=False)

    class Meta:
        model = MatterInfo
        fields = '__all__'
        # fields = ['file_no', 'claim_no', 'title', 'updated', 'created', 'client_contact' ]

        
class MatterInfoSerializer(ModelSerializer):
    class Meta:
        model = MatterInfo
        fields = '__all__'

    def to_representation(self, instance):
        rep = super(MatterInfoSerializer, self).to_representation(instance)
        rep['client_contact'] = "%s %s %s" % (
            instance.client_contact.familyName, 
            instance.client_contact.firstName, 
            instance.client_contact.otherName
            ) 
        return rep




        # "id": 1,
        # "last_login": "2022-07-18T17:29:32.753941Z",
        # "is_superuser": true,
        # "is_staff": true,
        # "is_active": true,
        # "date_joined": "2022-07-17T19:09:02Z",
        # "username": "kesia",
        # "email": "kesia@mail.com",
        # "user_type": null,
        # "groups": [],
        # "user_permissions": []