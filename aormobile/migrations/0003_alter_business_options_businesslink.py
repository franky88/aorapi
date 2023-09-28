# Generated by Django 4.2.5 on 2023-09-28 03:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aormobile', '0002_business'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='business',
            options={'verbose_name_plural': 'businesses'},
        ),
        migrations.CreateModel(
            name='BusinessLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(blank=True, null=True)),
                ('latitude', models.CharField(blank=True, max_length=100, null=True)),
                ('longitude', models.CharField(blank=True, max_length=100, null=True)),
                ('timezone', models.CharField(blank=True, max_length=100, null=True)),
                ('notification_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('links', models.URLField(blank=True, null=True)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aormobile.business')),
            ],
        ),
    ]