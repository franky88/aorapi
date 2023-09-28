# Generated by Django 4.2.5 on 2023-09-28 09:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aormobile', '0044_alter_snstopicsubscription_endpoint_arn'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduleInvitation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200)),
                ('invitation_type', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aormobile.business')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ScheduleInvitationDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('days', models.JSONField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('schedule_invitation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aormobile.scheduleinvitation')),
            ],
        ),
        migrations.CreateModel(
            name='ScheduleInvitationDateStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=200)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('schedule_invitation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aormobile.scheduleinvitation')),
                ('schedule_invitation_date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aormobile.scheduleinvitationdate')),
            ],
        ),
    ]