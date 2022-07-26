# Generated by Django 4.0 on 2022-06-28 20:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PMWorks_II', '0070_role_userrole'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='AssetCode',
            field=models.CharField(max_length=100, unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')], verbose_name='کد تجهیز'),
        ),
        migrations.AlterField(
            model_name='assetpriority',
            name='AssetPriorityCode',
            field=models.CharField(max_length=100, unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')], verbose_name='کد اولویت'),
        ),
        migrations.AlterField(
            model_name='department',
            name='DepartmentCode',
            field=models.CharField(max_length=100, unique=True, verbose_name='کد دپارتمان'),
        ),
        migrations.AlterField(
            model_name='document',
            name='DocumentCode',
            field=models.CharField(max_length=100, unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')], verbose_name='کد فایل'),
        ),
        migrations.AlterField(
            model_name='failurecause',
            name='FailureCauseCode',
            field=models.CharField(max_length=100, unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')], verbose_name='کد علت خرابی'),
        ),
        migrations.AlterField(
            model_name='jobcategory',
            name='JobCategoryCode',
            field=models.CharField(max_length=100, unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')], verbose_name='کد نوع شغل'),
        ),
        migrations.AlterField(
            model_name='location',
            name='LocationCode',
            field=models.CharField(max_length=100, unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')], verbose_name='کد مکان'),
        ),
        migrations.AlterField(
            model_name='sparepart',
            name='SparePartCode',
            field=models.CharField(max_length=100, unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')], verbose_name='کد قطعه'),
        ),
        migrations.AlterField(
            model_name='sparepartcategory',
            name='SparePartCategoryCode',
            field=models.CharField(max_length=100, unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')], verbose_name='کد خانواده قطعه'),
        ),
        migrations.AlterField(
            model_name='sparepartdimension',
            name='SparePartDimensionCode',
            field=models.CharField(max_length=100, unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')], verbose_name='کد بعد'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='SupplierCode',
            field=models.CharField(max_length=100, unique=True, verbose_name='کد تامین کننده'),
        ),
        migrations.AlterField(
            model_name='tasktype',
            name='TaskTypeCode',
            field=models.CharField(max_length=100, unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')], verbose_name='کد نوع وظیفه'),
        ),
        migrations.AlterField(
            model_name='typewr',
            name='TypeWrCode',
            field=models.CharField(max_length=100, unique=True, verbose_name='کد نوع درخواست کار'),
        ),
        migrations.AlterField(
            model_name='workpriority',
            name='WorkPriorityCode',
            field=models.CharField(max_length=100, unique=True, verbose_name='کد اولویت'),
        ),
    ]