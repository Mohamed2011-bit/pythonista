# Generated by Django 3.1.4 on 2020-12-11 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0003_auto_20201211_0158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='github',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='linkedin',
            field=models.URLField(blank=True),
        ),
    ]
