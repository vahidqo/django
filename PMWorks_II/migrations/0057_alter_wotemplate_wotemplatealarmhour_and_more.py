# Generated by Django 4.0 on 2022-03-23 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PMWorks_II', '0056_rename_templateschualingdate_templateschualingdate_schualingdate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wotemplate',
            name='WOTemplateAlarmHour',
            field=models.IntegerField(verbose_name='ساعت اعلام تناوب'),
        ),
        migrations.AlterField(
            model_name='wotemplate',
            name='WOTemplateDurationHour',
            field=models.IntegerField(verbose_name='ساعت تناوب'),
        ),
    ]
