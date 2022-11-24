from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from .models import Task
from .forms import TaskForm

@login_required(login_url='login')
def dailyTask(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'task/task.html', context)

# def createTask(request):
#     form = TaskForm()
#     context = {'form' : form}
#     return render(request, 'task/add_task.html', context)
@login_required(login_url='login')
def CreateTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        # print(request.POST)
        if form.is_valid():
            form.save()
            
        # if request.POST.get('title') and request.POST.get('description'):
        # task = Task()
        # user = User.objects.get(id=pk)
        # task.host = user
        # task.title = request.POST.get('title')
        # task.description = request.POST.get('description')
        # task.status = request.POST.get('priority')            
        # task.save()
            
    #         return redirect('task')  
            return JsonResponse({'success': True}, safe=False)
        else:
            return JsonResponse({'success': False}, safe=False)

    return render(request,'task/task.html')



def taskModalPopup(request):
    # print("DONE")
    if  request.method == "GET":        
        task_id = request.GET['task_id']
        task= Task.objects.filter(id=task_id)
        taskserial = serializers.serialize('json', task)
        # print("DONE")
        return HttpResponse(taskserial, content_type="text/json-comment-filtered")
        # return JsonResponse(personserial, safe=False)
    return JsonResponse({'message':'error'})


def deleteTask(request):
    dkey = request.POST.get('dkey')
    task = Task.objects.get(id=dkey)

    # if request.user != room.host:
    #     return HttpResponse('Your are not allowed here!!')
    print(dkey)
    if request.method == 'POST':
        # print("DONE2")
        task.delete()
        message = [{'success': 'success'},
                    {'msg': 'ok'}]
        SerialMsg = list(message)
        return JsonResponse(SerialMsg, safe=False)
    return JsonResponse({'message':'error'})



@login_required(login_url='login')
def UpdateTask(request):
    # form = TaskForm(instance=task)
    if request.method == 'POST':
        # print(request.POST)
        idd = request.POST.get('id')
        # print(task_id)
        task = Task.objects.get(id=idd)
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()            
            
            return JsonResponse({'success': True}, safe=False)
            # return render(request, 'contact/')
        else:
            print(form.errors)
            return JsonResponse({'success': False}, safe=False)

    # context = {'task': task}
    return render(request, 'task/update_task.html')



def TaskDataAutoloader(request):
    # print('jfhfhfhfhfh')
    tasks = Task.objects.all()
    if request.method == 'GET':
        # if request.GET.get('page') == 'other_file_name':
        print(request.GET)
        host_id = request.GET.get('host')
        taskObj = Task.objects.filter(host_id=host_id)
        taskData = serializers.serialize('json', taskObj)
        return HttpResponse(taskData, content_type="text/json-comment-filtered")
    else:
        return JsonResponse({'success': False}, safe=False)

    context = {'tasks': tasks}
    print(context)
    return render(request, 'task/task.html', context)