from django import forms
from .import models




class FormConnexion(forms.Form):
    nom=forms.CharField(widget=forms.TextInput(attrs={"class":'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":'form-control'}))



class FormAjoutEtudiant(forms.ModelForm):
    class Meta:
        model=models.Etudiant
        fields=[
            'matricule', 'nom', 'postnom', 'prenom'
        ]

        widgets={
            "matricule":forms.TextInput(attrs={"class":"form-control"}),
            "nom":forms.TextInput(attrs={"class":"form-control"}),
            "postnom":forms.TextInput(attrs={"class":"form-control"}),
            "prenom":forms.TextInput(attrs={"class":"form-control"}),   
        }

class FormAjoutFrais(forms.ModelForm):
    class Meta:
        model=models.Frais
        fields=[
            'designation', 'montant'
        ]
        widgets={
            "designation":forms.TextInput(attrs={"class":"form-control"}),
            "montant":forms.NumberInput(attrs={"class":"form-control"}),
        }

class FormAjoutTransaction(forms.ModelForm):
    class Meta:
        model=models.Transaction
        fields=[
            'etudiant', 'frais', 'montant'
        ]
        widgets={
                "etudiant":forms.Select(attrs={"class":"form-control"}),
                "frais":forms.Select(attrs={"class":"form-control"}),
                "montant":forms.NumberInput(attrs={"class":"form-control"}),
        }