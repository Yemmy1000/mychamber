# Generated by Django 2.2.28 on 2022-09-16 19:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('matter', '0007_auto_20220826_2015'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('category', models.CharField(blank=True, choices=[('Personal', 'Personal'), ('Official', 'Official'), ('Business', 'Business')], default='Official', max_length=12, null=True, verbose_name='Category')),
                ('priority', models.CharField(blank=True, choices=[('Urgent', 'Urgent'), ('Important', 'Important'), ('Normal', 'Normal')], default='Normal', max_length=12, null=True, verbose_name='Priority')),
                ('status', models.CharField(blank=True, choices=[('Closed', 'Closed'), ('Ongoing', 'Ongoing'), ('Scheduled', 'Scheduled')], default='Scheduled', max_length=12, null=True, verbose_name='Status')),
                ('start', models.DateField(blank=True, null=True, verbose_name='Start Date')),
                ('start_time', models.TimeField(blank=True, null=True, verbose_name='Start Time')),
                ('end', models.DateField(blank=True, null=True, verbose_name='End Date')),
                ('end_time', models.TimeField(blank=True, null=True, verbose_name='End Time')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_event_set', to=settings.AUTH_USER_MODEL)),
                ('matter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='matter_info', to='matter.MatterInfo')),
            ],
            options={
                'ordering': ['-updated', '-created'],
            },
        ),
        migrations.CreateModel(
            name='event_participants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_event', to='event.Event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='participant',
            field=models.ManyToManyField(blank=True, through='event.event_participants', to=settings.AUTH_USER_MODEL),
        ),
    ]