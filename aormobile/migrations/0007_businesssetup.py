# Generated by Django 4.2.5 on 2023-09-28 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aormobile', '0006_business_timestamp_businesscontent_timestamp_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessSetup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('tagline', models.CharField(blank=True, max_length=200, null=True)),
                ('logo', models.CharField(blank=True, max_length=200, null=True)),
                ('brand_color', models.CharField(blank=True, max_length=200, null=True)),
                ('other_settings', models.JSONField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aormobile.business')),
            ],
        ),
    ]
