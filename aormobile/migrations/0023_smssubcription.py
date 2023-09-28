# Generated by Django 4.2.5 on 2023-09-28 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aormobile', '0022_rename_capasity_smsplan_capacity_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SMSSubcription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credits', models.FloatField()),
                ('fee_per_message', models.FloatField(default=0.7)),
                ('is_active', models.BooleanField(default=True)),
                ('is_renewal', models.BooleanField(default=False)),
                ('is_upgrade', models.BooleanField(default=False)),
                ('is_downgrade', models.BooleanField(default=False)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aormobile.business')),
                ('sms_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aormobile.smsplan')),
            ],
        ),
    ]