from django.shortcuts import render, redirect
from django.views.generic.base import TemplateResponseMixin, View
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.contrib import messages
from .models import ClaimantDocumentType, DefendantDocumentType
from .forms import CivilMatterForm, CriminalMatterForm, DefendantDocumentTypeForm, ClaimantDocumentTypeForm
from matter.models import CivilMatterSample, CriminalMatterSample, MatterInfo
from activitylog.models import Action, ActionMatter



def SettingsPage_old(request):
    form = SystemSettingsForm()
    context = {
        'form': form,
    }
    return render(request, 'systemsettings/shome.html', context)



@login_required(login_url='login')
def SettingsPage(request):
    return render(request, 'systemsettings/shome.html')


@login_required(login_url='login')
def CriminalMatterEntry(request):
    form = CriminalMatterForm()
    if request.method == 'POST' and request.POST.get('action') == 'editData':
        pk = request.POST.get('pk')
        civ_matter = CriminalMatterSample.objects.get(id=pk)
        form = CriminalMatterForm(request.POST, instance=civ_matter)
        # print("DONE2")
        form.save()
        return JsonResponse({'success': True}, safe=False)

    elif request.method == 'POST' and request.POST.get('action') == 'addData':
        form = CriminalMatterForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True}, safe=False)
            # return render(request, 'systemsettings/criminal_matter_entry.html', {'form':form})
            # return HttpResponse({'success': True}, content_type="text/json-comment-filtered")
        else:
            return JsonResponse({'success': False}, safe=False)

    return render(request, 'systemsettings/criminal_matter_entry.html', {'form':form})


@login_required(login_url='login')
def CivilMatterEntry(request):
    # civil_sample = CivilMatterSample.objects.all()
    # print(request.POST)
    form = CivilMatterForm()
    if request.method == 'POST' and request.POST.get('action') == 'editData':
        pk = request.POST.get('pk')
        civ_matter = CivilMatterSample.objects.get(id=pk)
        form = CivilMatterForm(request.POST, instance=civ_matter)
        # print("DONE2")
        form.save()
        return JsonResponse({'success': True}, safe=False)

    elif request.method == 'POST' and request.POST.get('action') == 'addData':
        form = CivilMatterForm(request.POST)
        if form.is_valid():
            # civil = form.save(commit=False)
            # user.username = user.username.lower()
            form.save()
            return JsonResponse({'success': True}, safe=False)
        else:
            return JsonResponse({'success': False}, safe=False)

    return render(request, 'systemsettings/civil_matter_entry.html', {'form':form})
    # return HttpResponse(matterAFData, content_type="text/json-comment-filtered")

def AutoLoaddata(request):    
    # form = CivilMatterForm()
    # print(request.GET)
    if request.method == 'GET':
        if request.GET.get('page') == 'civilPage':
            civil_sample = CivilMatterSample.objects.all()
            civilSample = serializers.serialize('json', civil_sample)
            # print(civilSample)
            return HttpResponse(civilSample, content_type="text/json-comment-filtered")

        elif request.GET.get('page') == 'criminalPage':
            cri_sample = CriminalMatterSample.objects.all()
            criminalSample = serializers.serialize('json', cri_sample)
            # print(civilSample)
            return HttpResponse(criminalSample, content_type="text/json-comment-filtered")

        elif request.GET.get('page') == 'claimant_doc_type':
            doc_samples = ClaimantDocumentType.objects.all()
            doc_sample_serialized = serializers.serialize('json', doc_samples)
            # print(civilSample)
            return HttpResponse(doc_sample_serialized, content_type="text/json-comment-filtered")

        elif request.GET.get('page') == 'defendant_doc_type':
            doc_samples = DefendantDocumentType.objects.all()
            doc_sample_serialized = serializers.serialize('json', doc_samples)
            # print(civilSample)
            return HttpResponse(doc_sample_serialized, content_type="text/json-comment-filtered")

    return JsonResponse({'failed': 'failed'}, safe=False)
    

def SampleModalPopup(request):
    print("DONE")
    if  request.method == "GET" and request.GET.get('page') == 'civilPage':        
        rec_id = request.GET['rec_id']
        sample_record= CivilMatterSample.objects.filter(id=rec_id)
        sampleSerial = serializers.serialize('json', sample_record)
        return HttpResponse(sampleSerial, content_type="text/json-comment-filtered")
        # return JsonResponse(personserial, safe=False)
    elif request.method == "GET" and request.GET.get('page') == 'criminalPage':        
        rec_id = request.GET['rec_id']
        sample_record= CriminalMatterSample.objects.filter(id=rec_id)
        sampleSerial = serializers.serialize('json', sample_record)
        return HttpResponse(sampleSerial, content_type="text/json-comment-filtered")

    elif request.method == "GET" and request.GET.get('page') == 'claimantDocType':        
        rec_id = request.GET['rec_id']
        sample_record= ClaimantDocumentType.objects.filter(id=rec_id)
        sampleSerial = serializers.serialize('json', sample_record)
        return HttpResponse(sampleSerial, content_type="text/json-comment-filtered")

    elif request.method == "GET" and request.GET.get('page') == 'defendantDocType':        
        rec_id = request.GET['rec_id']
        sample_record= DefendantDocumentType.objects.filter(id=rec_id)
        sampleSerial = serializers.serialize('json', sample_record)
        return HttpResponse(sampleSerial, content_type="text/json-comment-filtered")

    return JsonResponse({'message':'error'})


@login_required(login_url='login')
def ActivityLogView(request):
    # activities_others = Action.objects.exclude(user=request.user)
    activities = Action.objects.filter(user=request.user.id)
    matter_activities = ActionMatter.objects.filter(user=request.user.id)
    # following_ids = request.user.following.values_list('id', flat=True)
    # if following_ids:
        # If user is following others, retrieve only their actions
        # actions = actions.filter(user_id__in=following_ids)
        # actions = actions[:10]
    context = {
        'activities': activities,
        'matter_activs': matter_activities,
    }
    # print(list(activities))
    return render(request, 'systemsettings/activity_log.html', context)


def Matter_Detail(request, file_no):
    # matter = get_object_or_404(MatterInfo, file_no=file_no)

    matter = MatterInfo.objects.filter(file_no=file_no)

    return render(request,
                  'systemsettings/matter_detail.html',
                  {'matter': matter})


class FactDocumentClaimantCat(TemplateResponseMixin, View):
    form_class = ClaimantDocumentTypeForm
    template_name = 'systemsettings/claimant_doc_type.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        # print(request.POST)
        if request.POST.get('action') == 'addData':
            form = self.form_class(request.POST)
            if form.is_valid():
                form.save()
                return JsonResponse({'message': 'success'})
            # print(form.errors)
            else:
                return JsonResponse({'message': 'failed'}, safe=False)

        elif request.POST.get('action') == 'editData':            
            pk = request.POST.get('pk')
            sample = ClaimantDocumentType.objects.get(id=pk)
            form = self.form_class(request.POST, instance=sample)
            form.save()
            return JsonResponse({'message': 'success'})


class FactDocumentDefendantCat(TemplateResponseMixin, View):
    form_class = DefendantDocumentTypeForm
    template_name = 'systemsettings/defendant_doc_type.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        # print(request.POST)
        if request.POST.get('action') == 'addData':
            form = self.form_class(request.POST)
            if form.is_valid():
                form.save()
                return JsonResponse({'message': 'success'})
            # print(form.errors)
            else:
                return JsonResponse({'message': 'failed'}, safe=False)

        elif request.POST.get('action') == 'editData':            
            pk = request.POST.get('pk')
            sample = DefendantDocumentType.objects.get(id=pk)
            form = self.form_class(request.POST, instance=sample)
            form.save()
            return JsonResponse({'message': 'success'})