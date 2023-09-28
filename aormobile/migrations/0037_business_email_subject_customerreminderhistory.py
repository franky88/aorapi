# Generated by Django 4.2.5 on 2023-09-28 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aormobile', '0036_reminderemailhistory_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='email_subject',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='CustomerReminderHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.BigIntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('invitation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aormobile.invitation')),
            ],
        ),
    ]