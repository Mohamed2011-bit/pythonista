# Generated by Django 3.1.4 on 2020-12-11 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0006_auto_20201211_0257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='github',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='linkedin',
            field=models.URLField(null=True),
        ),
    ]
