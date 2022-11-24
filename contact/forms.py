from django import forms
from .models import cPerson, cCompany
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div
from django.core.files import File
# from .widgets import DatePickerInput, TimePickerInput, DateTimePickerInput
# from bootstrap_datepicker_plus import DateInput

class ContactPersonForm(forms.ModelForm):
    class Meta:
        model= cPerson
        # fields= ["fullname", "email", "contact", "message"]
        fields = '__all__'
        # label = {
        # }
        widgets = {
        'firstName': forms.TextInput(attrs={'class':'form-control', 'id': 'firstName',}),
        'familyName': forms.TextInput(attrs={'class':'form-control', 'id': 'familyName',}),
        'dob': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'personPix': forms.FileInput(attrs={'class':'dropify', 'id':'personPix', 'data-default-file':'../../static/img/default-user.jpg', 'data-max-file-size':'2M', 'type':'file'}),
        'educationDescription': forms.Textarea(attrs={'id':'educationDescription', 'placeholder':'Description', 'rows':'3'}),
        'companyDescription': forms.Textarea(attrs={'Label':'Company Description', 'id':'CompanyDescription', 'placeholder':'Description', 'rows':'3'}),
        'dateGraduated': forms.DateInput(format=('%m/%d/%Y'), attrs={'placeholder':'Select a date', 'type':'date'}),
    }


class ContactCompanyForm(forms.ModelForm):
    class Meta:
        model= cCompany
        # fields= ["fullname", "email", "contact", "message"]
        fields = '__all__'
        widgets = {
        # 'dateFounded': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        # 'companyLogo': forms.FileInput(attrs={'class':'dropify', 'id':'personPix', 'data-default-file':'../../static/img/logo.png', 'data-max-file-size':'2M', 'type':'file'}),
        # 'firstRepresentative': forms.Select(attrs={'Label':'', 'placeholder':'Description', 'class':'form-select', 'id': 'single-s-f-firstRep', 'data-placeholder': 'Choose one thing'}),
        # 'secondRepresentative': forms.Select(attrs={'Label':'', 'placeholder':'Description', 'class':'form-select', 'id': 'single-s-f-secondRep', 'data-placeholder': 'Choose one thing'}),
        # 'thirdRepresentative': forms.Select(attrs={'Label':'', 'placeholder':'Description', 'class':'form-select', 'id': 'single-s-f-thirdRep', 'data-placeholder': 'Choose one thing'}),
        # 'companyActivityDescription': forms.Textarea(attrs={'Label':'Company Activities Description', 'id':'CompanyDescription', 'placeholder':'Description', 'rows':'3'}),
        # 'dateGraduated': forms.DateInput(format=('%m/%d/%Y'), attrs={'placeholder':'Select a date', 'type':'date'}),

    }









    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.layout = Layout(
    #         Div(
    #             Div('first_name', css_class='form-group col-4'),
    #             Div('last_name', css_class='form-group col-4'),
    #             Div('email', css_class='form-group col-4'),
    #             css_class='form-row'
    #         ),
    #         Div(
    #             Div('password', css_class='form-group col-4'),
    #             Div('confirm_password', css_class='form-group col-4'),
    #             css_class='form-row'
    #         ),
    #         Div(
    #             Div('gender', css_class='form-group col-4'),
    #             Div('phone_number', css_class='form-group col-8'),
    #             css_class='form-row'
    #         ),
    #         'about_you',
    #         Submit('submit', 'Sign up', css_class='mt-4')
    #     )

    # phone_number = us_forms.USPhoneNumberField(required=False)
    # state = us_forms.USStateField(widget=us_forms.USStateSelect, required=False)
    # zip_code = us_forms.USZipCodeField(label="ZIP Code", required=False)
