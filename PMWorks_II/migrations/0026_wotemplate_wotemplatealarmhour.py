# Generated by Django 3.1.2 on 2021-06-11 05:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PMWorks_II', '0025_wotemplate_wotemplatedurationhour'),
    ]

    operations = [
        migrations.AddField(
            model_name='wotemplate',
            name='WOTemplateAlarmHour',
            field=models.TimeField(verbose_name='ساعت اعلام تناوب'),
            preserve_default=False,
        ),
    ]
