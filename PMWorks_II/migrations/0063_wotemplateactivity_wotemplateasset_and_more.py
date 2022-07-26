# Generated by Django 4.0 on 2022-04-01 16:11

from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('PMWorks_II', '0062_remove_wotemplateschualing_frequencyid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WOTemplateActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Create', django_jalali.db.models.jDateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ ایجاد')),
                ('Update', django_jalali.db.models.jDateTimeField(auto_now=True, null=True, verbose_name='تاریخ آخرین تغییر')),
                ('TaskID', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='PMWorks_II.assetclasstask', verbose_name='وظيفه')),
            ],
            options={
                'verbose_name': 'وظايف تجهيز برنامه',
                'verbose_name_plural': 'وظايف تجهيزات برنامه',
                'ordering': ['-Create'],
            },
        ),
        migrations.CreateModel(
            name='WOTemplateAsset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Create', django_jalali.db.models.jDateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ ایجاد')),
                ('Update', django_jalali.db.models.jDateTimeField(auto_now=True, null=True, verbose_name='تاریخ آخرین تغییر')),
                ('AssetID', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='PMWorks_II.asset', verbose_name='تجهيز')),
                ('WOTemplateID', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='PMWorks_II.wotemplate', verbose_name='برنامه')),
            ],
            options={
                'verbose_name': 'تجهيز برنامه',
                'verbose_name_plural': 'تجهيزات برنامه',
                'ordering': ['-Create'],
            },
        ),
        migrations.AddField(
            model_name='templateschualingdate',
            name='WorkOrderID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='PMWorks_II.workorder', verbose_name='دستور کار'),
        ),
        migrations.DeleteModel(
            name='WOActivityTemplateTbl',
        ),
        migrations.AddField(
            model_name='wotemplateactivity',
            name='WOTemplateAssetID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='PMWorks_II.wotemplateasset', verbose_name='تجهيز برنامه'),
        ),
    ]
