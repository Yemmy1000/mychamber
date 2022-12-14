# Generated by Django 2.2.28 on 2022-07-30 13:03

import contact.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='cPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=200, verbose_name='First Name')),
                ('familyName', models.CharField(max_length=200, verbose_name='Family Name')),
                ('otherName', models.CharField(blank=True, max_length=200, verbose_name='Other Name')),
                ('sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=12)),
                ('maritalStatus', models.CharField(choices=[('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced'), ('Widow', 'Widow'), ('Widower', 'Widower')], max_length=20)),
                ('dob', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('personPix', models.ImageField(blank=True, null=True, upload_to=contact.models.upload_to, verbose_name='')),
                ('homeAddress', models.CharField(blank=True, max_length=200, null=True, verbose_name='Home Address')),
                ('homeState', models.CharField(blank=True, choices=[('Abia', 'Abia'), ('Adamawa', 'Adamawa'), ('Akwa-Ibom', 'Akwa-Ibom'), ('Anambra', 'Anambra'), ('Bauchi', 'Bauchi'), ('Bayelsa', 'Bayelsa'), ('Benue', 'Benue'), ('Borno', 'Borno'), ('Cross-River', 'Cross-River'), ('Delta', 'Delta'), ('Ebonyi', 'Ebonyi'), ('Edo', 'Edo'), ('Ekiti', 'Ekiti'), ('Enugu', 'Enugu'), ('FCT-Abuja', 'FCT-Abuja'), ('Gombe', 'Gombe'), ('Imo', 'Imo'), ('Jigawa', 'Jigawa'), ('Kaduna', 'Kaduna'), ('Kano', 'Kano'), ('Katsina', 'Katsina'), ('Kebbi', 'Kebbi'), ('Kogi', 'Kogi'), ('Kwara', 'Kwara'), ('Lagos', 'Lagos'), ('Nasarawa', 'Nasarawa'), ('Niger', 'Niger'), ('Ogun', 'Ogun'), ('Ondo', 'Ondo'), ('Osun', 'Osun'), ('Oyo', 'Oyo'), ('Plateau', 'Plateau'), ('Rivers', 'Rivers'), ('Sokoto', 'Sokoto'), ('Taraba', 'Taraba'), ('Yobe', 'Yobe'), ('Zamfara', 'Zamfara')], max_length=20, null=True)),
                ('homeCountry', models.CharField(blank=True, choices=[('Nigeria', 'Nigeria'), ('Ghana', 'Ghana')], max_length=20, null=True)),
                ('contactAddress', models.CharField(blank=True, max_length=200, null=True, verbose_name='Contact Address')),
                ('contactState', models.CharField(blank=True, choices=[('Abia', 'Abia'), ('Adamawa', 'Adamawa'), ('Akwa-Ibom', 'Akwa-Ibom'), ('Anambra', 'Anambra'), ('Bauchi', 'Bauchi'), ('Bayelsa', 'Bayelsa'), ('Benue', 'Benue'), ('Borno', 'Borno'), ('Cross-River', 'Cross-River'), ('Delta', 'Delta'), ('Ebonyi', 'Ebonyi'), ('Edo', 'Edo'), ('Ekiti', 'Ekiti'), ('Enugu', 'Enugu'), ('FCT-Abuja', 'FCT-Abuja'), ('Gombe', 'Gombe'), ('Imo', 'Imo'), ('Jigawa', 'Jigawa'), ('Kaduna', 'Kaduna'), ('Kano', 'Kano'), ('Katsina', 'Katsina'), ('Kebbi', 'Kebbi'), ('Kogi', 'Kogi'), ('Kwara', 'Kwara'), ('Lagos', 'Lagos'), ('Nasarawa', 'Nasarawa'), ('Niger', 'Niger'), ('Ogun', 'Ogun'), ('Ondo', 'Ondo'), ('Osun', 'Osun'), ('Oyo', 'Oyo'), ('Plateau', 'Plateau'), ('Rivers', 'Rivers'), ('Sokoto', 'Sokoto'), ('Taraba', 'Taraba'), ('Yobe', 'Yobe'), ('Zamfara', 'Zamfara')], max_length=20, null=True)),
                ('contactCountry', models.CharField(blank=True, choices=[('Nigeria', 'Nigeria'), ('Ghana', 'Ghana')], max_length=20, null=True)),
                ('nationality', models.CharField(max_length=200, verbose_name='Nationality')),
                ('language', models.CharField(blank=True, max_length=200, null=True, verbose_name='Language')),
                ('firstPhone', models.CharField(max_length=15, unique=True, verbose_name='First Phone')),
                ('secondPhone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Second Phone')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='Email')),
                ('website', models.URLField(blank=True, null=True, verbose_name='Website')),
                ('companyName', models.CharField(blank=True, max_length=200, null=True, verbose_name='Company Name')),
                ('companyAddress', models.CharField(blank=True, max_length=200, null=True, verbose_name='Company Address')),
                ('companyPhone', models.CharField(blank=True, max_length=200, verbose_name='Company Phone')),
                ('jobTitle', models.CharField(blank=True, max_length=200, null=True, verbose_name='Job Title')),
                ('companyEmail', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Company Email')),
                ('companyWebsite', models.URLField(blank=True, null=True, verbose_name='Company Website')),
                ('companyDescription', models.TextField(blank=True, verbose_name='Company Description')),
                ('highestEducation', models.CharField(blank=True, max_length=200, verbose_name='Highest Education')),
                ('schoolName', models.CharField(blank=True, max_length=500, verbose_name='School Name')),
                ('dateGraduated', models.DateField(blank=True, null=True, verbose_name='Date Graduated')),
                ('educationDescription', models.TextField(blank=True, verbose_name='Education Description')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Person Contact',
                'verbose_name_plural': 'Person Contacts',
                'ordering': ['-updated', '-created'],
            },
        ),
        migrations.CreateModel(
            name='cCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyName', models.CharField(max_length=200, verbose_name='Company Name')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-updated', '-created'],
            },
        ),
    ]
