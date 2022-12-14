# Generated by Django 2.2.28 on 2022-07-30 13:03

import base.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('password', models.CharField(max_length=200, verbose_name='password')),
                ('user_type', models.CharField(blank=True, max_length=200, null=True, verbose_name='User type')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CustomUserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=200, verbose_name='Last Name')),
                ('bio', models.TextField(blank=True, null=True, verbose_name='Short biography')),
                ('dob', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('address', models.CharField(blank=True, max_length=200, null=True, verbose_name='Last Name')),
                ('designation', models.CharField(blank=True, max_length=200, null=True, verbose_name='Designation')),
                ('phone', models.CharField(blank=True, max_length=200, null=True, verbose_name='Phone 1')),
                ('email2', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Alternate email')),
                ('avatar', models.ImageField(blank=True, default='avatar.svg', null=True, upload_to=base.models.upload_to, verbose_name='Avatar')),
                ('primary_school', models.CharField(blank=True, max_length=200, null=True, verbose_name='Primary school')),
                ('primary_school_year', models.DateField(blank=True, null=True, verbose_name='Grad Year')),
                ('secondary_school', models.CharField(blank=True, max_length=200, null=True, verbose_name='Secondary school')),
                ('secondary_school_year', models.DateField(blank=True, null=True, verbose_name='Grad Year')),
                ('tertiary_school1', models.CharField(blank=True, max_length=200, null=True, verbose_name='Tertiary school1')),
                ('tertiary_school1_year', models.DateField(blank=True, null=True, verbose_name='Grad Year')),
                ('tertiary_school2', models.CharField(blank=True, max_length=200, null=True, verbose_name='Tertiary School2')),
                ('tertiary_school2_year', models.DateField(blank=True, null=True, verbose_name='Grad Year')),
                ('others', models.CharField(blank=True, max_length=200, null=True, verbose_name='others')),
                ('sex', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=12, null=True)),
                ('marital_status', models.CharField(blank=True, choices=[('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced'), ('Widow', 'Widow'), ('Widower', 'Widower')], max_length=20, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
