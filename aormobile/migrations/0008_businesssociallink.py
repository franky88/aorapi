# Generated by Django 4.2.5 on 2023-09-28 04:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aormobile', '0007_businesssetup'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessSocialLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_url', models.URLField()),
                ('status', models.IntegerField(default=1)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('business_link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aormobile.businesslink')),
                ('social_link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aormobile.sociallink')),
            ],
        ),
    ]
