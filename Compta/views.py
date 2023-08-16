from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .import forms
from .import models


def index(request):
    form=forms.FormConnexion()
    if request.method == "POST":
        form=forms.FormConnexion(request.POST)
        if form.is_valid():
            nom=form.cleaned_data['nom']
            password=form.cleaned_data['password']
            user=authenticate(username=nom, password=password)
            if user:
                login(request, user)
                return redirect('dashoboard')
            else:
                messages.error(request, 'Connexion échouée !')
        else:
            messages.error(request, "Formulaire invalide !")
    return render(request, "accueil/index.html",{"form":form})

def deconnexion(request):
    logout(request)
    return redirect('index')


@login_required(login_url='index')
def dashoboard(request):
    liste_etudiant=models.Etudiant.objects.all().order_by('nom')
    context={
        "liste_etudiant":liste_etudiant
    }
    return render(request, "dashboard/dashoboard.html", context)

def listeFrais(request):
    liste_frais=models.Frais.objects.all()
    context={
        "liste_frais":liste_frais
    }
    return render(request, "dashboard/listeFrais.html", context)

def listeTransaction(request):
    liste_transaction=models.Transaction.objects.all()
    context={
        'liste_transaction':liste_transaction
    }
    return render(request, "dashboard/listeTransaction.html", context)

def listeEtudiant(request):
    liste_etudiant=models.Etudiant.objects.all()
    context={
        "liste_etudiant":liste_etudiant
    }
    return render(request, 'dashboard/listeEtudiant.html', context)

def ajouterEtudiant(request):
    form=forms.FormAjoutEtudiant()
    if request.method == 'POST':
        form=forms.FormAjoutEtudiant(request.POST)
        if form.is_valid():
            matricule=form.cleaned_data['matricule']
            nom=form.cleaned_data['nom']
            postnom=form.cleaned_data['postnom']
            prenom=form.cleaned_data['prenom']
            matricule=form.cleaned_data['matricule']
            new_etudiant=models.Etudiant.objects.create(matricule=matricule,nom=nom,postnom=postnom, prenom=prenom)
            new_etudiant.save()
            messages.success(request, "Etudiant enregistrée avec succès !")
            form=forms.FormAjoutEtudiant()
        else:
            messages.error(request, "Enregistrement echoué !")
    return render(request, 'dashboard/ajouterEtudiant.html', {"form":form})

def modifierEtudiant(request,id):
    get_id=models.Etudiant.objects.get(id=id)
    form=forms.FormAjoutEtudiant(instance=get_id)
    if request.method == 'POST':
        form=forms.FormAjoutEtudiant(request.POST, instance=get_id)
        if form.is_valid():
            form.save()
            return redirect('listeEtudiant')
        else:
            messages.error(request, "Modification Impossible !")
    return render(request, 'dashboard/ModifierEtudiant.html', {"form":form})

def supprimerEtudiant(request,id):
    get_id=models.Etudiant.objects.get(id=id)
    if request.method == "POST":
        get_id.delete()
        return redirect('listeEtudiant')
    return render(request, 'dashboard/confirmSuppEtudiant.html', {"get_id":get_id})

def ajouterTransaction(request):
    form=forms.FormAjoutTransaction()
    if request.method == "POST":
        form=forms.FormAjoutTransaction(request.POST)
        if form.is_valid(): 
            etudiant=form.cleaned_data['etudiant']
            frais=form.cleaned_data['frais']
            montant=form.cleaned_data['montant']
            verification_versement=models.Transaction.objects.filter(etudiant=etudiant, frais=frais)
            sommes=sum([ligne.montant for ligne in verification_versement])
            reste=frais.montant - sommes
            if montant < 1:
                messages.error(request, "Impossible de donner un montant inférieur à 1 !")
            elif montant > frais.montant:
                messages.error(request, "Montant supérieur au montant prévu !")
            elif montant + sommes > frais.montant :
                messages.error(request, f"Cet étudiant a déjà ce frais {frais.designation} donné il lui reste {reste}")
            else:
                new_transaction=models.Transaction.objects.create(etudiant=etudiant, frais=frais,montant=montant)
                new_transaction.save()
                messages.success(request, "Frais payé et enregistré avec succès !")
                form=forms.FormAjoutTransaction()
        else:
            messages.error(request, "Formulaire invalide !")
    return render(request, 'dashboard/ajouterTransaction.html', {"form":form})


def modifTransaction(request, id):
    get_id=models.Transaction.objects.get(id=id)
    oldMontant=get_id.montant
    form=forms.FormAjoutTransaction(instance=get_id)
    if request.method == "POST":
        form=forms.FormAjoutTransaction(request.POST,instance=get_id)
        if form.is_valid(): 
            etudiant=form.cleaned_data['etudiant']
            frais=form.cleaned_data['frais']
            montant=form.cleaned_data['montant']
            verification_versement=models.Transaction.objects.filter(etudiant=etudiant, frais=frais)
            sommes=sum([ligne.montant for ligne in verification_versement])
            diminuer=sommes - oldMontant
            if montant < 1:
                messages.error(request, "Impossible de donner un montant inférieur à 1 !")
            elif montant > frais.montant:
                messages.error(request, "Montant supérieur au montant prévu !")
            elif montant + diminuer > frais.montant :
                messages.error(request, "Impossible d'effectuer cette Opération !")
            else:
                form.save()
                return redirect('listeTransaction')
        else:
            messages.error(request, "Formulaire invalide !")
    return render(request, 'dashboard/modifierTransaction.html',{"form":form})

def FixerFrais(request):
    form=forms.FormAjoutFrais()
    if request.method == "POST":
        form=forms.FormAjoutFrais(request.POST)
        if form.is_valid():
            designation=form.cleaned_data['designation']
            montant=form.cleaned_data['montant']
            annee=form.cleaned_data['annee']
            verification=models.Frais.objects.filter(designation=designation, annee=annee).exists()
            if verification :
                messages.error(request, "Cette année avec cette designation des frais existe déjà !")
            else:
                form.save()
                messages.success(request, "Frais fixé avec succès !")
                form=forms.FormAjoutFrais()
        else:
            messages.error(request, "Impossible de fixer ce frais")
    return render(request,'dashboard/fixerFrais.html', {"form":form})


def ChangeFrais(request, id):
    get_id=models.Frais.objects.get(id=id)
    form=forms.FormAjoutFrais(instance=get_id)
    if request.method == "POST":
        form=forms.FormAjoutFrais(request.POST, instance=get_id)
        if form.is_valid():
            designation=form.cleaned_data['designation']
            montant=form.cleaned_data['montant']
            annee=form.cleaned_data['annee']
            verification=models.Frais.objects.filter(designation=designation,montant=montant, annee=annee).exists()
            if verification :
                messages.error(request, "Tu n'as apporté aucune modification !")
            else:
                form.save()
                messages.success(request, "Frais fixé avec succès !")
                form=forms.FormAjoutFrais()
        else:
            messages.error(request, "Impossible de fixer ce frais")
    return render(request,'dashboard/changerFrais.html', {"form":form})

def suppFrais(request, id):
    get_id=models.Frais.objects.get(id=id)
    if request.method == "POST":
        get_id.delete()
        return redirect('listeFrais')
    return render(request, "dashboard/confirmSuppFrais.html")

def suppTransaction(request, id):
    get_id=models.Transaction.objects.get(id=id)
    if request.method == 'POST':
        get_id.delete()
        return redirect('listeTransaction')
    return render(request, "dashboard/confirmSuppTransaction.html")