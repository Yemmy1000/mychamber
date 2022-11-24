import datetime
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from .models import Action, ActionMatter

def create_activity(user, verb, target=None):
    # check for any similar activitie made in the last minute
    now = timezone.now()
    last_minute = now - datetime.timedelta(seconds=60)
    similar_activities = Action.objects.filter(user_id=user.id, verb= verb, created__gte=last_minute)
    
    if target:
        target_ct = ContentType.objects.get_for_model(target)
        similar_activities = similar_activities.filter(target_ct=target_ct, target_id=target.id)
    
    if not similar_activities:
        # no existing activities found
        action = Action(user=user, verb=verb, target=target)
        action.save()
        return True

    return False



def create_matter_activity(user, verb, target=None):
    # check for any similar activitie made in the last minute
    now = timezone.now()
    last_minute = now - datetime.timedelta(seconds=60)
    similar_activities = ActionMatter.objects.filter(user_id=user.id, verb= verb, created__gte=last_minute)
    
    if target:
        target_ct = ContentType.objects.get_for_model(target)
        similar_activities = similar_activities.filter(target_ct=target_ct, target_id=target.file_no)
    
    if not similar_activities:
        # no existing activities found
        action = ActionMatter(user=user, verb=verb, target=target)
        action.save()
        return True

    return False

