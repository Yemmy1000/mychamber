from django.shortcuts import render
from base.models import CustomUser
from django.views.generic import ListView
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST
from common.decorators import ajax_required
from django.contrib.auth.decorators import login_required
from notifications.signals import notify

# Create your views here.

def Notification_Home(request):
    users = CustomUser.objects.all()
    # print(users)
    return render(request, 'notice/index.html', {'users': users})

@ajax_required
@require_POST
@login_required
def SendNotification(request):
    if request.method == "POST":
        # print(request.POST.get("recipient[]"))
        # sender = request.POST.get("sender") 
        recipient = CustomUser.objects.get(id=request.POST.get("recipient[]"))
        # recipient = request.POST.get("recipient[]") 
        verb = request.POST.get("topic")
        level = request.POST.get("level")
        description = request.POST.get("description")
        notify.send(request.user, recipient=recipient, verb=verb, level=level, description=description)
    return JsonResponse({'status': 'ok'})

# class SendNotification(ListView):
#     model = Publisher
#     context_object_name = 'my_favorite_publishers'


# notify.send(actor, recipient, verb, action_object, target, level, description, public, timestamp, **kwargs)

# actor: An object of any type. (Required) Note: Use sender instead of actor if you intend to use keyword arguments
# recipient: A Group or a User QuerySet or a list of User. (Required)
# verb: An string. (Required) e.g. 'you reached level 10'
# action_object: An object of any type. (Optional)
# target: An object of any type. (Optional)
# level: One of Notification.LEVELS ('success', 'info', 'warning', 'error') (default=info). (Optional)
# description: An string. (Optional)
# public: An boolean (default=True). (Optional)
# timestamp: An tzinfo (default=timezone.now()). (Optional)