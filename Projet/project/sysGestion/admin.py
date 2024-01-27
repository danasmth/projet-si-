from django.contrib import admin
from .models import Patient, Medecin, RendezVous, DossierMedical, Departement, TacheDepartement

# Register your models here.
admin.site.register(Patient)
admin.site.register(Medecin)
admin.site.register(RendezVous)
admin.site.register(DossierMedical)
admin.site.register(Departement)
admin.site.register(TacheDepartement)
