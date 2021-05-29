# Generated by Django 3.1.2 on 2021-05-23 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PMWorks_II', '0020_assetsubdivision_assetclasscodechain'),
    ]

    operations = [
        migrations.AddField(
            model_name='assetsubdivision',
            name='AssetClassNameChain',
            field=models.CharField(default=1, max_length=500, verbose_name='رشته نام کلاس'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assetsubdivision',
            name='idChain',
            field=models.CharField(default=1, max_length=500, verbose_name='رشته اي دي'),
            preserve_default=False,
        ),
    ]
