# Generated by Django 4.2.5 on 2023-09-28 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aormobile', '0041_mobilemessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessreview',
            name='is_read',
            field=models.BooleanField(default=False),
        ),
    ]
