# Generated by Django 3.1.4 on 2020-12-11 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0011_auto_20201211_1920'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='github_url',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='linkedin_url',
        ),
        migrations.AddField(
            model_name='profile',
            name='github',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='linkedin',
            field=models.URLField(blank=True),
        ),
    ]
