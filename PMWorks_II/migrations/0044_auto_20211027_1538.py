# Generated by Django 3.1.2 on 2021-10-27 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PMWorks_II', '0043_status_workflowlevel_workflowlevelstatus_wostatus_wrstatus_wrworelationstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='workorder',
            name='Status',
            field=models.CharField(default=1, max_length=100, verbose_name='وضعيت'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workrequest',
            name='Status',
            field=models.CharField(default=1, max_length=100, verbose_name='وضعيت'),
            preserve_default=False,
        ),
    ]