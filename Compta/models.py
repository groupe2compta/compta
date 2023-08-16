from django.db import models



# class Faculte(models.Model):
#     designation=models.CharField(max_length=155)
#     date_creation=models.DateField(auto_now_add=True)
#     date_modification=models.DateField(auto_now=True)

#     def __str__(self):
#         return self.designation

# class Promotion(models.Model):
#     faculte=models.ForeignKey(Faculte,on_delete=models.CASCADE)
#     designation=models.CharField(max_length=155)
#     date_creation=models.DateField(auto_now_add=True)
#     date_modification=models.DateField(auto_now=True)

#     def __str__(self):
#         return f"{self.designation} : {self.faculte}"

class Etudiant(models.Model):
    matricule=models.CharField(max_length=155, unique=True)
    nom=models.CharField(max_length=155)
    postnom=models.CharField(max_length=155)
    prenom=models.CharField(max_length=155)
    date_creation=models.DateField(auto_now_add=True)
    date_modification=models.DateField(auto_now=True)


    @property
    def getMontantInscription(self):
        inscription=self.transaction_set.filter(frais__designation="INSCR")
        return sum([ligne.montant for ligne in inscription])
    
    @property
    def getMontantReinscription(self):
        reinscription=self.transaction_set.filter(frais__designation="REINSCR")
        return sum([ligne.montant for ligne in reinscription])
    
    @property
    def getSession(self):
        session=self.transaction_set.filter(frais__designation="S")
        return sum([ligne.montant for ligne in session])
    
    @property
    def getTranche1(self):
        tranche1=self.transaction_set.filter(frais__designation="T1")
        return sum([ligne.montant for ligne in tranche1])
    
    @property
    def getTranche2(self):
        tranche2=self.transaction_set.filter(frais__designation="T2")
        return sum([ligne.montant for ligne in tranche2])
    
    @property
    def getTranche3(self):
        tranche3=self.transaction_set.filter(frais__designation="T3")
        return sum([ligne.montant for ligne in tranche3])


    def __str__(self):
        return f"{self.matricule} : {self.nom}-{self.postnom}-{self.prenom}"


    




class Annee(models.Model):
    designation=models.CharField(max_length=155)
    date_creation=models.DateField(auto_now_add=True)
    date_modification=models.DateField(auto_now=True)


    def __str__(self):
        return self.designation





class Frais(models.Model):
    TYPE_FRAIS=(
        ('INSCR', 'INSCRIPTION'),
        ('REINSCR', 'REINSCRIPTION'),
        ('S', 'SESSION'),
        ('T1', 'TRANCHE1'),
        ('T2', 'TRANCHE2'),
        ('T3', 'TRANCHE3'),
    )
    etudiant=models.ManyToManyField(Etudiant, through='Transaction')
    designation=models.CharField(max_length=20, choices=TYPE_FRAIS)
    montant=models.DecimalField(max_digits=15, decimal_places=2)
    annee=models.ForeignKey(Annee, on_delete=models.CASCADE)
    date_creation=models.DateField(auto_now_add=True)
    date_modification=models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.designation}-{self.annee}-{self.montant}"
    

class Transaction(models.Model):
    etudiant=models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    frais=models.ForeignKey(Frais, on_delete=models.CASCADE)
    montant=models.DecimalField(max_digits=15, decimal_places=2)
    date_creation=models.DateField(auto_now_add=True)
    date_modification=models.DateField(auto_now=True)


    def __str__(self):
        return f"{self.etudiant.nom}-{self.montant}"