# Generated by Django 3.1.2 on 2021-05-10 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PMWorks_II', '0018_asset_fakesub'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workrequest',
            name='FailureCauseID',
        ),
    ]
