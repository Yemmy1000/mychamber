import os
import logging
from django.db import models
from django.urls import reverse
# from django.contrib.auth.models import User
from base.models import CustomUser, CustomUserProfile
from contact.models import cPerson
from base.widgets import DatePickerInput, TimePickerInput, DateTimePickerInput
from django.utils.timezone import now as timezone_now
from django.utils.translation import gettext_lazy as _
from component.country import COUNTRY
from component.stateGov import STATE_GOV
import uuid, string, random
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey, TreeManyToManyField

# def upload_to(instance, filename):
#     now = timezone_now()
#     filename_base, filename_ext = os.path.splitext(filename)
#     return "file/%s%s" % (
#         now.strftime("%Y/%m/%Y%m%d%H%M%S"),
#         filename_ext.lower(),
#     )
def upload_to(instance, filename):
    now = timezone_now()
    filename_base, filename_ext = os.path.splitext(filename)
    return "file/%s%s%s%s" % (
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


def file_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def file_generator2():
    myStr = str(uuid.uuid4())[0:7] 
    return myStr.upper()


class MatterInfo(models.Model):
    file_no: str = models.CharField('File Number', primary_key=True, max_length=200, default=file_generator2)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    client_contact = models.ForeignKey(cPerson, related_name='matter_info', on_delete=models.CASCADE, null=True)
    claim_no: str = models.CharField('Claim Number', max_length=200, blank=True)
    title: str = models.CharField('Subject Matter', max_length=200)


    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self) -> str:
        return self.file_no

    def get_absolute_url(self):
        return reverse('matter_detail',
                       args=[self.file_no])

class MatterAttorney(models.Model):
    file_no = models.ForeignKey(MatterInfo, on_delete=models.CASCADE, null=True, related_name='matterInfo')
    referrer = models.ForeignKey(CustomUserProfile, on_delete=models.CASCADE, null=True, blank=True, related_name='referrer')
    originating_attorney = models.ForeignKey(CustomUserProfile, on_delete=models.CASCADE, null=True, blank=True, related_name='originating_attorney')
    supervising_attorney = models.ForeignKey(CustomUserProfile, on_delete=models.CASCADE, null=True, blank=True, related_name='supervising_attorney')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self) -> str:
        return "%s" % (self.id)

class MatterConflictOtherParty(models.Model):
    id_no = models.AutoField(primary_key=True)
    file_no = models.ForeignKey(MatterInfo, on_delete=models.CASCADE, null=True)
    # other_party: str = models.ForeignKey(cPerson, on_delete=models.CASCADE, null=True)
    # adverse_party: str = models.CharField('Status', max_length=200, blank=True)
    other_party_relationship: str = models.CharField('Relationship', max_length=200, blank=True)
    other_party: str = models.ForeignKey(cPerson, on_delete=models.CASCADE, null=True, blank=True)
    # other_party = models.CharField(
    #     max_length=20,
    #     choices=get_person(),
    #     null=True, blank=True
    # )
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self) -> str:
        return "%s" % (self.id_no)

class MatterConflictAdverseParty(models.Model):
    id_no = models.AutoField(primary_key=True)
    file_no = models.ForeignKey(MatterInfo, on_delete=models.CASCADE, null=True)
    adverse_party: str = models.ForeignKey(cPerson, on_delete=models.CASCADE, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self) -> str:
        return self.file_no

class MatterConflictAssocFile(models.Model):
    id_no = models.AutoField(primary_key=True)
    file_no = models.ForeignKey(MatterInfo, on_delete=models.CASCADE, null=True)    
    associated_other_files: str = models.CharField('Relationship', max_length=200, blank=True)    
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self) -> str:
        return self.file_no        

class MatterDocument(models.Model):
    file_no = models.ForeignKey(MatterInfo, on_delete=models.CASCADE, null=True)
    writ_of_summon = models.ImageField('', null=True, blank=True, upload_to=upload_to)
    statement_of_claim = models.ImageField('', null=True, blank=True, upload_to=upload_to)
    witness_statement_on_oath = models.ImageField('', null=True, blank=True, upload_to=upload_to)
    affidavit = models.ImageField('', null=True, blank=True, upload_to=upload_to)
    motion_exparte = models.ImageField('', null=True, blank=True, upload_to=upload_to)
    statement_of_defense = models.ImageField('', null=True, blank=True, upload_to=upload_to)
    motion_on_notice = models.ImageField('', null=True, blank=True, upload_to=upload_to)
    reply_doc = models.ImageField('', null=True, blank=True, upload_to=upload_to)
    written_address = models.ImageField('', null=True, blank=True, upload_to=upload_to)
    
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']
        verbose_name = ("Document Documents")
        verbose_name_plural = ("Document Documents")

    def __str__(self) -> str:
        return "%s" % (self.id)

class MatterSample(models.Model):
    CATEGORY = [
        ('Civil', 'Civil'),
        ('Criminal', 'Criminal'),              
    ]
    # parent = TreeForeignKey("self", blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField("Title", max_length=200)
    # category = models.CharField("Matter Category", max_length=200)
    category = models.CharField(
        "Matter Category",
        max_length=20,
        choices=CATEGORY,
        null=True,
        blank=False,
    )
    description = models.TextField('Matter Category Description', null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        # ordering = ["tree_id", "lft"]
        verbose_name = ("Matter sample")
        verbose_name_plural = ("Matter samples")

    def __str__(self):
        return self.title

class CivilMatterSample(models.Model):
    title = models.CharField("Title", max_length=200)
    description = models.TextField('Matter Category Description', null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        # ordering = ["tree_id", "lft"]
        verbose_name = ("Civil Matter sample")
        verbose_name_plural = ("Civil Matter samples")

    def __str__(self):
        return self.title

class CriminalMatterSample(models.Model):
    title = models.CharField("Title", max_length=200)
    description = models.TextField('Matter Category Description', null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        # ordering = ["tree_id", "lft"]
        verbose_name = ("Criminal Matter sample")
        verbose_name_plural = ("Criminal Matter samples")

    def __str__(self):
        return self.title

class MatterNature(models.Model):
    id_no = models.AutoField(primary_key=True)
    file_no = models.ForeignKey(MatterInfo, on_delete=models.CASCADE, null=True)
    # category: str = models.CharField('Category', max_length=200, blank=True)
    # cases: str = models.CharField('Cases', max_length=200, null=True, blank=True)
    # cases_selected = models.ForeignKey(MatterSample, on_delete=models.CASCADE, null=True)
    cases_selected = models.ManyToManyField(MatterSample, verbose_name="Cases Selected", blank=True)
    # categories = TreeManyToManyField(MatterSample, verbose_name="Matter sample")
    # status: str = models.CharField('Status', max_length=200, blank=True)
    
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']
        verbose_name = ("Matter nature")
        verbose_name_plural = ("Matter natures")

    def __str__(self) -> str:
        return str(self.cases_selected)

class MatterCivilNature(models.Model):
    id_no = models.AutoField(primary_key=True)
    file_no = models.ForeignKey(MatterInfo, on_delete=models.CASCADE)
    cases = models.ManyToManyField(CivilMatterSample, verbose_name="Civil Cases Selected", blank=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']
        verbose_name = ("Civil Matter nature")
        verbose_name_plural = ("Civil Matter natures")

    def __str__(self) -> str:
        return str(self.id_no)

class MatterCriminalNature(models.Model):
    id_no = models.AutoField(primary_key=True)
    file_no = models.ForeignKey(MatterInfo, on_delete=models.CASCADE)
    cases = models.ManyToManyField(CriminalMatterSample, verbose_name="Criminal Cases Selected", blank=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']
        verbose_name = ("Criminal Matter nature")
        verbose_name_plural = ("Criminal Matter natures")

    def __str__(self) -> str:
        return str(self.id_no)

class MatterDescription(models.Model):
    file_no = models.ForeignKey(MatterInfo, on_delete=models.CASCADE, null=True)
    description = models.TextField('Case Summary', null=True, blank=True)
    
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Case Summary")
        verbose_name_plural = ("Case Summary")

    def __str__(self) -> str:
        return self.description

class UpdateLog(models.Model):
    file_no = models.ForeignKey(MatterInfo, on_delete=models.CASCADE, null=True, db_index=True, related_name='update_log')
    section = models.CharField('section', max_length=250, blank=True)
    update_date = models.DateField('Update date', null=True, blank=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self) -> str:
        return "%s" % (self.id)

class AssignedTo(models.Model):
    file_no = models.ForeignKey(MatterInfo, on_delete=models.CASCADE, null=True, db_index=True, related_name='assignee')
    personnel = models.ForeignKey(CustomUser, on_delete=models.CASCADE, db_index=True, null=True)
    current = models.BooleanField('Current Assignee', null=True, blank=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self) -> str:
        return "%s" % (self.id)


class ClientType(models.Model):
    CLIENT_TYPE = [
        ('Claimant', 'Claimant'),
        ('Defendant', 'Defendant'), 
        ('Respondent', 'Respondent'),
        ('Appellant', 'Appellant'),
        ('Others', 'Others'),              
    ]
    file_no = models.ForeignKey(MatterInfo, on_delete=models.CASCADE, null=True, related_name='client_type')
    client_type = models.CharField(
        max_length=20,
        choices=CLIENT_TYPE,
        null=True, blank=True
    )
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self) -> str:
        return "%s" % (self.id)


class SupportingDocument(models.Model):
    file_no = models.ForeignKey(MatterInfo, on_delete=models.CASCADE, null=True, db_index=True)
    client_type = models.ForeignKey(ClientType, on_delete=models.CASCADE, null=True)
    document_type = models.CharField(_('Document Type'), max_length=250, blank=True)
    document = models.ImageField(_('Document'), null=True, blank=True, upload_to=upload_to)
    
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']
        verbose_name = ("Document Documents")
        verbose_name_plural = ("Document Documents")

    def __str__(self) -> str:
        return "%s" % (self.id)