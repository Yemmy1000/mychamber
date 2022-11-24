from django import forms
from .models import *
# MatterInfo, MatterAttorney, MatterConflictOtherParty, MatterConflictAdverseParty, MatterConflictAssocFile, MatterDocument, CivilMatterSample, CriminalMatterSample, MatterCivilNature, MatterCriminalNature, MatterDescription
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div
from django.core.files import File
from base.widgets import DatePickerInput, TimePickerInput, DateTimePickerInput
# from bootstrap_datepicker_plus import DateInput

class MatterInfoForm(forms.ModelForm):
    class Meta:
        model= MatterInfo
        # fields= ["fullname", "email", "contact", "message"]
        fields = '__all__'
        label = {
            'file_no': 'File Number:'
        }
        widgets = {
        'file_no': forms.TextInput(attrs={'name': 'file_no', 'class':'form-control', 'readonly': 'readonly'}),
        'client_contact': forms.Select(attrs={'class':'select2 form-select shadow-none', 'id': 'single_client_contact', 'data-live-search':"true", 'style':"width: 100%; height: 36px"}),
    }


class MatterAttorneyForm(forms.ModelForm):
    class Meta:
        model= MatterAttorney
        # fields= ["fullname", "email", "contact", "message"]
        fields = '__all__'
        label = {
            'file_no': 'File Number:',
        }
        widgets = {
        'file_no': forms.TextInput(attrs={'name': 'file_no', 'class':'form-control', 'readonly': 'readonly'}),
        'claim_no': forms.TextInput(attrs={'name': 'claim_no', 'class':'form-control'}),
        'referrer': forms.Select(attrs={'class':'select2 form-select shadow-none', 'id': 'referrer', 'style':"width: 100%; height: 36px"}),
        'originating_attorney': forms.Select(attrs={'class':'select2 form-select shadow-none', 'id': 'originating_attorney', 'style':"width: 100%; height: 36px"}),
        'supervising_attorney': forms.Select(attrs={'class':'select2 form-select shadow-none', 'id': 'supervising_attorney', 'style':"width: 100%; height: 36px"}),
        # 'start_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        # 'start_time': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'time'}),
        # 'end_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        # 'description': forms.Textarea(attrs={'id':'educationDescription', 'placeholder':'Description', 'rows':'3'}),
        # 'companyDescription': forms.Textarea(attrs={'Label':'Company Description', 'id':'CompanyDescription', 'placeholder':'Description', 'rows':'3'}),
        # 'dateGraduated': forms.DateInput(format=('%m/%d/%Y'), attrs={'placeholder':'Select a date', 'type':'date'}),
    }


class MatterConflictOPForm(forms.ModelForm):
    class Meta:
        model= MatterConflictOtherParty
        # fields= ["fullname", "email", "contact", "message"]
        fields = '__all__'
        widgets = {
        'other_party_relationship': forms.TextInput(attrs={'name': 'other_party_relationship[]', 'class':''}),
        'other_party': forms.Select(attrs={'class':'select2 form-select shadow-none', 'id': 'other_party', 'data-live-search':"true", 'data-placeholder': 'Choose other_party'}),
        # 'adverse_party': forms.Select(attrs={'label':'Adverse Party',  'class':'selectpicker form-select', 'name': 'adverse_party[]', 'data-live-search':"true", 'data-placeholder': 'Choose other_party'}),
        # 'supervising_attorney': forms.Select(attrs={'label':'supervising attorney', 'placeholder':'Description', 'class':'selectpicker form-select', 'id': 'supervising_attorney', 'data-live-search':"true", 'data-placeholder': 'Choose supervising attorney'}),
    }


class MatterConflictAPForm(forms.ModelForm):
    class Meta:
        model= MatterConflictAdverseParty
        # fields= ["fullname", "email", "contact", "message"]
        fields = '__all__'
        widgets = {
        # 'other_party_relationship': forms.TextInput(attrs={'label':'Relationship', 'placeholder':'What is the relationship with client', 'name': 'relationship[]', 'class':''}),
        # 'other_party': forms.Select(attrs={'label':'Other Party', 'class':'selectpicker form-select', 'name': 'other_party[]', 'data-live-search':"true", 'data-placeholder': 'Choose other_party'}),
        'adverse_party': forms.Select(attrs={'class':'select2 form-select shadow-none', 'name': 'adverse_party', 'id': 'adverse_party', 'data-live-search':"true", 'style':"width: 100%; height: 40px" }),
        # 'supervising_attorney': forms.Select(attrs={'label':'supervising attorney', 'placeholder':'Description', 'class':'selectpicker form-select', 'id': 'supervising_attorney', 'data-live-search':"true", 'data-placeholder': 'Choose supervising attorney'}),
    }
    
class MatterConflictAFForm(forms.ModelForm):
    class Meta:
        model= MatterConflictAssocFile
        # fields= ["fullname", "email", "contact", "message"]
        fields = '__all__'
        widgets = {
        # 'other_party_relationship': forms.TextInput(attrs={'label':'Relationship', 'placeholder':'What is the relationship with client', 'name': 'relationship[]', 'class':''}),
        # 'other_party': forms.Select(attrs={'label':'Other Party', 'class':'selectpicker form-select', 'name': 'other_party[]', 'data-live-search':"true", 'data-placeholder': 'Choose other_party'}),
        # 'adverse_party': forms.Select(attrs={'label':'Adverse Party',  'class':'selectpicker form-select', 'name': 'adverse_party[]', 'data-live-search':"true", 'data-placeholder': 'Choose other_party'}),
        # 'supervising_attorney': forms.Select(attrs={'label':'supervising attorney', 'placeholder':'Description', 'class':'selectpicker form-select', 'id': 'supervising_attorney', 'data-live-search':"true", 'data-placeholder': 'Choose supervising attorney'}),
    }
# remove this later
class MatterDocumentForm(forms.ModelForm):
    class Meta:
        model= MatterDocument
        # fields= ["fullname", "email", "contact", "message"]
        fields = '__all__'
        # exclude = ['file_no']
        widgets = {
        'writ_of_summon': forms.FileInput(attrs={'class':'writ_of_summon', 'id':'writ_of_summon', 'data-max-file-size':'2M', 'type':'file'}),
        'statement_of_claim': forms.FileInput(attrs={'class':'statement_of_claim', 'id':'statement_of_claim', 'data-max-file-size':'2M', 'type':'file'}),
        'witness_statement_on_oath': forms.FileInput(attrs={'class':'witness_statement_on_oath', 'id':'witness_statement_on_oath', 'data-max-file-size':'2M', 'type':'file'}),
        'affidavit': forms.FileInput(attrs={'class':'affidavit', 'id':'affidavit', 'data-max-file-size':'2M', 'type':'file'}),
        'motion_exparte': forms.FileInput(attrs={'class':'motion_exparte', 'id':'motion_exparte', 'data-max-file-size':'2M', 'type':'file'}),
        'statement_of_defense': forms.FileInput(attrs={'class':'statement_of_defense', 'id':'statement_of_defense', 'data-max-file-size':'2M', 'type':'file'}),
        'motion_on_notice': forms.FileInput(attrs={'class':'motion_on_notice', 'id':'motion_on_notice', 'data-max-file-size':'2M', 'type':'file'}),
        'reply_doc': forms.FileInput(attrs={'class':'reply_doc', 'id':'reply_doc', 'data-max-file-size':'2M', 'type':'file'}),
        'written_address': forms.FileInput(attrs={'class':'written_address', 'id':'written_address', 'data-max-file-size':'2M', 'type':'file'}),
    }


class MatterDocumentForm(forms.ModelForm):
    class Meta:
        model= MatterFactDocument
        # fields= ["fullname", "email", "contact", "message"]
        fields = '__all__'
        # exclude = ['file_no']
        widgets = {

    }


class MatterNatureCivilForm(forms.ModelForm):
    # cases_selected = forms.ModelMultipleChoiceField(queryset=MatterSample.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)
    cases = forms.ModelMultipleChoiceField(queryset=CivilMatterSample.objects.all(), required=False, label='Civil Matters', widget=forms.CheckboxSelectMultiple)
    # criminal_choices = forms.ModelMultipleChoiceField(queryset=MatterSample.objects.filter(category='Civil'), required=False, widget=forms.CheckboxSelectMultiple)
    class Meta:
        model= MatterCivilNature
        # fields= ["title"]
        fields = '__all__'
        label ={
            'cases': 'Civil Matters'
        }
        widgets = {
            # MatterClient.objects.get(file_no=file_no)
    }

class MatterNatureCriminalForm(forms.ModelForm):
    # cases_selected = forms.ModelMultipleChoiceField(queryset=MatterSample.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)
    cases = forms.ModelMultipleChoiceField(queryset=CriminalMatterSample.objects.all(), required=False, label='Criminal Matters', widget=forms.CheckboxSelectMultiple)
    class Meta:
        model= MatterCriminalNature
        # fields= ["title"]
        fields = '__all__'
        label ={
            'cases': 'Criminal Matters'
        }
        widgets = {
            # MatterClient.objects.get(file_no=file_no)
    }


class MatterDescriptionForm(forms.ModelForm):
    class Meta:
        model= MatterDescription
        # fields= ["title"]
        fields = '__all__'
        label ={
            'description': 'Case Summary'
        }
        widgets = {
        'description': forms.Textarea(attrs={'id':'MatterDescription', 'placeholder':'Summary', 'maxlength': 200, 'rows':'3'}),
    }


class CaseAssigneeForm(forms.ModelForm):
    class Meta:
        model= AssignedTo
        # fields= ["title"]
        fields = '__all__'
        label ={
            'personnel': 'Case Assignee'
        }
        widgets = {
            'personnel': forms.Select(attrs={'class':'select2 form-select shadow-none', 'name': 'personnel', 'id': '', 'data-live-search':"true", 'style':"width: 100%; height: 40px" }),
        }

class NatureOfClaimForm(forms.ModelForm):
    class Meta:
        model= NatureOfClaim
        # fields= ["title"]
        fields = '__all__'
        label ={
            'category': 'Matter category'
        }
        widgets = {
            # 'nature_of_claim': forms.TextInput(attrs={ 'class':'form-control', 'id': 'nature_of_claim' }),
            # 'category': forms.Select(attrs={'class':'form-select form-control shadow-none', 'id': 'category',  'style':"width: 100%; height: 34px" }),
        }



class UpdateLogForm(forms.ModelForm):
    class Meta:
        model= UpdateLog
        # fields= ["title"]
        fields = '__all__'
        label ={
            # 'category': 'Matter category'
        }
        widgets = {
            # 'nature_of_claim': forms.TextInput(attrs={ 'class':'form-control', 'id': 'nature_of_claim' }),
            # 'category': forms.Select(attrs={'class':'form-select form-control shadow-none', 'id': 'category',  'style':"width: 100%; height: 34px" }),
        }

        