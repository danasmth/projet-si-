from django.shortcuts import render
from .models import Patient, Medecin, RendezVous, DossierMedical, Departement, TacheDepartement
from .forms import RechercheForm
from .forms import MedecinForm
from .forms import PatientForm
from .forms import RendezVousForm



def tableau_de_bord(request):
    form = RechercheForm(request.GET)

    type_entite = None
    recherche = None
    if form.is_valid():
        type_entite = form.cleaned_data['type_entite']
        recherche = form.cleaned_data['recherche']

    if   type_entite == 'patient':
        entites = Patient.objects.filter(nom__iexact=recherche)
    elif type_entite == 'medecin':
        entites = Medecin.objects.filter(nom__iexact=recherche)
    elif type_entite == 'rendezvous':
        entites = RendezVous.objects.filter(rendezvous_id__iexact=recherche)
    elif type_entite == 'dossier':
        entites = DossierMedical.objects.filter(dossier_id__iexact=recherche)
    elif type_entite == 'departement':
        entites = Departement.objects.filter(nom__iexact=recherche)
    elif type_entite == 'tache':
        entites = TacheDepartement.objects.filter(tache_id__iexact=recherche)
    else:
        entites = None
     

    context = {
        'form': form,
        'type_entite': type_entite,
        'entites': entites,
        'recherche': recherche,
    }
    return render(request, 'liste.html', context)




from django.shortcuts import render, redirect, get_object_or_404

#MEDECIN

def ajouter_medecin(request):
    message = None

    if request.method == 'POST':
        form = MedecinForm(request.POST)
        if form.is_valid():
            form.save()
            message = "Médecin ajouté avec succès."
            # Réinitialiser le formulaire après l'ajout si nécessaire
            form = MedecinForm()
    else:
        form = MedecinForm()

    return render(request, 'formulaire_medecin.html', {'form': form, 'action': 'Ajouter', 'message': message})



def liste_medecins(request):
    medecins = Medecin.objects.all()
    return render(request, 'liste_medecin.html', {'medecins': medecins})

def editer_medecin(request, medecin_id):
    medecin = get_object_or_404(Medecin, pk=medecin_id)
    message_edit = None

    if request.method == 'POST':
        form = MedecinForm(request.POST, instance=medecin)
        if form.is_valid():
            form.save()
            message_edit = "Modifications enregistrées avec succès."
        else:
            message_edit = "Erreur lors de l'enregistrement des modifications. Veuillez corriger les erreurs."
    else:
        form = MedecinForm(instance=medecin)

    return render(request, 'modifier_medecin.html', {'medecin': medecin, 'form': form, 'message_edit': message_edit})


def supprimer_medecin(request, medecin_id):
    medecin = get_object_or_404(Medecin, pk=medecin_id)

    if request.method == 'POST':
        medecin.delete()
        return redirect('liste_medecins')

    return render(request, 'supprimer_medecin.html', {'medecin': medecin})


def liste_suppression_medecins(request):
    medecins = Medecin.objects.all()
    return render(request, 'liste_suppression_medecins.html', {'medecins': medecins})

def actions_medecins(request):
    return render(request, 'action_medecins.html')






#PATIENT

def ajouter_patient(request):
    message = None

    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            message = "Patient ajouté avec succès."

            #reinitialiser le formulaire apres l'ajout 
            form = PatientForm()

    else:
        form = PatientForm()


    return render(request, 'formulaire_patient.html', {'form': form, 'action': 'Ajouter', 'message': message})        



def liste_patients(request):
    patients = Patient.objects.all()
    return render(request, 'liste_patient.html', {'patients': patients})



def editer_patient(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    message_edit = None

    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            message_edit = "Modifications enregistrées avec succès."
        else:
            message_edit = "Erreur lors de l'enregistrement des modifications. Veuillez corriger les erreurs."
    else:
        form = PatientForm(instance=patient)

    return render(request, 'modifier_patient.html', {'patient': patient, 'form': form, 'message_edit': message_edit})



def supprimer_patient(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)

    if request.method == 'POST':
        patient.delete()
        return redirect('liste_patients')

    return render(request, 'supprimer_patient.html', {'patient': patient})



def liste_suppression_patient(request):
    patients = Patient.objects.all()
    return render(request, 'liste_suppression_patients.html', {'patient': patients})


def actions_patient(request):
    return render(request, 'action_patients.html')




#rendez_vous


def ajouter_rendezvous(request):
    message = None

    if request.method == 'POST':
        form = RendezVousForm(request.POST)
        if form.is_valid():
            form.save()
            message = "RendezVous ajouté avec succès."

            #reinitialiser le formulaire apres l'ajout 
            form = RendezVousForm()

    else:
        form = RendezVousForm()


    return render(request, 'formulaire_rendezvous.html', {'form': form, 'action': 'Ajouter', 'message': message})        



def liste_rendezvous(request):
    rendezvouss = RendezVous.objects.all()
    return render(request, 'liste_rendezvous.html', {'rendezvouss': rendezvouss})



def editer_rendezvous(request, rendezvous_id):
    rendezvous = get_object_or_404(RendezVous, pk=rendezvous_id)
    message_edit = None

    if request.method == 'POST':
        form = RendezVousForm(request.POST, instance=rendezvous)
        if form.is_valid():
            form.save()
            message_edit = "Modifications enregistrées avec succès."
        else:
            message_edit = "Erreur lors de l'enregistrement des modifications. Veuillez corriger les erreurs."
    else:
        form = RendezVousForm(instance=rendezvous)

    return render(request, 'modifier_rendezvous.html', {'rendezvous': rendezvous, 'form': form, 'message_edit': message_edit})



def supprimer_rendezvous(request, rendezvous_id):
    rendezvous = get_object_or_404(RendezVous, pk=rendezvous_id)

    if request.method == 'POST':
        rendezvous.delete()
        return redirect('liste_rendezvous')

    return render(request, 'supprimer_rendezvous.html', {'rendezvous': rendezvous})



def liste_suppression_rendezvous(request):
    rendezvous = RendezVous.objects.all()
    return render(request, 'liste_suppression_rendezvous.html', {'rendezvous': rendezvous})


def actions_rendezvous(request):
    return render(request, 'action_rendezvous.html')






