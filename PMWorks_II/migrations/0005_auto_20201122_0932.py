# Generated by Django 3.1.2 on 2020-11-22 06:02

from django.db import migrations, models
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('PMWorks_II', '0004_auto_20201117_1038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asset',
            name='DocumentID',
        ),
        migrations.CreateModel(
            name='AssetDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Create', django_jalali.db.models.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('Update', django_jalali.db.models.jDateTimeField(auto_now=True, verbose_name='تاریخ آخرین تغییر')),
                ('AssetID', models.ForeignKey(on_delete=models.Model, to='PMWorks_II.asset', verbose_name='تجهیز')),
                ('DocumentID', models.ForeignKey(on_delete=models.Model, to='PMWorks_II.document', verbose_name='فایل')),
            ],
            options={
                'verbose_name': 'قایل تجهیز',
                'verbose_name_plural': 'فایل های تجهیز',
                'ordering': ['-Create'],
            },
        ),
    ]
