from django.urls import path
from .views import tableau_de_bord
from django.contrib.auth.views import LoginView, LogoutView



from .views import (
    liste_medecins,
    ajouter_medecin,
    editer_medecin,
    supprimer_medecin,
    liste_suppression_medecins,
    actions_medecins,
   
    liste_patients,
    ajouter_patient,
    editer_patient,
    supprimer_patient,
    liste_suppression_patient,
    actions_patient,

    liste_rendezvous,
    ajouter_rendezvous,
    editer_rendezvous,
    supprimer_rendezvous,
    liste_suppression_rendezvous,
    actions_rendezvous,

)

urlpatterns = [
    path('tableau/', tableau_de_bord, name='tableau_de_bord'),
    path('connexion/', LoginView.as_view(template_name='connexion.html'), name='connexion'),
    path('deconnexion/', LogoutView.as_view(next_page='connexion'), name='deconnexion'),
   
    path('medecin/liste/', liste_medecins, name='liste_medecins'),
    path('medecin/ajouter/', ajouter_medecin, name='ajouter_medecin'),
    path('medecin/editer/<int:medecin_id>/', editer_medecin, name='editer_medecin'),
    path('medecin/supprimer/<int:medecin_id>/', supprimer_medecin, name='supprimer_medecin'),
    path('medecin/supprimer/', liste_suppression_medecins, name='liste_suppression_medecins'),
    path('medecin/actions/', actions_medecins, name='actions_medecins'),
   
    path('patient/ajouter/', ajouter_patient, name='ajouter_patient'),
    path('patient/liste/', liste_patients, name='liste_patients'),
    path('patient/editer/<int:patient_id>/', editer_patient, name='editer_patient'),
    path('patient/supprimer/<int:patient_id>/', supprimer_patient, name='supprimer_patient'),
    path('patient/supprimer/', liste_suppression_patient, name='liste_suppression_patients'),
    path('patient/actions/', actions_patient, name='actions_patients'),

    path('rendezvous/ajouter/', ajouter_rendezvous, name='ajouter_rendezvous'),
    path('rendezvous/liste/', liste_rendezvous, name='liste_rendezvous'),
    path('rendezvous/editer/<int:rendezvous_id>/', editer_rendezvous, name='editer_rendezvous'),
    path('rendezvous/supprimer/<int:rendezvous_id>/', supprimer_rendezvous, name='supprimer_rendezvous'),
    path('rendezvous/supprimer/', liste_suppression_rendezvous, name='liste_suppression_rendezvous'),
    path('rendezvous/actions/', actions_rendezvous, name='actions_rendezvous'),




]







