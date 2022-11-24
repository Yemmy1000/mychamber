from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, CustomUserProfile
from django import forms


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)


class UserForm(UserChangeForm):
    # password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
        fields = ['email', 'password']
        widgets = {
        # 'password': forms.PasswordInput(),
        }

class CustomUserForm(ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
        # fields = '__all__'
        # exclude = ['password', 'email', 'date_joined']
        fields = ['avatar', 'first_name', 'last_name', 'username', 'email', 'bio', 'dob', 'phone']
        widgets = {
            'first_name': forms.TextInput(attrs={'id': 'first_name', 'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'id': 'last_name', 'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control', 'readonly': 'readonly'}),
            'phone': forms.TextInput(attrs={'class':'form-control', 'maxlength': '11'}),
            'username': forms.TextInput(attrs={'class':'form-control', 'readonly': 'readonly'}),
            'dob': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
            # 'avatar': forms.FileInput(attrs={'class':'', 'id':'personPix', 'data-default-file':'../../static/img/default-user.jpg', 'data-max-file-size':'2M', 'type':'file'}),
            'bio': forms.Textarea(attrs={'id':'bio', 'placeholder':'bio', 'rows':'3', 'maxlength': '150'}),
        }


class UserProfileForm(ModelForm):
    class Meta:
        model = CustomUserProfile
        # fields = ['email', 'first_name', 'last_name', 'password']
        fields = '__all__'
        widgets = {

        'tertiary_school2_year': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
        'tertiary_school1_year': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
        'secondary_school_year': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
        'primary_school_year': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
    }

    


