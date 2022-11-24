from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST
from common.decorators import ajax_required
from django.core import serializers
from django.db import connection
from django.contrib.auth.models import User
from base.models import CustomUser
from matter.models import MatterInfo
from .models import Event, event_participants
from .forms import EventForm
from activitylog.utils import create_activity

@login_required(login_url='login')
def eventPage(request):
    form = EventForm()
    return render(request, 'event/event.html', {'form': form})


@ajax_required
@require_POST
@login_required(login_url='login')
def createEvent(request):
    form = EventForm()
    
    if request.method == 'POST':        
        form = EventForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            # participant = request.POST.getlist('participant[]')
            data.save()

            participants = request.POST.getlist('participant[]')
            for participant in participants:
                if CustomUser.objects.filter(id=participant).exists():
                    parti = CustomUser.objects.get(id=participant)
                    data.participant.add(parti)

        return JsonResponse({'status': 'ok'})
        # print("goooo")
    else:
        
        return JsonResponse({'status': 'error'})
            # messages.error(request, 'An error occured! Event not saved!')
    return render(request, 'event/event.html', {'form': form})

     
    
     
     

@login_required(login_url='login')
def UpdateEvent(request, id):
    # form = TaskForm(instance=task)
    if request.method == 'POST':
        # print(request.POST)
        # event_id = request.POST.get('id')
        # print(event_id)
        event = Event.objects.get(id=id)
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()            
            
            return JsonResponse({'success': True}, safe=False)
            # return render(request, 'contact/')
        else:
            # print(form.errors)
            return JsonResponse({'success': False}, safe=False)

    # context = {'task': task}
    # return render(request, 'task/update_task.html')    

def DeleteEvent(request, id):
    # dkey = request.POST.get('dkey')
    event = Event.objects.get(id=id)

    # if request.user != room.host:
    #     return HttpResponse('Your are not allowed here!!')
    # print(dkey)
    if request.method == 'POST':
        # print("DONE2")
        event.delete()
        message = [{'success': 'success'},
                    {'msg': 'ok'}]
        SerialMsg = list(message)
        return JsonResponse(SerialMsg, safe=False)
    return JsonResponse({'message':'error'})


def CalendarEventData(request):

    if request.method == 'GET':
        # if request.GET.get('page') == 'other_file_name':
        # author = request.GET.get('author')
        # print(request.GET)
        # print(author)
        cursor = connection.cursor()
        cursor.execute('SELECT event_event.author_id, event_event.title\
            FROM event_event')
        cursor = connection.cursor()
        solution = cursor.fetchall()
        event = list(solution)


        # eventObj = Event.objects.filter(author=author)
        # eventData = list(eventObj)
        # eventData = serializers.serialize('json', eventObj)
        print(solution)
        
        return JsonResponse(event, safe=False)
        # return HttpResponse(eventData, content_type="text/json-comment-filtered")