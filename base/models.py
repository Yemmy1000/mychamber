import os
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
# from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from .managers import CustomUserManager
from django.utils.timezone import now as timezone_now



# class User(AbstractUser):
#     firstname = models.CharField(max_length=200, null=True)
#     lastname = models.CharField(max_length=200, null=True)

def upload_to(instance, filename):
    now = timezone_now()
    filename_base, filename_ext = os.path.splitext(filename)
    return "user/%s%s%s%s" % (
        now.strftime("%Y/%m/"),
        filename_base.replace(" ", "_").lower()+"_",
        now.strftime("%d%H%M%S"),
        filename_ext.lower(),
    )


class CustomUser(AbstractUser):
    username = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('First Name'), max_length=200)
    last_name = models.CharField(_('Last Name'), max_length=200)
    bio = models.TextField(_('Short biography'), null=True, blank=True)
    dob = models.DateField(_('Date of Birth'), null=True, blank=True)
    phone = models.CharField(_('Phone 1'), max_length=200, null=True, blank=True)
    avatar = models.ImageField(_('Avatar'), null=True, blank=True, default="avatar.svg", upload_to=upload_to)
    password = models.CharField(_('password'), max_length=200)
    user_type = models.CharField(_('User type'), max_length=200, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class CustomUserProfile(models.Model):
    MARITAL_STATUS = [
        ('Single', 'Single'),
        ('Married', 'Married'), 
        ('Divorced', 'Divorced'),
        ('Widow', 'Widow'),
        ('Widower', 'Widower'),              
    ]

    SEX = [
        ('Male', 'Male'),
        ('Female', 'Female'),             
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_profile', db_index=True, on_delete=models.CASCADE)
    other_name = models.CharField(_('Other Name'), max_length=200, null=True, blank=True)
    address = models.CharField(_('Home Address'), max_length=200, null=True, blank=True)
    designation = models.CharField(_('Designation'), max_length=200, null=True, blank=True)
    email2 = models.EmailField(_('Alternate email'), null=True, blank=True)
    primary_school = models.CharField(_('Primary school'), max_length=200, null=True, blank=True)
    primary_school_year = models.DateField(_('Grad Year'), null=True, blank=True)
    secondary_school = models.CharField(_('Secondary school'), max_length=200, null=True, blank=True)
    secondary_school_year = models.DateField(_('Grad Year'), null=True, blank=True)
    tertiary_school1 = models.CharField(_('Tertiary school1'), max_length=200, null=True, blank=True)
    tertiary_school1_year = models.DateField(_('Grad Year'), null=True, blank=True)
    tertiary_school2 = models.CharField(_('Tertiary School2'), max_length=200, null=True, blank=True)
    tertiary_school2_year = models.DateField(_('Grad Year'), null=True, blank=True)
    others = models.CharField(_('others'), max_length=200, null=True, blank=True)

    sex = models.CharField(
        max_length=12,
        choices=SEX,
        null=True, blank=True
    )
    marital_status = models.CharField(
        max_length=20,
        choices=MARITAL_STATUS,
        null=True, blank=True
    )
    def get_absolute_url(self):
        return reverse('users:detail', args=[self.id, self.slug])

    def __str__(self) -> str:
        return "%s" % (self.user)


