# Generated by Django 5.0 on 2023-12-23 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sysGestion', '0003_patient_date_naissance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medecin',
            fields=[
                ('medecin_id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('specialite', models.CharField(choices=[('Cardiologie', 'Cardiologie'), ('Neurologie', 'Neurologie'), ('Urologie', 'Urologie'), ('Rhumatologie', 'Rhumatologie'), ('ORL', 'ORL')], max_length=20)),
                ('numero_telephone', models.CharField(max_length=15)),
                ('adresse_email', models.EmailField(max_length=254)),
                ('heures_disponibilite', models.CharField(max_length=255)),
            ],
        ),
    ]
