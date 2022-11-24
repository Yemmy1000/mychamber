from django import forms
from .models import DefendantDocumentType, ClaimantDocumentType
from matter.models import CivilMatterSample, CriminalMatterSample
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div

# from bootstrap_datepicker_plus import DateInput

# class SystemSettingsForm(forms.ModelForm):
#     class Meta:
#         model= MatterSample
#         # fields= ["fullname", "email", "contact", "message"]
#         fields = '__all__'
#         widgets = {
#         # 'client_contact': forms.Select(attrs={'label':'Client Contact', 'placeholder':'Description', 'class':'selectpicker form-select', 'id': 'single_client_contact', 'data-live-search':"true", 'data-placeholder': 'Choose one thing'}),
#     }


class CriminalMatterForm(forms.ModelForm):
    class Meta:
        model= CriminalMatterSample
        # fields= ["fullname", "email", "contact", "message"]
        fields = '__all__'
        widgets = {
        'title': forms.TextInput(attrs={'id':'title'}),
        'description': forms.Textarea(attrs={'id':'description', 'placeholder':'', 'rows':'3'}),
    }


class CivilMatterForm(forms.ModelForm):
    class Meta:
        model= CivilMatterSample
        # fields= ["fullname", "email", "contact", "message"]
        fields = '__all__'
        widgets = {
        'title': forms.TextInput(attrs={'id':'title'}),
        'description': forms.Textarea(attrs={'id':'description', 'placeholder':'', 'rows':'3'}),
    }

class DefendantDocumentTypeForm(forms.ModelForm):
    class Meta:
        model= DefendantDocumentType
        # fields= ["fullname", "email", "contact", "message"]
        fields = '__all__'
        widgets = {
        'doc_type': forms.TextInput(attrs={'id':'doc_type'}),
        'description': forms.Textarea(attrs={'id':'description', 'placeholder':'', 'rows':'3'}),
    }

class ClaimantDocumentTypeForm(forms.ModelForm):
    class Meta:
        model= ClaimantDocumentType
        # fields= ["fullname", "email", "contact", "message"]
        fields = '__all__'
        widgets = {
        'doc_type': forms.TextInput(attrs={'id':'doc_type'}),
        'description': forms.Textarea(attrs={'id':'description', 'placeholder':'', 'rows':'3'}),
    }

