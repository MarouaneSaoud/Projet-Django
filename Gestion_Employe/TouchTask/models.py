from django.db import models
from django.utils import timezone


class Chef_Service(models.Model):
    Matricule = models.AutoField(primary_key = True)
    Nom = models.CharField(max_length=50)
    Prenom = models.CharField(max_length=50)
    Date_recrutement = models.DateField()
    salaire = models.FloatField(default=8000)
    email =models.CharField(max_length=40)
    mdp = models.CharField(max_length=100)
    def _str_(self):
        return self.NOM

class Equipe(models.Model):
    id_Equipe = models.AutoField(primary_key=True)
    Nom_Equipe=models.CharField(max_length=80)
    date_creation=models.DateField(auto_now_add=True)
    chef_Service=models.ForeignKey(Chef_Service , on_delete=models.CASCADE)
    def _str_(self):
        return self.Nom_Equipe


class Employe(models.Model):
    Matricule = models.AutoField(primary_key=True)
    Nom = models.CharField(max_length=50)
    Prenom = models.CharField(max_length=50)
    Date_recrutement = models.DateTimeField(auto_now_add=True)
    salaire = models.FloatField(default=2500)
    email = models.CharField(max_length=40)
    mdp = models.CharField(max_length=100)
    Equipe=models.ForeignKey(Equipe , on_delete=models.CASCADE)
    def _str_(self):
        return self.NOM

class Projet(models.Model):
    id_projet = models.AutoField(primary_key=True)
    NomProjet = models.CharField(max_length=80)
    Description = models.CharField(max_length=30000)
    date_creation = models.DateField(auto_now_add=True)
    Dead_Line = models.DateField()
    Equipe=models.ForeignKey(Equipe , on_delete=models.CASCADE)
    def _str_(self):
        return self.NomProjet


class Tache(models.Model):
    id_tache = models.AutoField(primary_key=True)
    Nom_tache = models.CharField(max_length=50)
    Description = models.CharField(max_length=30000)
    date_lancement =models.DateTimeField(auto_now_add=True)
    etat_choix={('en cours' , 'EN COURS'),('fin','FIN')}
    Etat = models.CharField(max_length=20 , choices=etat_choix,  default='En attente')
    Employe = models.ForeignKey(Employe, on_delete=models.CASCADE)
    Projet = models.ForeignKey(Projet, on_delete=models.CASCADE)
    def _str_(self):
        return self.Nom_tache