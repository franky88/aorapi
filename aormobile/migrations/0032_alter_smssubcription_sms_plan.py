# Generated by Django 4.2.5 on 2023-09-28 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aormobile', '0031_smssubcription_chargebee_plan_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smssubcription',
            name='sms_plan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aormobile.smsplan'),
        ),
    ]
