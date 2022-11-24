import os
import logging
from django.db import models
# from django.contrib.auth.models import User
from base.models import CustomUser
from .widgets import DatePickerInput, TimePickerInput, DateTimePickerInput
from django.utils.timezone import now as timezone_now
from component.country import COUNTRY
from component.stateGov import STATE_GOV


# def upload_to(instance, filename):
#     now = timezone_now()
#     filename_base, filename_ext = os.path.splitext(filename)
#     return "image/%s%s" % (
#         now.strftime("%Y/%m/%Y%m%d%H%M%S"),
#         filename_ext.lower(),
#     )
def upload_to(instance, filename):
    now = timezone_now()
    filename_base, filename_ext = os.path.splitext(filename)
    return "client/%s%s%s%s" % (
        now.strftime("%Y/%m/"),
        filename_base.replace(" ", "_").lower()+"_",
        now.strftime("%d%H%M%S"),
        filename_ext.lower(),
    )

def get_person():
    Person = cPerson.objects.all()
    p_list = []
    for person in Person:
        a = (str(person.id), person.familyName +' '+person.firstName)
        p_list.append(a)      

    return p_list

class cPerson(models.Model):
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
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    firstName: str = models.CharField('First Name', max_length=200)
    familyName: str = models.CharField('Family Name', max_length=200)
    otherName: str = models.CharField('Other Name', max_length=200, blank=True)
    sex = models.CharField(
        max_length=12,
        choices=SEX,
        null=True, blank=True
    )
    maritalStatus = models.CharField(
        max_length=20,
        choices=MARITAL_STATUS,
        null=True, blank=True
    )
    dob = models.DateField('Date of Birth', null=True, blank=True)
    personPix = models.ImageField('', null=True, blank=True, default="client/client.jpg", upload_to=upload_to)
    homeAddress = models.CharField('Home Address', null=True, max_length=200, blank=True)
    # homeState: str = models.CharField('Home State', null=True, blank=True, max_length=200)
    homeState = models.CharField(
        max_length=20,
        choices=STATE_GOV,
        null=True,
        blank=True,
    )
    homeCountry = models.CharField(
        max_length=20,
        choices=COUNTRY,
        null=True,
        blank=True,
    )
    # homeCountry: str = models.CharField('Home Country', null=True, blank=True, max_length=200)
    contactAddress = models.CharField('Contact Address', null=True, blank=True, max_length=200)
    # contactState: str = models.CharField('Contact State', null=True, blank=True, max_length=200)
    contactState = models.CharField(
        max_length=20,
        choices=STATE_GOV,
        null=True, 
        blank=True,
    )
    # contactCountry: str = models.CharField('Contact Country', null=True, blank=True, max_length=200)
    contactCountry = models.CharField(
        max_length=20,
        choices=COUNTRY,
        null=True, 
        blank=True,
    )
    nationality: str = models.CharField('Nationality', blank=True, max_length=200)    
    language = models.CharField('Language', null=True, blank=True, max_length=200)
    firstPhone = models.CharField('First Phone', blank=True, null=True, max_length=15)
    secondPhone = models.CharField('Second Phone', null=True, blank=True, max_length=15) 
    email = models.EmailField('Email', unique=True, null=True, blank=True)
    website = models.URLField('Website',  null=True, blank=True)   
    companyName: str = models.CharField('Company Name', null=True, blank=True, max_length=200)
    companyAddress: str = models.CharField('Company Address', null=True, blank=True, max_length=200)
    companyPhone: str = models.CharField('Company Phone', max_length=200, blank=True)
    jobTitle: str = models.CharField('Job Title', null=True, blank=True, max_length=200)
    companyEmail = models.EmailField('Company Email', null=True, blank=True)
    companyWebsite = models.URLField('Company Website', null=True, blank=True) 
    companyDescription = models.TextField('Company Description', null=False, blank=True)
    highestEducation: str = models.CharField('Highest Education', max_length=200, blank=True)
    schoolName: str = models.CharField('School Name', max_length=500, blank=True)
    dateGraduated = models.DateField('Date Graduated', null=True, blank=True)
    educationDescription = models.TextField('Education Description', null=False, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']
        verbose_name = ("Person Contact")
        verbose_name_plural = ("Person Contacts")

    def __str__(self) -> str:
        return "%s %s %s " % (self.familyName, self.firstName, self.otherName)


class cCompany(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    companyName: str = models.CharField('Company Name', max_length=200)
    # dateFounded = models.DateField('Date Founded', null=True, blank=True)
    # specialization: str = models.CharField('Specialization', max_length=200)
    # numberOfStaff: str = models.PositiveIntegerField('Number of Staff', blank=True)
    # companyLogo = models.ImageField('', null=True, blank=True, upload_to=upload_to)
    # cacRegNo = models.CharField('CAC Reg. No.', null=True, max_length=200, blank=True)
    # taxID = models.CharField('Tax ID', null=True, max_length=200, blank=True)
    # companyActivityDescription = models.TextField('Description of Company Activities', null=False, blank=True)
    # officeAddress = models.CharField('Office Address', null=True, max_length=200, blank=True)
    # # homeState: str = models.CharField('Home State', null=True, blank=True, max_length=200)
    # companyState = models.CharField(
    #     max_length=20,
    #     choices=STATE_GOV,
    # )
    # companyCountry = models.CharField(
    #     max_length=20,
    #     choices=COUNTRY,
    # )
    # firstPhone = models.CharField('First Phone', max_length=15)
    # secondPhone = models.CharField('Second Phone', max_length=15, null=True, blank=True) 
    # email = models.EmailField('Email', unique=True, null=True, blank=True)
    # website = models.URLField('Website', unique=True, null=True, blank=True)   
    # firstRepresentative = models.ForeignKey(cPerson, on_delete=models.CASCADE, null=True)
    # secondRepresentative = models.ForeignKey(secondRep, on_delete=models.CASCADE, null=True, blank=True)
    # thirdRepresentative = models.ForeignKey(thirdRep, on_delete=models.CASCADE, null=True, blank=True)
    # secondRepresentative: str = models.CharField('Second Representative', max_length=200, null=True, blank=True)
    # thirdRepresentative: str = models.CharField('Third Representative', max_length=200, null=True, blank=True)
    
    # secondRepresentative = models.CharField(
    #     max_length=20,
    #     choices=get_person(),
    #     null=True, blank=True
    # )
    # thirdRepresentative = models.CharField(
    #     max_length=20,
    #     choices=get_person(),
    #     null=True, blank=True
    # )
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self) -> str:
        return self.companyName