# Generated by Django 4.2.5 on 2023-09-28 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aormobile', '0016_alter_businessindustry_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='messagetemplate',
            name='message_type',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
