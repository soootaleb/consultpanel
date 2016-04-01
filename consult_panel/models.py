from django.db import models
from django.contrib.auth.models import User

class Formation(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField()
    
    def __str__(self):
        return self.nom 
    
class Session(models.Model):
    formation = models.ForeignKey(Formation)
    
    def __str__(self):
        return "Session de : " + self.formation.nom;
    
class Localisation(models.Model):
    nom = models.CharField(max_length=200)
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    
class Cours(models.Model):
    date_cours = models.DateField(auto_now_add=True)
    session = models.ForeignKey(Session, default=1)
    localisation = models.ForeignKey(Localisation, default=1)

class Catalogue(models.Model):
    nom = models.CharField(max_length=200)
    liste_formations = models.ManyToManyField(Formation)

    def __str__(self):
        return self.nom

class Entreprise(models.Model):
    nom = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nom;

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    liste_entreprises = models.ManyToManyField(Entreprise)
    liste_catalogues = models.ManyToManyField(Catalogue)
    
    def __str__(self):
        return self.user.first_name;





    




#    nom_commercial = models.CharField(max_length=200, blank=True)
#    siren = models.CharField(max_length=8, unique=True)
#    siret = models.CharField(max_length=14, unique=True)
#    adresse = models.CharField(max_length=250)
#    code_postal = models.CharField(max_length=10)
#    telephone = models.CharField(max_length=15)