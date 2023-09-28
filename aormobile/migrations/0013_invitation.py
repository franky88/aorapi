# Generated by Django 4.2.5 on 2023-09-28 06:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aormobile', '0012_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('invitation_type', models.CharField(choices=[('Single', 'single'), ('Bulk', 'bulk')], default='single', max_length=20)),
                ('batch', models.IntegerField(blank=True, null=True)),
                ('status', models.BooleanField(default=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('business', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aormobile.business')),
                ('message_template', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aormobile.messagetemplate')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]