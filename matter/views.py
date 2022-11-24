import os
from django.http import HttpResponse, JsonResponse
from django.utils.timezone import now as timezone_now
from django.utils.html import escape
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic.base import TemplateResponseMixin, View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from base.models import CustomUser, CustomUserProfile
from contact.models import cPerson
from .models import *
from .forms import *
from django_datatables_view.base_datatable_view import BaseDatatableView
import json
from django.core import serializers
from django.db import connection
from django.forms import modelform_factory
from activitylog.utils import create_activity, create_matter_activity

from django.views.generic.detail import SingleObjectTemplateResponseMixin
from django.views.generic.edit import ModelFormMixin, ProcessFormView

def MatterPage(request):
    return render(request, 'matter/matter.html')

def addMatter(request):
    return render(request, 'matter/add_matter.html')

class MatterListJson(BaseDatatableView):
    model = MatterInfo
    columns = [ 'file_no', 'client_contact', 'created', 'updated', ]
    order_columns = [ 'file_no', 'client_contact', 'created', 'updated', ]

    # max_display_length = 500

def MatterListJson_2(request):
    matters = MatterClient.objects.all().values('file_no')  # or simply .values() to get all fields
    personserial = serializers.serialize('json', matters)
    return HttpResponse(personserial, content_type="text/json-comment-filtered")

class MatterInfoView(TemplateResponseMixin, View):
    form_class = MatterInfoForm
    model = MatterInfo
    template_name = 'matter/matter_info.html'
    context_object_name = 'matter_info'  
    # queryset = MatterInfo.objects.get(file_no=file_no)

    def get(self, request):
        form = self.form_class()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        file_no = request.POST.get('file_no')
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            form.save()
            request.session['file_no'] = file_no
            # create_matter_activity(request.user, 'created matter', self.get_queryset(file_no))
            return redirect('matter-update', file_no=file_no)

        context = {'form': form}
        return render(request, self.template_name, context)


class UpdateMatterInfoView_old(UpdateView):
    # queryset = MatterInfo.objects
    def get_object(self, file_no, queryset=None):
        return self.model.objects.filter(file_no=file_no)


class UpdateMatterInfoView_old(MatterInfoView, UpdateView):
    form_class = MatterInfoForm
    model = MatterInfo
    template_name = 'matterupdate/update_basic_information.html'
    context_object_name = 'update-matter-info'
    form = None  
    sample = None
    # queryset = MatterInfo.objects.get(file_no=file_no)

    def get(self, request, file_no):
        self.sample = self.model.objects.get(file_no=file_no)
        self.form = self.form_class(instance=self.sample)
        # form = self.form_class()
        context = {'form': self.form}
        return render(request, self.template_name, context)

    def post(self, request, file_no):
        print(request)
        # file_no = request.POST.get('file_no')
        self.form = self.form_class(request.POST, instance=self.sample)
        if self.form.is_valid():
            self.form.save()
        return redirect(request, 'matterupdate/matter-update.html', file_no=file_no)

class UpdateMatterInfoView(UpdateView):
    # specify the model you want to use
    model = MatterInfo
    form_class = MatterInfoForm
    template_name = 'matterupdate/update_basic_information.html' 

    def get_success_url(self):
        return reverse('matter-update', kwargs={'file_no': self.object.file_no})




@login_required(login_url='login')
def CreateMatterInfo(request):
    form = MatterInfoForm()

    if request.method == 'POST':
        file_no = request.POST.get('file_no')
        try:
            matterInfo = MatterInfo.objects.get(file_no=file_no)
        except:
            print("Something went wrong")
            # Do somethng good
            form = MatterInfoForm(request.POST)
            if form.is_valid():
                contact = form.save(commit=False)
                # file_no = request.POST.get('file_no') 
                contact.save()
                request.session['file_no'] = file_no
                matterInfo = MatterInfo.objects.get(file_no=file_no)
                others=initialOtherMatterModels(matterInfo)
                create_matter_activity(request.user, 'created matter', matterInfo)
                return redirect('create-matter-attorney', file_no=file_no)
            # return render(request, 'matter/matter_info.html', {'file_no': file_no} )
            else:
                messages.error(request, 'An error occured! Matter not saved!')            
        else:
            print("Nothing went wrong")
            

            form = MatterInfoForm(request.POST, instance=matterInfo)
            if form.is_valid():
                form.save()
                create_matter_activity(request.user, 'created matter', matterInfo)
                # return redirect('person-contact')
                # if request.session['file_no'] is None or request.session['file_no'] is not file_no:
                request.session['file_no'] = file_no
            
                others=initialOtherMatterModels(matterInfo)
                return redirect('create-matter-attorney', file_no=file_no)
            else:
                messages.error(request, 'An error occured! Matter not saved!')          

    return render(request, 'matter/matter_info.html', {'form': form})


def initialOtherMatterModels(file_no):
    MatterAttorney.objects.create(file_no = file_no)
    # MatterConflictOtherParty.objects.create(file_no = file_no)
    MatterConflictAdverseParty.objects.create(file_no = file_no)
    # MatterConflictAssocFile.objects.create(file_no = file_no)
    # MatterDocument.objects.create(file_no = file_no)
    # MatterCivilNature.objects.create(file_no = file_no)
    # MatterCriminalNature.objects.create(file_no = file_no)
    # MatterDescription.objects.create(file_no = file_no)    

    return True  



@login_required(login_url='login')
def createMatterAttorney(request, file_no):
    form = MatterAttorneyForm()

    if request.method == 'POST':
        if request.session['file_no'] == request.POST.get('file_no') == file_no:
            file_no = request.session['file_no']             
            try:
                matterInfo = MatterAttorney.objects.get(file_no=file_no)
            except:
                print("Something went wrong")
                # Do somethng good
                form = MatterAttorneyForm(request.POST)
                if form.is_valid():
                    contact = form.save(commit=False)
                    # file_no = request.POST.get('file_no') 
                    contact.save()
                    return redirect('create-matter-other-party', file_no=file_no)
                    # return render(request, 'matter/matter_info.html', {'file_no': file_no} )
                else:
                    messages.error(request, 'An error occured! Matter not saved!')            
            else:
                print("Nothing went wrong")
                form = MatterAttorneyForm(request.POST, instance=matterInfo)
                if form.is_valid():
                    form.save()
                    # return redirect('person-contact')
                    return redirect('create-matter-other-party', file_no=file_no)
                else:
                    messages.error(request, 'An error occured! Matter not saved!')          
        else:
            return redirect('home')

    context = {
        'form': form,
        'file_no' : file_no,        
    }
    return render(request, 'matter/matter_attorney.html', context)



@login_required(login_url='login')
def createMatterOtherParty(request, file_no):
    Person_contact = cPerson.objects.all()
    if file_no == request.session['file_no']:
        matterOPs = MatterConflictOtherParty.objects.select_for_update().filter(file_no=file_no)
        
        # forms = []
        # for matterOP in matterOPs:
        #     forms.append(MatterConflictOPForm(instance=matterOP))
    
    context = { 
        'Person_contact': Person_contact,
        'matterOPs': matterOPs,
        # 'forms': forms,
        'file_no': request.session['file_no'],
        }
   
    if request.method == 'POST':
        form = MatterConflictOPForm(request.POST)
        print(request.POST)
        if form.is_valid():
            otherParty = form.save(commit=False)
            # user.username = user.username.lower()
            otherParty.save()
            return JsonResponse({'message': 'success'}, safe=False)
            # return render(request, 'matter/update_other_party.html', context)
            # return render(request, 'contact/')
        else:
            return JsonResponse({'failed': 'failed'}, safe=False)
            # messages.error(request, 'An error occured! data saved!') 

    return render(request, 'matter/other_party.html', context)


@login_required(login_url='login')
def CreateMatterAdverseParty(request, file_no):
    # Person_contact = cPerson.objects.all()
    form_1 = MatterConflictAPForm()

    context = { 
        # 'Person_contact': Person_contact,
        'form_1': form_1,
        'file_no': request.session['file_no'],
        }

    if request.method == 'POST':
        form = MatterConflictAPForm(request.POST)
        if form.is_valid():
            adverseParty = form.save(commit=False)
            # user.username = user.username.lower()
            adverseParty.save()
            return JsonResponse({'message': 'success'}, safe=False)
            # return render(request, 'matter/update_other_party.html', context)
            # return render(request, 'contact/')
        else:
            return JsonResponse({'failed': 'failed'}, safe=False)

    return render(request, 'matter/adverse_party.html', context)


@login_required(login_url='login')
def CreateMatterOtherFileName(request, file_no):
    if file_no == request.session['file_no']:
        matterAFs = MatterConflictAssocFile.objects.filter(file_no=file_no)
    context = { 
        'matterAFs': matterAFs,
        'file_no': request.session['file_no'],
        }

    if request.method == 'POST':
        form = MatterConflictAFForm(request.POST)
        if form.is_valid():
            otherFilename = form.save(commit=False)
            # user.username = user.username.lower()
            otherFilename.save()
            matterAFs = MatterConflictAssocFile.objects.filter(file_no=file_no)
            matterAFData = serializers.serialize('json', matterAFs)
            return HttpResponse(matterAFData, content_type="text/json-comment-filtered")
            # return JsonResponse(matterAFData, safe=False)
        else:
            return JsonResponse({'failed': 'failed'}, safe=False)

    return render(request, 'matter/other_file_name.html', context)


@login_required(login_url='login')
def createMatterDocument(request, file_no):
    form = MatterDocumentForm()
    file_no = request.session['file_no']
    if request.method == 'POST':
        form = MatterDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            contact = form.save(commit=False)
            # user.username = user.username.lower()
            contact.save()
            return redirect('create-matter-nature-civil', file_no=file_no)
            # return render(request, 'contact/')
        else:
            messages.error(request, 'An error occured! Document not saved!')
    else:
        messages.error(request, 'An error occured! Document not saved!')

    return render(request, 'matter/document.html', {'form': form})


@login_required(login_url='login')
def createMatterNatureCivil(request, file_no):
    if file_no == request.session['file_no']:
        form = MatterNatureCivilForm()   
        if request.method == 'POST' and len(request.POST) > 0:
            print(request.POST)
            print(len(request.POST))

            form = MatterNatureCivilForm(request.POST)
            if form.is_valid():
                # matter_nature = form.save(commit=False)
                form.save()
                # matter_nature.save_m2m() # needed since using commit=False
            return redirect('create-matter-nature-criminal', file_no=file_no )
        else:
            messages.error(request, 'An error occured! nature not saved!')
    context = {
        'form': form,
    }
    # print(matter_sample)
    return render(request, 'matter/nature_civil.html', context)

@login_required(login_url='login')
def createMatterNatureCriminal(request, file_no):
    if file_no == request.session['file_no']:
        form = MatterNatureCriminalForm()   
        if request.method == 'POST' and len(request.POST) > 0:
            print(request.POST)
            print(len(request.POST))
            form = MatterNatureCriminalForm(request.POST)
            if form.is_valid():
                # matter_nature = form.save(commit=False)
                form.save()
                # matter_nature.save_m2m() # needed since using commit=False
            return redirect('create-matter-description', file_no=file_no )
        else:
            messages.error(request, 'An error occured! Matter not saved!')
    context = {
        'form': form,
    }
    # print(matter_sample)
    return render(request, 'matter/nature_criminal.html', context)

@login_required(login_url='login')
def createMatterDescription(request, file_no):
    form = MatterDescriptionForm()
    file_no = request.session['file_no']
    if request.method == 'POST':
        form = MatterDescriptionForm(request.POST)
        if form.is_valid():
            descr = form.save(commit=False)
            # file_no = request.POST.get('file_no') 
            descr.save()

        if "file_no" in request.session.keys():
            del request.session["file_no"]

        return redirect('matter')
        # return render(request, 'contact/')
    else:
        messages.error(request, 'An error occured! Matter not saved!')
    context = {
        'form': form,
    }
    return render(request, 'matter/description.html', context)

# if request.method=='POST':
#     form = ProfileForm(request.POST)
#     if form.is_valid():
#         profile = form.save(commit=False)
#         profile.user = request.user
#         profile.save()
#         form.save_m2m() # needed since using commit=False
#     else:
#         form = ProfileForm()

# return render_to_response(template_name, {"profile_form": form}, context_instance=RequestContext(request))





@login_required(login_url='login')
def viewMatter_old(request, file_no):
    MatterInfor = MatterInfo.objects.get(file_no=file_no)
    Attorney = MatterAttorney.objects.get(file_no=file_no)
    ConflictOtherParties = MatterConflictOtherParty.objects.filter(file_no=file_no)
    ConflictAdverseParties = MatterConflictAdverseParty.objects.filter(file_no=file_no)
    ConflictAssocFiles = MatterConflictAssocFile.objects.filter(file_no=file_no)
    # Document = MatterDocument.objects.get(file_no=file_no)
    # CivilNature = MatterCivilNature.objects.filter(file_no=file_no)
    # CriminalNature = MatterCriminalNature.objects.filter(file_no=file_no)
    natureCivilSample = CivilMatterSample.objects.filter(mattercivilnature__file_no=file_no)
    natureCriminalSample = CriminalMatterSample.objects.filter(mattercriminalnature__file_no=file_no)
    Description = MatterDescription.objects.get(file_no=file_no)

    # print(Document)
    # attorney = Attorney.supervising_attorney_id.first_name

    context = {
        'Attorney': Attorney,
        'MatterInfor': MatterInfor,
        'ConflictOtherParties': ConflictOtherParties,
        'ConflictAdverseParties': ConflictAdverseParties,
        'ConflictAssocFiles': ConflictAssocFiles,
        'Document': Document,
        'natureCivilSample': natureCivilSample,
        'natureCriminalSample': natureCriminalSample,
        'Description': Description,
        # 'attorney': attorney,
        }

    return render(request, 'matter/view_matter.html', context)




@login_required(login_url='login')
def viewMatter(request, file_no):
    # if request.session['file_no'] is None or request.session['file_no'] is not file_no:
    request.session['file_no'] = file_no
    Attorney = []
    myDocuments = []
    Coparties = []
    ConflictAdverseParties = []
    ConflictAssocFiles = []
    Description = []
    Client_Type = []
    Assignee = []
    NatureOfClaims = []
    # MatterInfor = get_object_or_404(MatterInfo, file_no= file_no)
    # Attorney = get_object_or_404(MatterAttorney, file_no= file_no)
    # Coparties = get_object_or_404(MatterConflictOtherParty, file_no= file_no)
    MatterInfor = MatterInfo.objects.get(file_no=file_no)
    if MatterAttorney.objects.filter(file_no=file_no).exists():
        Attorney = MatterAttorney.objects.filter(file_no=file_no)
    if MatterConflictOtherParty.objects.filter(file_no=file_no).exists():
        Coparties = MatterConflictOtherParty.objects.filter(file_no=file_no)
    if MatterConflictAdverseParty.objects.filter(file_no=file_no).exists():
            ConflictAdverseParties = MatterConflictAdverseParty.objects.filter(file_no=file_no)
    if MatterConflictAssocFile.objects.filter(file_no=file_no).exists():
        ConflictAssocFiles = MatterConflictAssocFile.objects.filter(file_no=file_no)
    # if MatterDocument.objects.filter(file_no=file_no).exists():
    myDocuments = MatterFactDocument.objects.filter(file_no=file_no)
    if NatureOfClaim.objects.filter(file_no=file_no).exists():
        NatureOfClaims = NatureOfClaim.objects.filter(file_no=file_no)
    # CivilNature = MatterCivilNature.objects.filter(file_no=file_no)
    # CriminalNature = MatterCriminalNature.objects.filter(file_no=file_no)
    # natureCivilSample = CivilMatterSample.objects.filter(mattercivilnature__file_no=file_no)
    # natureCriminalSample = CriminalMatterSample.objects.filter(mattercriminalnature__file_no=file_no)
    if MatterDescription.objects.filter(file_no=file_no).exists():
        Description = MatterDescription.objects.filter(file_no=file_no)        
    if ClientType.objects.filter(file_no=file_no).exists():
        Client_Type = ClientType.objects.filter(file_no=file_no)

    if AssignedTo.objects.filter(file_no=file_no).exists():
        Assignee = AssignedTo.objects.filter(file_no=file_no)
    # print(myDocuments)


    context={
        'MatterInfor': MatterInfor,
        'Attorney': Attorney,
        'Coparties': Coparties,
        'ConflictAdverseParties': ConflictAdverseParties,
        'ConflictAssocFiles': ConflictAssocFiles,
        'Description': Description,
        'file_no': file_no,
        'Client_Type': Client_Type,
        'Assignee': Assignee,
        'myDocuments': myDocuments,
        'NatureOfClaims': NatureOfClaims,
        
        }

    return render(request, 'matter/view_matter.html', context)





@login_required(login_url='login')
def UpdateMatterInfo_old(request, file_no):
    matterInfo = MatterInfo.objects.get(file_no=file_no)
    form = MatterInfoForm(instance=matterInfo)

    if request.method == 'POST':
        form = MatterInfoForm(request.POST, instance=matterInfo)
        if form.is_valid():
            form.save()
            request.session['file_no'] = file_no
            return redirect('update-matter-attorney', file_no=file_no)
            # return render(request, 'contact/')
        else:
            messages.error(request, 'An error occured! Contact not updated!')

    context = { 
        'matterInfo': matterInfo,
        'form': form,
        }
    return render(request, 'matter/update_matter_info.html', context)


@login_required(login_url='login')
def UpdateMatterAttorney(request, file_no):
    if file_no == request.session['file_no']:
        matterAttorney = MatterAttorney.objects.get(file_no=file_no)
        form = MatterAttorneyForm(instance=matterAttorney)

    if request.method == 'POST':
        form = MatterAttorneyForm(request.POST, instance=matterAttorney)
        if form.is_valid():
            form.save()
            if request.POST.get('saveContinue'):
                return redirect('update-matter-other-party', file_no=file_no)

            if request.POST.get('saveClose'):
                del request.session["file_no"]
                return redirect('matter')

        else:
            messages.error(request, 'An error occured! Matter Info not updated!')

    context = { 
        # 'matterInfo': matterInfo,
        'form': form,
        'file_no': request.session['file_no'],
        }
    return render(request, 'matter/update_matter_attorney.html', context)


@login_required(login_url='login')
def UpdateMatterOtherParty(request, file_no):
    Person_contact = cPerson.objects.all()
    if file_no == request.session['file_no']:
        matterOPs = MatterConflictOtherParty.objects.filter(file_no=file_no)
        # forms = []
        # for matterOP in matterOPs:
        #     forms.append(MatterConflictOPForm(instance=matterOP))
    
    context = { 
        'Person_contact': Person_contact,
        'matterOPs': matterOPs,
        # 'forms': forms,
        'file_no': request.session['file_no'],
        }
   
    if request.method == 'POST':
        form = MatterConflictOPForm(request.POST)
        print(request.POST)
        if form.is_valid():
            otherParty = form.save(commit=False)
            # user.username = user.username.lower()
            otherParty.save()
            return JsonResponse({'message': 'success'}, safe=False)
            # return render(request, 'matter/update_other_party.html', context)
            # return render(request, 'contact/')
        else:
            return JsonResponse({'failed': 'failed'}, safe=False)
            # messages.error(request, 'An error occured! data saved!') 
    return render(request, 'matter/update_other_party.html', context)


@login_required(login_url='login')
def UpdateMatterAdverseParty(request, file_no):
    # Person_contact = cPerson.objects.all()
    form_1 = MatterConflictAPForm()

    context = { 
        # 'Person_contact': Person_contact,
        'form_1': form_1,
        'file_no': request.session['file_no'],
        }

    if request.method == 'POST':
        form = MatterConflictAPForm(request.POST)
        if form.is_valid():
            adverseParty = form.save(commit=False)
            # user.username = user.username.lower()
            adverseParty.save()
            return JsonResponse({'message': 'success'}, safe=False)
            # return render(request, 'matter/update_other_party.html', context)
            # return render(request, 'contact/')
        else:
            return JsonResponse({'failed': 'failed'}, safe=False)

    return render(request, 'matter/update_adverse_party.html', context)



@login_required(login_url='login')
def UpdateMatterOtherFileName(request, file_no):
    if file_no == request.session['file_no']:
        matterAFs = MatterConflictAssocFile.objects.filter(file_no=file_no)
    context = { 
        'matterAFs': matterAFs,
        'file_no': request.session['file_no'],
        }

    if request.method == 'POST':
        form = MatterConflictAFForm(request.POST)
        if form.is_valid():
            otherFilename = form.save(commit=False)
            # user.username = user.username.lower()
            otherFilename.save()
            matterAFs = MatterConflictAssocFile.objects.filter(file_no=file_no)
            matterAFData = serializers.serialize('json', matterAFs)
            return HttpResponse(matterAFData, content_type="text/json-comment-filtered")
            # return JsonResponse(matterAFData, safe=False)
        else:
            return JsonResponse({'failed': 'failed'}, safe=False)

    return render(request, 'matter/update_other_file_name.html', context)


@login_required(login_url='login')
def UpdateMatterDocument(request, file_no):
    if file_no == request.session['file_no']:
        # matterDoc = get_object_or_404(MatterDocument, file_no=file_no)
        matterDoc = ''
        form = ''
        if not MatterDocument.objects.filter(file_no=file_no).exists():
            # matterDoc = MatterDocument.objects.get(file_no=file_no)
            form = MatterDocumentForm()
        else:
            matterDoc = MatterDocument.objects.get(file_no=file_no)
            form = MatterDocumentForm(instance=matterDoc)

        context = { 
            'matterDoc': matterDoc,
            'form': form,
            'file_no': request.session['file_no'],
            }

        if request.method == 'POST':
            from django.utils.datastructures import MultiValueDictKeyError
            fields = []
            # print(request.FILES)
            try:
                for key in request.FILES:
                    if request.FILES[key]:
                        fields.append(key)
                        # print(key)

            except MultiValueDictKeyError:
                is_private = False
            # print(fields)
            matter_Doc = MatterDocument.objects.get(file_no=file_no)
            # print(matter_Doc)
            Form = modelform_factory(
                MatterDocument, form=MatterDocumentForm, fields= fields
            )
            form = Form(request.POST, request.FILES, instance=matter_Doc)
            if form.is_valid():
                form.save()
                # print(request.POST.get('writ_of_summon'))
                return redirect('update-matter-nature-civil', file_no=file_no)
            else:
                return render(request, 'matter/update_document.html', context)

    return render(request, 'matter/update_document.html', context)



@login_required(login_url='login')
def UpdateMatterNatureCivil(request, file_no):
    if file_no == request.session['file_no']:
        # try:
        # matterNature = get_object_or_404(MatterCivilNature, file_no=file_no)
        matterNature = MatterCivilNature.objects.get(file_no=file_no)
        # except:
            # form = MatterNatureCivilForm()
        # else:
        form = MatterNatureCivilForm(instance=matterNature)
    # cursor = connection.cursor()
    # cursor.execute('SELECT * FROM matter_matternature_cases_selected')
    # cursor = connection.cursor()
    # solution = cursor.fetchall()
    # selectedNature = list(solution)

        if request.method == 'POST':
            try:
                form_new = MatterNatureCivilForm(request.POST, instance=matterNature)
            except:
                form_new = MatterNatureCivilForm(request.POST)

            if form_new.is_valid():
                form_new.save()
                return redirect('update-matter-nature-criminal', file_no=file_no )
            else:
                messages.error(request, 'An error occured! Matter not saved!')
        context = {
            'form': form,
        }
    return render(request, 'matter/update_nature_civil.html', context)


@login_required(login_url='login')
def UpdateMatterNatureCriminal(request, file_no):
    if file_no == request.session['file_no']:
        # try:
            # matterNature = get_object_or_404(MatterCriminalNature, file_no=file_no)
        matterNature = MatterCriminalNature.objects.get(file_no=file_no)
        # except:
            # form = MatterNatureCriminalForm()
        # else:
        form = MatterNatureCriminalForm(instance=matterNature)
        # cursor = connection.cursor()
        # cursor.execute('SELECT * FROM matter_matternature_cases_selected')
        # cursor = connection.cursor()
        # solution = cursor.fetchall()
        # selectedNature = list(solution)
        if request.method == 'POST':
            try:
                form_new = MatterNatureCriminalForm(request.POST, instance=matterNature)
            except:
                form_new = MatterNatureCriminalForm(request.POST)
            if form_new.is_valid():
                form_new.save()
                return redirect('update-matter-description', file_no=file_no )
            else:
                messages.error(request, 'An error occured! Matter not saved!')
        context = {
            'form': form,
        }
    return render(request, 'matter/update_nature_criminal.html', context)



@login_required(login_url='login')
def UpdateMatterDescription(request, file_no):
    if file_no == request.session['file_no']:
        # try:
        matterDescr = MatterDescription.objects.get(file_no=file_no)        
        # except:
            # form = MatterDescriptionForm()
        # else:
        form = MatterDescriptionForm(instance=matterDescr)

        if request.method == 'POST':
            try:
                form_new = MatterDescriptionForm(request.POST, instance=matterDescr)
            except:
                form_new = MatterDescriptionForm(request.POST)
            if form_new.is_valid():
                form_new.save()
                del request.session["file_no"]
                messages.success(request, 'Matter Information updated successfully !')
                return redirect('matter')

            else:
                messages.error(request, 'An error occured! Matter Info not updated!')

        context = { 
            # 'matterInfo': matterInfo,
            'form': form,
            'file_no': request.session['file_no'],
            }
    return render(request, 'matter/update_description.html', context)


@login_required(login_url='login')
def DeleteMatterData(request):    
    # if request.user != room.host:
    #     return HttpResponse('Your are not allowed here!!')
    if request.method == 'POST':
        if request.POST.get('page') == 'adverse_party':
            dkey = request.POST.get('id')
            matter_AP = MatterConflictAdverseParty.objects.get(id_no=dkey)
            matter_AP.delete()

        elif request.POST.get('page') == 'other_party':
            dkey = request.POST.get('id')
            matter_OP = MatterConflictOtherParty.objects.get(id_no=dkey)
            matter_OP.delete()

        elif request.POST.get('page') == 'other_file_name':
            dkey = request.POST.get('id')
            matter_AF = MatterConflictAssocFile.objects.get(id_no=dkey)
            matter_AF.delete()
        
        elif request.POST.get('page') == 'fact_document':
            dkey = request.POST.get('id')
            matter_AF = MatterFactDocument.objects.get(id=dkey)
            matter_AF.delete()

        elif request.POST.get('page') == 'nature_of_claim':
            dkey = request.POST.get('id')
            matter_AF = NatureOfClaim.objects.get(id=dkey)
            matter_AF.delete()

        elif request.POST.get('page') == 'matter_document':
            field = request.POST.get('field')
            # print(field)
            if field == 'writ_of_summon':
                matter_Doc = get_object_or_404(MatterDocument, file_no=request.POST.get('file_no'))
                matter_Doc.writ_of_summon = ''
                matter_Doc.save()
            
            elif field == 'statement_of_claim':
                matter_Doc = get_object_or_404(MatterDocument, file_no=request.POST.get('file_no'))
                matter_Doc.statement_of_claim = ''
                matter_Doc.save()    

            elif field == 'witness_statement_on_oath':
                matter_Doc = get_object_or_404(MatterDocument, file_no=request.POST.get('file_no'))
                matter_Doc.witness_statement_on_oath = ''
                matter_Doc.save()

            elif field == 'affidavit':
                matter_Doc = get_object_or_404(MatterDocument, file_no=request.POST.get('file_no'))
                matter_Doc.affidavit = ''
                matter_Doc.save()

            elif field == 'motion_exparte':
                matter_Doc = get_object_or_404(MatterDocument, file_no=request.POST.get('file_no'))
                matter_Doc.motion_exparte = ''
                matter_Doc.save()

            elif field == 'motion_on_notice':
                matter_Doc = get_object_or_404(MatterDocument, file_no=request.POST.get('file_no'))
                matter_Doc.motion_on_notice = ''
                matter_Doc.save()

            elif field == 'statement_of_defense':
                matter_Doc = get_object_or_404(MatterDocument, file_no=request.POST.get('file_no'))
                matter_Doc.statement_of_defense = ''
                matter_Doc.save()

            elif field == 'reply_doc':
                matter_Doc = get_object_or_404(MatterDocument, file_no=request.POST.get('file_no'))
                matter_Doc.reply_doc = ''
                matter_Doc.save()
            
            elif field == 'written_address':
                matter_Doc = get_object_or_404(MatterDocument, file_no=request.POST.get('file_no'))
                matter_Doc.written_address = ''
                matter_Doc.save()

        return JsonResponse({'success': True}, safe=False)
    return JsonResponse({'message':'error'})


    
def DataAutoloader(request):
    if request.method == 'GET':
        if request.GET.get('page') == 'other_file_name':
            file_no = request.GET.get('file_no')
            matterAFs = MatterConflictAssocFile.objects.filter(file_no=file_no)
            matterAFData = serializers.serialize('json', matterAFs)
            return HttpResponse(matterAFData, content_type="text/json-comment-filtered")

        # elif request.GET.get('page') == 'other_party':
        #     file_no = request.GET.get('file_no')
        #     matterOPs = MatterConflictOtherParty.objects.filter(file_no=file_no)
        #     matterAFData = serializers.serialize('json', matterOPs)
        #     return HttpResponse(matterAFData, content_type="text/json-comment-filtered")

        elif request.GET.get('page') == 'other_party':
            file_no = request.GET.get('file_no')
            cursor = connection.cursor()
            cursor.execute('SELECT matter_MatterConflictOtherParty.id_no, matter_MatterConflictOtherParty.other_party_relationship, contact_cPerson.id, contact_cPerson.familyName, contact_cPerson.firstName, contact_cPerson.otherName\
            FROM matter_MatterConflictOtherParty, contact_cPerson\
            WHERE  matter_MatterConflictOtherParty.other_party_id = contact_cPerson.id\
            AND matter_MatterConflictOtherParty.file_no_id = %s', [file_no])
            solution = cursor.fetchall()
            # matterAPss = MatterConflictAdverseParty.objects.filter(file_no=file_no).select_related('adverse_party')
            # print(matterAPss)
            # matterAPs = MatterConflictAdverseParty.objects.select_related('adverse_party_id').get(p_id=user)
            # matterAPs = MatterConflictAdverseParty.objects.filter(file_no=file_no)
            matterAPs = list(solution)
            # matterAFData = serializers.serialize('json', solution)
            # print(matterAFData)
            # return HttpResponse(solution, content_type="text/json-comment-filtered")
            return JsonResponse(matterAPs, safe=False)
        

        elif request.GET.get('page') == 'adverse_party':
            file_no = request.GET.get('file_no')
            cursor = connection.cursor()
            cursor.execute('SELECT matter_MatterConflictAdverseParty.id_no, contact_cPerson.id, contact_cPerson.familyName, contact_cPerson.firstName, contact_cPerson.otherName\
            FROM matter_MatterConflictAdverseParty, contact_cPerson\
            WHERE  matter_MatterConflictAdverseParty.adverse_party_id = contact_cPerson.id\
            AND matter_MatterConflictAdverseParty.file_no_id = %s', [file_no])
            solution = cursor.fetchall()
            # matterAPss = MatterConflictAdverseParty.objects.filter(file_no=file_no).select_related('adverse_party')
            # print(matterAPss)
            # matterAPs = MatterConflictAdverseParty.objects.select_related('adverse_party_id').get(p_id=user)
            # matterAPs = MatterConflictAdverseParty.objects.filter(file_no=file_no)
            matterAPs = list(solution)
            # matterAFData = serializers.serialize('json', solution)
            # print(matterAFData)
            # return HttpResponse(solution, content_type="text/json-comment-filtered")
            return JsonResponse(matterAPs, safe=False)
        
        elif request.GET.get('page') == 'matter_document':
            file_no = request.GET.get('file_no')
            matterDoc = MatterDocument.objects.filter(file_no=file_no)
            matterAFData = serializers.serialize('json', matterDoc)
            return HttpResponse(matterAFData, content_type="text/json-comment-filtered")

        elif request.GET.get('page') == 'fact_document':
            file_no = request.GET.get('file_no')
            matterDoc = MatterFactDocument.objects.filter(file_no=file_no)
            matterAFData = serializers.serialize('json', matterDoc)
            return HttpResponse(matterAFData, content_type="text/json-comment-filtered")

        elif request.GET.get('page') == 'nature_of_claim':
            file_no = request.GET.get('file_no')
            matterDoc = NatureOfClaim.objects.filter(file_no=file_no)
            matterAFData = serializers.serialize('json', matterDoc)
            return HttpResponse(matterAFData, content_type="text/json-comment-filtered")

        else:
            return JsonResponse({'failed': 'failed'}, safe=False)

    return render(request, 'matter/update_other_file_name.html', context)


def DeleteMatterRecords(request):

    if request.method == 'POST':
        file_no = request.POST.get('file_no')
        matter_info = MatterInfo.objects.get(file_no=file_no)
        matter_attorney = MatterAttorney.objects.get(file_no=file_no)
        matter_description = MatterDescription.objects.get(file_no=file_no)
        
        matter_conflict_OP = MatterConflictOtherParty.objects.filter(file_no=file_no)
        matter_conflict_AP = MatterConflictAdverseParty.objects.filter(file_no=file_no)
        matter_conflict_AF = MatterConflictAssocFile.objects.filter(file_no=file_no)
        matter_document = MatterDocument.objects.filter(file_no=file_no)
        matter_criminal = MatterCriminalNature.objects.filter(file_no=file_no)
        matter_civil = MatterCivilNature.objects.filter(file_no=file_no)
        # for op in matter_conflict_OP:
        # print(matter_document)
        matter_info.delete()
        matter_attorney.delete()
        matter_description.delete()
        matter_document.delete()
        matter_criminal.delete()
        matter_civil.delete()
        for op in matter_conflict_OP:
            op.delete
        for ap in matter_conflict_AP:
            ap.delete     
        for af in matter_conflict_AF:
            af.delete  

        message = [{'success': True}]
        SerialMsg = list(message)
        return JsonResponse(SerialMsg, safe=False)
    return JsonResponse({'success': False}, safe=False)



