# Generated by Django 4.0 on 2022-03-24 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PMWorks_II', '0058_remove_wotemplate_wotemplatealarmhour'),
    ]

    operations = [
        migrations.AddField(
            model_name='wotemplate',
            name='WOTemplateAlarmHour',
            field=models.IntegerField(default=1, verbose_name='ساعت اعلام تناوب'),
            preserve_default=False,
        ),
    ]
