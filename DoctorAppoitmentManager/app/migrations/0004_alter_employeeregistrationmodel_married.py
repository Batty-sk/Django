# Generated by Django 4.0.4 on 2022-12-29 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_employeeregistrationmodel_date_of_joining'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeregistrationmodel',
            name='Married',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')]),
        ),
    ]
