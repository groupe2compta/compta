from django.urls import path
from .import views

urlpatterns=[
    path('', views.index, name="index"),
    path('dashoboard', views.dashoboard, name="dashoboard"),
    path('deconnexion', views.deconnexion,name='deconnexion'),
    path('listeFrais', views.listeFrais, name='listeFrais'),
    path('listeTransaction', views.listeTransaction,name="listeTransaction"),
    path('listeEtudiant', views.listeEtudiant, name="listeEtudiant"),
    path('ajouterEtudiant', views.ajouterEtudiant, name='ajouterEtudiant'),
    path('modifier/<str:id>/Etudiant', views.modifierEtudiant, name="modifierEtudiant"),
    path('supprimer/<str:id>/Etudiant', views.supprimerEtudiant, name="supprimerEtudiant"),
    path('ajouterTransaction', views.ajouterTransaction, name="ajouterTransaction"),
    path('modif/<str:id>/Transaction', views.modifTransaction, name="modifTransaction"),
    path('FixerFrais', views.FixerFrais,name="FixerFrais"),
    path('Change/<str:id>/Frais', views.ChangeFrais, name="ChangeFrais"),
    path('supp/<str:id>/Frais', views.suppFrais, name="suppFrais"),
    path('supp/<str:id>/Transaction', views.suppTransaction, name="suppTransaction")
]