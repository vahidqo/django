# Generated by Django 3.1.2 on 2021-07-19 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PMWorks_II', '0031_auto_20210713_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='failuremode',
            name='FailureModeCode',
            field=models.CharField(max_length=100, unique=True, verbose_name='کد نوع خرابی'),
        ),
        migrations.AlterField(
            model_name='failuremode',
            name='FailureModeDescription',
            field=models.TextField(blank=True, verbose_name='توضیحات'),
        ),
    ]