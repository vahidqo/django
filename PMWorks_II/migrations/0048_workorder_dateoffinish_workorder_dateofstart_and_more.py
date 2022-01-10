# Generated by Django 4.0 on 2022-01-05 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PMWorks_II', '0047_auto_20211110_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='workorder',
            name='DateOfFinish',
            field=models.DateField(default='2021-01-01', verbose_name='تاریخ پایان'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workorder',
            name='DateOfStart',
            field=models.DateField(default='2021-01-01', verbose_name='تاریخ شروع'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workorder',
            name='DepartmentID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='PMWorks_II.department', verbose_name='دپارتمان'),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='DateOfPlanFinish',
            field=models.DateField(verbose_name=' برنامهتاریخ پایان'),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='DateOfPlanStart',
            field=models.DateField(verbose_name='تاریخ شروع برنامه'),
        ),
    ]
