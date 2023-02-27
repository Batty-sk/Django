# Generated by Django 4.0.4 on 2022-12-26 14:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0002_alter_user_pics_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_pics',
            name='id',
        ),
        migrations.AlterField(
            model_name='user_pics',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
