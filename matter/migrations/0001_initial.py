# Generated by Django 2.2.28 on 2022-07-30 13:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import matter.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contact', '0001_initial'),
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CivilMatterSample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Matter Category Description')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Matter sample',
                'verbose_name_plural': 'Matter samples',
            },
        ),
        migrations.CreateModel(
            name='CriminalMatterSample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Matter Category Description')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Criminal Matter sample',
                'verbose_name_plural': 'Criminal Matter samples',
            },
        ),
        migrations.CreateModel(
            name='MatterInfo',
            fields=[
                ('file_no', models.CharField(default=matter.models.file_generator2, max_length=200, primary_key=True, serialize=False, verbose_name='File Number')),
                ('claim_no', models.CharField(blank=True, max_length=200, verbose_name='Claim Number')),
                ('title', models.CharField(max_length=200, verbose_name='Title of Matter')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('client_contact', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='matter_info', to='contact.cPerson')),
            ],
            options={
                'ordering': ['-updated', '-created'],
            },
        ),
        migrations.CreateModel(
            name='MatterSample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('category', models.CharField(choices=[('Civil', 'Civil'), ('Criminal', 'Criminal')], max_length=20, null=True, verbose_name='Matter Category')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Matter Category Description')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Matter sample',
                'verbose_name_plural': 'Matter samples',
            },
        ),
        migrations.CreateModel(
            name='MatterNature',
            fields=[
                ('id_no', models.AutoField(primary_key=True, serialize=False)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('cases_selected', models.ManyToManyField(blank=True, to='matter.MatterSample', verbose_name='Cases Selected')),
                ('file_no', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='matter.MatterInfo')),
            ],
            options={
                'verbose_name': 'Matter nature',
                'verbose_name_plural': 'Matter natures',
                'ordering': ['-updated', '-created'],
            },
        ),
        migrations.CreateModel(
            name='MatterDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writ_of_summon', models.ImageField(blank=True, null=True, upload_to=matter.models.upload_to, verbose_name='')),
                ('statement_of_claim', models.ImageField(blank=True, null=True, upload_to=matter.models.upload_to, verbose_name='')),
                ('witness_statement_on_oath', models.ImageField(blank=True, null=True, upload_to=matter.models.upload_to, verbose_name='')),
                ('affidavit', models.ImageField(blank=True, null=True, upload_to=matter.models.upload_to, verbose_name='')),
                ('motion_exparte', models.ImageField(blank=True, null=True, upload_to=matter.models.upload_to, verbose_name='')),
                ('statement_of_defense', models.ImageField(blank=True, null=True, upload_to=matter.models.upload_to, verbose_name='')),
                ('motion_on_notice', models.ImageField(blank=True, null=True, upload_to=matter.models.upload_to, verbose_name='')),
                ('reply_doc', models.ImageField(blank=True, null=True, upload_to=matter.models.upload_to, verbose_name='')),
                ('written_address', models.ImageField(blank=True, null=True, upload_to=matter.models.upload_to, verbose_name='')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('file_no', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='matter.MatterInfo')),
            ],
            options={
                'verbose_name': 'Document Documents',
                'verbose_name_plural': 'Document Documents',
                'ordering': ['-updated', '-created'],
            },
        ),
        migrations.CreateModel(
            name='MatterDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Matter Description')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('file_no', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='matter.MatterInfo')),
            ],
            options={
                'verbose_name': 'Matter description',
                'verbose_name_plural': 'Matter descriptions',
            },
        ),
        migrations.CreateModel(
            name='MatterCriminalNature',
            fields=[
                ('id_no', models.AutoField(primary_key=True, serialize=False)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('cases', models.ManyToManyField(to='matter.CriminalMatterSample', verbose_name='Criminal Cases Selected')),
                ('file_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matter.MatterInfo')),
            ],
            options={
                'verbose_name': 'Criminal Matter nature',
                'verbose_name_plural': 'Criminal Matter natures',
                'ordering': ['-updated', '-created'],
            },
        ),
        migrations.CreateModel(
            name='MatterConflictOtherParty',
            fields=[
                ('id_no', models.AutoField(primary_key=True, serialize=False)),
                ('other_party_relationship', models.CharField(blank=True, max_length=200, verbose_name='Relationship')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('file_no', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='matter.MatterInfo')),
                ('other_party', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contact.cPerson')),
            ],
            options={
                'ordering': ['-updated', '-created'],
            },
        ),
        migrations.CreateModel(
            name='MatterConflictAssocFile',
            fields=[
                ('id_no', models.AutoField(primary_key=True, serialize=False)),
                ('associated_other_files', models.CharField(blank=True, max_length=200, verbose_name='Relationship')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('file_no', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='matter.MatterInfo')),
            ],
            options={
                'ordering': ['-updated', '-created'],
            },
        ),
        migrations.CreateModel(
            name='MatterConflictAdverseParty',
            fields=[
                ('id_no', models.AutoField(primary_key=True, serialize=False)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('adverse_party', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contact.cPerson')),
                ('file_no', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='matter.MatterInfo')),
            ],
            options={
                'ordering': ['-updated', '-created'],
            },
        ),
        migrations.CreateModel(
            name='MatterCivilNature',
            fields=[
                ('id_no', models.AutoField(primary_key=True, serialize=False)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('cases', models.ManyToManyField(to='matter.CivilMatterSample', verbose_name='Civil Cases Selected')),
                ('file_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matter.MatterInfo')),
            ],
            options={
                'verbose_name': 'Civil Matter nature',
                'verbose_name_plural': 'Civil Matter natures',
                'ordering': ['-updated', '-created'],
            },
        ),
        migrations.CreateModel(
            name='MatterAttorney',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('file_no', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='matterInfo', to='matter.MatterInfo')),
                ('originating_attorney', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='originating_attorney', to='base.CustomUserProfile')),
                ('referrer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='referrer', to='base.CustomUserProfile')),
                ('supervising_attorney', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='supervising_attorney', to='base.CustomUserProfile')),
            ],
            options={
                'ordering': ['-updated', '-created'],
            },
        ),
    ]
