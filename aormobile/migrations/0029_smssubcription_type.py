# Generated by Django 4.2.5 on 2023-09-28 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aormobile', '0028_smsrate'),
    ]

    operations = [
        migrations.AddField(
            model_name='smssubcription',
            name='type',
            field=models.CharField(default='topup', max_length=100),
        ),
    ]
