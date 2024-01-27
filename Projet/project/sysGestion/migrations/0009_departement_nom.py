# Generated by Django 5.0 on 2023-12-23 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sysGestion', '0008_departement_alter_medecin_specialite'),
    ]

    operations = [
        migrations.AddField(
            model_name='departement',
            name='nom',
            field=models.CharField(blank=True, choices=[('Cardiologie', 'Cardiologie'), ('Neurologie', 'Neurologie'), ('Urologie', 'Urologie'), ('Rhumatologie', 'Rhumatologie'), ('ORL', 'ORL')], max_length=20, null=True),
        ),
    ]