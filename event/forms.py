from django import forms
from .models import Event
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div
from django.core.files import File
from base.widgets import DatePickerInput, TimePickerInput, DateTimePickerInput
from base.models import CustomUser
# from bootstrap_datepicker_plus import DateInput

class EventForm(forms.ModelForm):
    participant = forms.ModelMultipleChoiceField(queryset=CustomUser.objects.all(), 
    required=False, label='Participants', 
    widget= forms.Select(attrs={'class':'select2 form-select shadow-none', 'id': 'participant-select', 'multiple': 'multiple', 'rows':'3', 'style':"width: 100%; height: 36px"}),
    )
    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        # self.helper = FormHelper()
        # self.helper.form_show_labels = False 
        # self.fields['category'].label = ''
        # self.fields['priority'].label = ''
        # self.fields['status'].label = ''
        self.fields['matter'].label = ''
        self.fields['start'].label = ''

    class Meta:
        model= Event
        # fields= ["fullname", "email", "contact", "message"]
        fields = '__all__'
        label={
            'title': 'Title'
        }
        widgets = {
        'matter': forms.Select(attrs={'class':'select2 form-select shadow-none', 'id': 'matter', 'style':"width: 100%; height: 36px"}),
        'start': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'type':'date'}),
        # 'start_time': forms.TimeField(widget=forms.TimeInput(format='%H:%M')),
        'end': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'type':'date'}),
        # 'end_time': forms.TimeField(widget=forms.TimeInput(format='%H:%M')) ,
        # 'participant': forms.Select(attrs={'class':'select2 form-select shadow-none', 'id': 'participant-select', 'multiple': 'multiple', 'rows':'3', 'style':"width: 100%; height: 36px"}),
        'description': forms.Textarea(attrs={'id':'eventDescription', 'placeholder':'Description', 'rows':'3'}),
        'category': forms.Select(attrs={'id': 'eventCategory'}),
        'priority': forms.Select(attrs={'id': 'eventPriority'}),
        'status': forms.Select(attrs={'id': 'eventStatus'}),
        # 'companyDescription': forms.Textarea(attrs={'Label':'Company Description', 'id':'CompanyDescription', 'placeholder':'Description', 'rows':'3'}),
        # 'dateGraduated': forms.DateInput(format=('%m/%d/%Y'), attrs={'placeholder':'Select a date', 'type':'date'}),
    }
        