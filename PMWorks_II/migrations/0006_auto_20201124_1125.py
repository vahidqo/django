# Generated by Django 3.1.2 on 2020-11-24 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PMWorks_II', '0005_auto_20201122_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='InstallationDate',
            field=models.DateField(verbose_name='تاریخ نصب'),
        ),
    ]
