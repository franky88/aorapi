# Generated by Django 4.2.5 on 2023-09-28 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aormobile', '0033_credittransaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
