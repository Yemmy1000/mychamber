from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import TemplateResponseMixin, View
from django.http import HttpResponse, JsonResponse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import ClientTypeForm
from matter.forms import MatterAttorneyForm, MatterConflictOPForm, MatterConflictAPForm, MatterConflictAFForm, MatterDescriptionForm, CaseAssigneeForm, \
    MatterDocumentForm, NatureOfClaimForm, MatterInfoForm
from matter.models import *
from matter.models import NatureOfClaim
from contact.models import cPerson
from systemsettings.models import ClaimantDocumentType, DefendantDocumentType
# MatterInfo, MatterAttorney, MatterConflictOtherParty, MatterDescription

# Create your views here.


class MatterUpdate(TemplateResponseMixin, View):
    # model = MatterInfo
    template_name = "matterupdate/index.html"

    # def get_queryset(self, file_no):
    #     qs = super().get_queryset()
    #     return qs.filter(file_no= file_no)

    def get(self, request, file_no):
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

        return self.render_to_response(context)


class ClientCategory(TemplateResponseMixin, View):
    form_class = ClientTypeForm
    template_name = 'matterupdate/client_category.html'

    def get(self, request, file_no, *args, **kwargs):
        form = self.form_class()
        context = {'form': form, 'file_no': file_no}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        file_no = request.POST.get('file_no')
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            form.save()
            return redirect('matter-update', file_no=file_no)
        context = {'form': form, 'file_no': file_no}
        return render(request, self.template_name, context)
        

class CaseAttorney(TemplateResponseMixin, View):
    form_class = MatterAttorneyForm
    template_name = 'matterupdate/attorney.html'

    def get(self, request, file_no, *args, **kwargs):
        form = self.form_class()
        context = {'form': form, 'file_no': file_no}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        file_no = request.POST.get('file_no')
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            form.save()
            return redirect('matter-update', file_no=file_no)
        context = {'form': form, 'file_no': file_no}
        return render(request, self.template_name, context)


class ClientCoparties(TemplateResponseMixin, View):
    form_class = MatterConflictOPForm
    template_name = 'matterupdate/coparties.html'

    def get(self, request, file_no, *args, **kwargs):
        form = self.form_class()
        Person_contact = cPerson.objects.all()
        context = {'form': form, 'file_no': file_no, 'Person_contact': Person_contact}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        file_no = request.POST.get('file_no')

        return redirect('matter-update', file_no=file_no)

class ClientAdverseParties(TemplateResponseMixin, View):
    form_class = MatterConflictAPForm
    template_name = 'matterupdate/adverse_parties.html'

    def get(self, request, file_no, *args, **kwargs):
        form = self.form_class()
        Person_contact = cPerson.objects.all()
        context = {'form': form, 'file_no': file_no, 'Person_contact': Person_contact}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        file_no = request.POST.get('file_no')

        return redirect('matter-update', file_no=file_no)


class CaseAssociateNames(TemplateResponseMixin, View):
    form_class = MatterConflictAFForm
    template_name = 'matterupdate/aassociate_names.html'

    def get(self, request, file_no, *args, **kwargs):
        form = self.form_class()
        CaseAssociatedNames = MatterConflictAssocFile.objects.filter(file_no=file_no)
        context = {'form': form, 'file_no': file_no, 'CaseAssociatedNames': CaseAssociatedNames}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        file_no = request.POST.get('file_no')

        return redirect('matter-update', file_no=file_no)


class CaseBrief(TemplateResponseMixin, View):
    form_class = MatterDescriptionForm
    template_name = 'matterupdate/case_brief.html'

    def get(self, request, file_no, *args, **kwargs):
        form = self.form_class()
        context = {'form': form, 'file_no': file_no}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        file_no = request.POST.get('file_no')
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            form.save()
            return redirect('matter-update', file_no=file_no)
        context = {'form': form, 'file_no': file_no}
        return render(request, self.template_name, context)


class EditCaseBrief(UpdateView):
    # specify the model you want to use
    model = MatterDescription
    form_class = MatterDescriptionForm
    template_name = 'matterupdate/update_case_brief.html' 

    def get_success_url(self):
        return reverse('matter-update', kwargs={'file_no': self.object.file_no})

class CaseAssignee(TemplateResponseMixin, View):
    form_class = CaseAssigneeForm
    template_name = 'matterupdate/case_assignee.html'

    def get(self, request, file_no, *args, **kwargs):
        form = self.form_class()
        context = {'form': form, 'file_no': file_no}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        file_no = request.POST.get('file_no')
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            form.save()
            return redirect('matter-update', file_no=file_no)
        context = {'form': form, 'file_no': file_no}
        return render(request, self.template_name, context)


class CaseAssigneeEdit(UpdateView):
    # specify the model you want to use
    model = AssignedTo
    form_class = CaseAssigneeForm
    template_name = 'matterupdate/case_assignee_edit.html' 

    def get_success_url(self):
        return reverse('matter-update', kwargs={'file_no': self.object.file_no})


class CaseFactDocument(TemplateResponseMixin, View):
    form_class = MatterDocumentForm
    template_name = 'matterupdate/fact_document.html'
    # claimant_class = ClaimantDocumentType.objects.all()
    # defendant_class = DefendantDocumentType.objects.all()

    def get(self, request, file_no, *args, **kwargs):
        form = self.form_class()
        # claimants = self.claimant_class()
        # defendants = self.defendant_class()
        claimants = ClaimantDocumentType.objects.all()
        defendants = DefendantDocumentType.objects.all()
        context = {'form': form, 'file_no': file_no, 'claimants': claimants, 'defendants': defendants}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        file_no = request.POST.get('file_no')
        print(request.POST)
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            # <process form cleaned data>
            form.save()
            # return redirect('matter-update', file_no=file_no)
            return JsonResponse({'message': 'success'})


class CaseNatureOfClaim(TemplateResponseMixin, View):
    form_class = NatureOfClaimForm
    template_name = 'matterupdate/nature_of_claim.html'
    # claimant_class = ClaimantDocumentType.objects.all()
    # defendant_class = DefendantDocumentType.objects.all()

    def get(self, request, file_no, *args, **kwargs):
        form = self.form_class()
        context = {'form': form, 'file_no': file_no}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        file_no = request.POST.get('file_no')
        print(request.POST)
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            form.save()
            # return redirect('matter-update', file_no=file_no)
            return JsonResponse({'message': 'success'})
        print(form.errors)


class UpdateBasicInformation_old(UpdateView):
    form_class = MatterInfoForm
    model = MatterInfo
    template_name = 'matterupdate/update_basic_information.html'

    def get(self, request, file_no, *args, **kwargs):
        matterInfo = MatterInfo.objects.get(file_no=file_no)
        form = self.form_class(instance=matterInfo)
        context = {'form': form, 'file_no': file_no}
        return render(request, self.template_name, context)

    # def post(self, request, *args, **kwargs):
    #     file_no = request.POST.get('file_no')
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('matter-update', file_no=file_no)
    #     context = {'form': form, 'file_no': file_no}
    #     return render(request, self.template_name, context)

def UpdateBasicInfo(request, file_no):
    # matterInfo = MatterInfo.objects.get(file_no=file_no)
    # form = MatterInfoForm(instance=matterInfo)

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
        # 'matterInfo': matterInfo,
        # 'form': form,
        }
    return render(request, 'matter/update_matter_info.html', context)