from django import forms
from django.contrib.auth.forms import AuthenticationForm

class RechercheForm(forms.Form):
    type_entite = forms.ChoiceField(choices=[('patient', 'Patient'), ('medecin', 'Médecin'),
    ('rendezvous', 'Rendez-vous'), ('dossier', 'Dossier Médical'), 
    ('departement', 'Département'), ('tache', 'Tâche de Département')])
    recherche = forms.CharField(required=False, label='Recherche', 
    widget=forms.TextInput(attrs={'placeholder': 'Rechercher...'}))



class ConnexionForm(AuthenticationForm):
    pass



from .models import Medecin

class MedecinForm(forms.ModelForm):
    class Meta:
        model = Medecin
        fields = ['nom', 'prenom', 'specialite', 'numero_telephone', 'adresse_email'] 




from .models import Patient  

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient 
        fields = ['nom', 'date_naissance']




from .models import RendezVous  

class RendezVousForm(forms.ModelForm):
    class Meta:
        model = RendezVous 
        fields = ['medecin', 'patient', 'date_heure', 'status', 'notes']


