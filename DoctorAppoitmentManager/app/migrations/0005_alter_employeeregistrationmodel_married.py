# Generated by Django 4.0.4 on 2022-12-29 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_employeeregistrationmodel_married'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeregistrationmodel',
            name='Married',
            field=models.CharField(max_length=10),
        ),
    ]
