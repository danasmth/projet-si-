from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Patient (models.Model):
    patient_id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    date_naissance = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.nom



class Medecin(models.Model):
    SPECIALITES = [
        ('Cardiologie', 'Cardiologue'),
    ]

    medecin_id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    specialite = models.CharField(max_length=20, choices=SPECIALITES)
    numero_telephone = models.CharField(max_length=15)
    adresse_email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return f"{self.nom} {self.prenom}"
    

class RendezVous(models.Model):
    rendezvous_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medecin = models.ForeignKey(Medecin, on_delete=models.CASCADE)
    date_heure = models.DateTimeField()
    status = models.CharField(max_length=20, choices=[('confirmé', 'Confirmé'), ('annulé', 'Annulé'), ('en_attente', 'En attente')])
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Rendez-vous avec {self.medecin} le {self.date_heure}"


class DossierMedical(models.Model):
    dossier_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medecin = models.ForeignKey(Medecin, on_delete=models.CASCADE)
    date_creation = models.DateField(auto_now_add=True)
    informations_medicales = models.TextField(blank=True, null=True)
    resultats_examens = models.TextField(blank=True, null=True)
    traitement_en_cours = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Dossier médical de {self.patient} créé le {self.date_creation}"


class Departement(models.Model):

    DEPARTEMENT_CHOICES = [
        ('Cardiologie', 'Cardiologie'),

    ]

    departement_id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=20, choices=DEPARTEMENT_CHOICES , null=True, blank=True)

    def __str__(self):
        return self.nom

class TacheDepartement(models.Model):
    tache_id = models.AutoField(primary_key=True)
    medecin = models.ForeignKey(Medecin, on_delete=models.CASCADE)
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE)
    description = models.TextField() 
    statut = models.CharField(max_length=20, choices=[('en_cours', 'En cours'), ('terminee', 'Terminée'), ('en_attente', 'En attente')])

    def __str__(self):
        return f"Tâche {self.description} pour {self.departement} - {self.medecin}"
