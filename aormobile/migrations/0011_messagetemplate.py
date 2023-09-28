# Generated by Django 4.2.5 on 2023-09-28 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aormobile', '0010_sociallink_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('status', models.BooleanField(default=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]