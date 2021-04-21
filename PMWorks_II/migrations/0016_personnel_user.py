# Generated by Django 3.1.2 on 2021-04-21 16:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('PMWorks_II', '0015_auto_20210202_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='personnel',
            name='user',
            field=models.OneToOneField(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user', verbose_name='یوزر'),
            preserve_default=False,
        ),
    ]
