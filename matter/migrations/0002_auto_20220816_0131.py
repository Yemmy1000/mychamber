# Generated by Django 2.2.28 on 2022-08-16 00:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import matter.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('matter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_type', models.CharField(blank=True, choices=[('Claimant', 'Claimant'), ('Defendant', 'Defendant'), ('Respondent', 'Respondent'), ('Appellant', 'Appellant'), ('Others', 'Others')], max_length=20, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-updated', '-created'],
            },
        ),
        migrations.AlterModelOptions(
            name='civilmattersample',
            options={'verbose_name': 'Civil Matter sample', 'verbose_name_plural': 'Civil Matter samples'},
        ),
        migrations.AlterModelOptions(
            name='matterdescription',
            options={'verbose_name': 'Case Summary', 'verbose_name_plural': 'Case Summary'},
        ),
        migrations.AlterField(
            model_name='matterdescription',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Case Summary'),
        ),
        migrations.AlterField(
            model_name='matterinfo',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Subject Matter'),
        ),
        migrations.CreateModel(
            name='UpdateLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(blank=True, max_length=250, verbose_name='section')),
                ('update_date', models.DateField(blank=True, null=True, verbose_name='Update date')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('file_no', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='update_log', to='matter.MatterInfo')),
            ],
            options={
                'ordering': ['-updated', '-created'],
            },
        ),
        migrations.CreateModel(
            name='SupportingDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_type', models.CharField(blank=True, max_length=250, verbose_name='Document Type')),
                ('document', models.ImageField(blank=True, null=True, upload_to=matter.models.upload_to, verbose_name='Document')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('client_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='matter.ClientType')),
                ('file_no', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='matter.MatterInfo')),
            ],
            options={
                'verbose_name': 'Document Documents',
                'verbose_name_plural': 'Document Documents',
                'ordering': ['-updated', '-created'],
            },
        ),
        migrations.AddField(
            model_name='clienttype',
            name='file_no',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_type', to='matter.MatterInfo'),
        ),
        migrations.CreateModel(
            name='AssignedTo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current', models.BooleanField(blank=True, null=True, verbose_name='Current Assignee')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('file_no', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assignee', to='matter.MatterInfo')),
                ('personnel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-updated', '-created'],
            },
        ),
    ]