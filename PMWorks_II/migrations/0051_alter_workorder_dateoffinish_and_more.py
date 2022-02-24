# Generated by Django 4.0 on 2022-01-09 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PMWorks_II', '0050_remove_workflowlevelstatusshow_workflowlevelid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workorder',
            name='DateOfFinish',
            field=models.DateField(blank=True, null=True, verbose_name='تاریخ پایان'),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='DateOfPlanFinish',
            field=models.DateField(blank=True, null=True, verbose_name=' برنامهتاریخ پایان'),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='DateOfPlanStart',
            field=models.DateField(blank=True, null=True, verbose_name='تاریخ شروع برنامه'),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='DateOfStart',
            field=models.DateField(blank=True, null=True, verbose_name='تاریخ شروع'),
        ),
    ]