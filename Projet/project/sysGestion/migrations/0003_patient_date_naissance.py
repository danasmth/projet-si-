# Generated by Django 5.0 on 2023-12-23 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sysGestion', '0002_remove_patient_date_naissance'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='date_naissance',
            field=models.DateField(blank=True, null=True),
        ),
    ]
