from django.db import models
from django.contrib.auth.models import User
import os
from consult_panel.settings import MEDIA_ROOT

import datetime


class Formation(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField()
    prix_ht = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    prix_ttc = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return self.nom


class Session(models.Model):
    formation = models.ForeignKey(Formation)

    def __str__(self):
        return "Session de : " + self.formation.nom


class Localisation(models.Model):
    nom = models.CharField(max_length=200)
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)

    def __str__(self):
        return self.nom


class Cours(models.Model):
    date_cours_debut = models.DateTimeField(default=datetime.datetime.now)
    date_cours_fin = models.DateTimeField(default=datetime.datetime.now)
    session = models.ForeignKey(Session, default=1)
    localisation = models.ForeignKey(Localisation, default=1)

    def get_date_debut(self):
        return self.date_cours_debut.strftime('%d/%m/%y')

    def get_heure_debut(self):
        return self.date_cours_debut.strftime('%Hh%M')

    def __str__(self):
        return 'Cours de ' + str(self.session.formation.nom) + ' le ' + self.get_date_debut()


class Catalogue(models.Model):
    nom = models.CharField(max_length=200)
    liste_formations = models.ManyToManyField(Formation, blank=True)

    def __str__(self):
        return self.nom


class Entreprise(models.Model):
    nom = models.CharField(max_length=200)

    def __str__(self):
        return self.nom


class Client(models.Model):
    nom = models.CharField(max_length=200)
    catalogue = models.ForeignKey(
        Catalogue, on_delete=models.CASCADE, default=1)
    entreprise = models.ForeignKey(
        Entreprise, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.nom


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # A ForeignKey would be okay (One entreprise == One formateur == One profile)
    # ManyToMany for entreprises account (with multiple formateurs)
    liste_entreprises = models.ManyToManyField(Entreprise)
    liste_catalogues = models.ManyToManyField(Catalogue)

    def __str__(self):
        return self.user.first_name

    def get_medias_directory_simple(self):
        return str(self.user.id) + '_' + self.user.username

    def get_medias_directory(self):
        user_folder = str(self.user.id) + '_' + self.user.username
        directory = os.path.join(MEDIA_ROOT, 'admin_documents', user_folder)
        if not os.path.isdir(directory):
            os.mkdir(directory)
        return directory


class PreferenceType(models.Model):
    label = models.CharField(max_length=100)


class Preference(models.Model):
    type = models.ForeignKey(PreferenceType, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)


"""
Landing page models
"""


class EmailForBeta(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


#    nom_commercial = models.CharField(max_length=200, blank=True)
#    siren = models.CharField(max_length=8, unique=True)
#    siret = models.CharField(max_length=14, unique=True)
#    adresse = models.CharField(max_length=250)
#    code_postal = models.CharField(max_length=10)
#    telephone = models.CharField(max_length=15)
