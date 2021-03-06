# Generated by Django 3.1.2 on 2020-12-07 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PMWorks_II', '0006_auto_20201124_1125'),
    ]

    operations = [
        migrations.CreateModel(
            name='status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_id', models.IntegerField(blank=True, null=True)),
                ('bikes_available', models.IntegerField(blank=True, null=True)),
                ('docks_available', models.IntegerField(blank=True, null=True)),
                ('time', models.DateTimeField()),
            ],
            options={
                'ordering': ['time'],
            },
        ),
    ]
