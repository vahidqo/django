# Generated by Django 4.0 on 2022-05-08 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PMWorks_II', '0068_remove_wotask_workorderid_woassetsubdivision_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personnel',
            name='PersonnelNetCode',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='کد نت پرسنل'),
        ),
    ]
