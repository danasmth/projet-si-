# Generated by Django 5.0 on 2023-12-23 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sysGestion', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='date_naissance',
        ),
    ]
