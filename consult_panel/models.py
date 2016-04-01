from django.db import models
from django.contrib.auth.models import User



class Entreprise(models.Model):
    nom = models.CharField(max_length=200)
    nom_commercial = models.CharField(max_length=200, blank=True)
    siren = models.CharField(max_length=8, unique=True)
    siret = models.CharField(max_length=14, unique=True)
    adresse = models.CharField(max_length=250)
    code_postal = models.CharField(max_length=10)
    telephone = models.CharField(max_length=15)
    
    def __str__(self):
        if self.nom_commercial:
            return self.nom_commercial;
        else:
            return self.nom;
        

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    entreprise = models.ForeignKey(Entreprise)
    biography = models.CharField(max_length=200)
    def __str__(self):
        return self.first_name + " " + self.last_name;
    
    
    
    

class Formation(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    user = models.ForeignKey(User, default=1)
    
    def is_formation_of_user(self, the_user):
        return self.user.id == the_user.id;
    
    def __str__(self):
        return self.name
    



class Catalogue(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    liste_formations = models.ManyToManyField(Formation)
    user = models.ForeignKey(User, default=1)
    
    def is_catalogue_of_user(self, the_user):
        return self.user.id == the_user.id;

    def __str__(self):
        return self.name