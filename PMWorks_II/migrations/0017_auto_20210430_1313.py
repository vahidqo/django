# Generated by Django 3.1.2 on 2021-04-30 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PMWorks_II', '0016_personnel_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='status',
            field=models.IntegerField(blank=True, default=1, verbose_name='وضعيت توليد'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assetsubdivision',
            name='fakelocation',
            field=models.IntegerField(blank=True, default=1, verbose_name='مکان فيک'),
            preserve_default=False,
        ),
    ]
