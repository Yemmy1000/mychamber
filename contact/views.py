import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.utils.html import escape
from .forms import ContactPersonForm, ContactCompanyForm
from .models import cPerson, cCompany
from activitylog.utils import create_activity


@login_required(login_url='login')
def personContactPage(request):
    # tasks = Task.objects.all()
    # context = {'tasks': tasks}
    return render(request, 'contact/person-contact.html')

@login_required(login_url='login')
def companyContactPage(request):
    # tasks = Task.objects.all()
    # context = {'tasks': tasks}
    return render(request, 'contact/company-contact.html')

@login_required(login_url='login')
def CreatePersonContact(request):

    form = ContactPersonForm()

    if request.method == 'POST':
        # print(request.FILES)
        form = ContactPersonForm(request.POST, request.FILES)
       
        if form.is_valid():            
            contact = form.save(commit=False)
            contact.save()
            create_activity(request.user, 'contact created', contact)
            # return redirect('person-contact')
            # return render(request, 'contact/')
            return JsonResponse({'status': 'ok'})
        else:
            # print(form.errors)
            messages.error(request, 'An error occured! Contact not saved!')
            return JsonResponse({'status': 'error'})
            
            # print('form.errors')

    return render(request, 'contact/add_person.html', {'form': form})


@login_required(login_url='login')
def viewPersonContact(request, fk):
    # form = ContactPersonForm()
    person_contact = cPerson.objects.get(id=fk)
    context = {'person_contact': person_contact}

    return render(request, 'contact/view_person.html', context)


@login_required(login_url='login')
def updatePersonContact(request, fk):
    # form = ContactPersonForm()
    person_contact = cPerson.objects.get(id=fk)
    form = ContactPersonForm(instance=person_contact)
    pix = getattr(person_contact, 'personPix')

    if request.method == 'POST':
        form = ContactPersonForm(request.POST, request.FILES, instance=person_contact)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'ok'})
            # return redirect('person-contact')
            # return render(request, 'contact/')
        else:
            print(form.errors)
            messages.error(request, 'An error occured! Contact not updated!')
            return JsonResponse({'status': 'error'})

    context = {'form': form, 'id': fk, 'pix': pix}

    return render(request, 'contact/update_person.html', context)


@login_required(login_url='login')
def createCompanyContact(request, fk):
    form = ContactCompanyForm()

    if request.method == 'POST':
        form = ContactCompanyForm(request.POST, request.FILES)
        if form.is_valid():
            contact = form.save(commit=False)
            # user.username = user.username.lower()
            contact.save()
            # return redirect('contactPage')
            return render(request, 'contact/company-contact.html')
        else:
            messages.error(request, request.POST)

    return render(request, 'contact/add_company.html', {'form': form})



class PersonContactListJson(BaseDatatableView):
    # The model we're going to show
    model = cPerson

    # define the columns that will be returned
    columns = [ 'title', 'file_no', 'claim_no', 'nature', 'description', 'status',]  

    # define column names that will be used in sorting
    # order is important and should be same as order of columns
    # displayed by datatables. For non-sortable columns use empty
    # value like ''
    order_columns = [ 'personPix', 'firstName', 'familyName', 'homeAddress', 'firstPhone', 'sex',]

    # set max limit of records returned, this is used to protect our site if someone tries to attack our site
    # and make it return huge amount of data
    max_display_length = 500


    # def filter_queryset(self, qs):
    #     sSearch = self.request.GET.get('sSearch', None)
    #     if sSearch:
    #         qs = qs.filter(Q(firstName__istartswith=sSearch) | Q(familyName__istartswith=sSearch))
    #     return qs

def personContactPopup2(request):
    if  request.method == "GET":
        id = request.GET.get('rec_id')
        # person_contact = cPerson.objects.all().values()
        person_contact = cPerson.objects.filter(id=id)
        # context = {'datalist': person_contact}
        # personserial = list(person_contact)
        print(person_contact)
        personserial = serializers.serialize('json', person_contact)
        # json.dumps(personserial)
        # return JsonResponse(personserial, safe=False)
        return HttpResponse(personserial, content_type="text/json-comment-filtered")
    return JsonResponse({'message':'error'})


def personContactPopup(request):
    # print("DONE")
    if  request.method == "GET":        
        rec_id = request.GET['rec_id']
        person_contact= cPerson.objects.filter(id=rec_id)
        personserial = serializers.serialize('json', person_contact)
        return HttpResponse(personserial, content_type="text/json-comment-filtered")
        # return JsonResponse(personserial, safe=False)
    return JsonResponse({'message':'error'})


def deletePersonContact(request):
    dkey = request.POST.get('dkey')
    person_contact = cPerson.objects.get(id=dkey)

    # if request.user != room.host:
    #     return HttpResponse('Your are not allowed here!!')
    print(dkey)
    if request.method == 'POST':
        print("DONE2")
        person_contact.delete()
        message = [{'success': 'success'},
                    {'msg': 'ok'}]
        SerialMsg = list(message)
        return JsonResponse(SerialMsg, safe=False)
    return JsonResponse({'message':'error'})


def AllPersonContactList(request):
    # print("DONE")
    Person_contact = cPerson.objects.all()
    # if  request.method == "GET":        
    #     rec_id = request.GET['rec_id']
    #     person_contact= cPerson.objects.filter(id=rec_id)
    personserial = serializers.serialize('json', Person_contact)
    return HttpResponse(personserial, content_type="text/json-comment-filtered")
        # return JsonResponse(personserial, safe=False)
    # return JsonResponse({'message':'error'})