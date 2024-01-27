# Generated by Django 5.0 on 2023-12-23 13:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sysGestion', '0005_remove_medecin_heures_disponibilite_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RendezVous',
            fields=[
                ('rendezvous_id', models.AutoField(primary_key=True, serialize=False)),
                ('date_heure', models.DateTimeField()),
                ('statut', models.CharField(choices=[('confirmé', 'Confirmé'), ('annulé', 'Annulé'), ('en_attente', 'En attente')], max_length=20)),
                ('notes', models.TextField(blank=True, null=True)),
                ('medecin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sysGestion.medecin')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sysGestion.patient')),
            ],
        ),
    ]
