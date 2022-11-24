from django import forms
from matter.models import ClientType
from crispy_forms.helper import FormHelper

# from bootstrap_datepicker_plus import DateInput

class ClientTypeForm(forms.ModelForm):
    class Meta:
        model= ClientType
        # fields= ["fullname", "email", "contact", "message"]
        fields = '__all__'
        label = {
            'file_no': 'File Number:'
        }
        widgets = {
            
            'client_type': forms.Select(attrs={'class':'form-control'}),
    }