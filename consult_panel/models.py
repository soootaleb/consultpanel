import datetime
import os

from django.contrib.auth.models import User
from django.db import models
from django.http import HttpResponse

from consult_panel.settings import MEDIA_ROOT

def get_signature_path(instance, filename):
    return os.path.join(instance.get_medias_directory, "signature.jpg")

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

    def get_date_debut(self):
        cours = Cours.objects.filter(
            session=self.id).order_by('date_cours_debut')
        return cours[0].date_cours_debut if cours.count() > 0 else 'Aucun cours dans cette session'


class Catalogue(models.Model):
    nom = models.CharField(max_length=200)
    liste_formations = models.ManyToManyField(Formation, blank=True)

    def __str__(self):
        return self.nom


class Entreprise(models.Model):
    nom = models.CharField(max_length=255)
    siret = models.CharField(
        max_length=14, unique=True, default='DEFAULT_SIRET')
    adresse = models.CharField(max_length=255, default='DEFAULT_ADDR')
    ville = models.CharField(max_length=255, default='DEFAULT_VILLE')
    code_postal = models.CharField(max_length=10, default='DEFAULT_CP')
    telephone = models.CharField(max_length=15, default='DEFAULT_PHONE')

    def __str__(self):
        return self.nom


class CentreFormation(models.Model):
    nom = models.CharField(max_length=255)
    siret = models.CharField(
        max_length=14, unique=True, default='DEFAULT_SIRET')
    adresse = models.CharField(max_length=255, default='DEFAULT_ADDR')
    ville = models.CharField(max_length=255, default='DEFAULT_VILLE')
    code_postal = models.CharField(max_length=10, default='DEFAULT_CP')
    telephone = models.CharField(max_length=15, default='DEFAULT_PHONE')

    def __str__(self):
        return self.nom


class Client(models.Model):
    nom = models.CharField(max_length=200)
    catalogue = models.ForeignKey(
        Catalogue, on_delete=models.CASCADE, default=1)
    entreprise = models.ForeignKey(
        Entreprise, on_delete=models.CASCADE, default=1)

    convention_url = ''

    def __str__(self):
        return self.nom


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    centre_formation = models.ForeignKey(CentreFormation, default=1)
    liste_entreprises = models.ManyToManyField(Entreprise)
    liste_catalogues = models.ManyToManyField(Catalogue)
    signature = models.ImageField(upload_to=get_signature_path , blank=True)

    def __str__(self):
        return self.user.first_name

    def get_medias_directory_simple(self):
        return str(self.user.id) + '_' + self.user.username

    def get_medias_directory(self):
        user_folder = str(self.user.id) + '_' + self.user.username
        directory = os.path.join(MEDIA_ROOT, 'admin_documents', user_folder)
        if not os.path.isdir(directory):
            os.mkdir(directory)
        return directory + os.sep



class Localisation(models.Model):
    nom = models.CharField(max_length=200)
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default=2)

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


class PreferenceType(models.Model):
    label = models.CharField(max_length=100)


class Preference(models.Model):
    type = models.ForeignKey(PreferenceType, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)


class Inscription(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, default=1)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, default=1)


"""
Landing page models
"""


class EmailForBeta(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


"""
Debug models
"""


class DebugValidateEmail(models.Model):
    email = models.EmailField(unique=False)
    is_valid = models.BooleanField(default=False)

    def __str__(self):
        return "{} ({})".format(self.email, 'VALID' if self.is_valid else 'UNVALID')

    @staticmethod
    def valid(**kwargs):
        id = kwargs.get('id', None)  # Récupération de l'idée (envoyé dans les params)

        # Récupération de l'objet unique
        # L'objet unique est injecté automatiquement dans les kwargs par le linker.
        unique = kwargs.get('unique', None)

        if id is None:
            return HttpResponse('<pre>Param \'id\' requis.</pre>')

        # À faire seulement si vous désirez que le lien ne soit plus
        # utilisable par la suite
        unique.perime = True
        unique.save()

        # Récupération de l'objet DebugValidateEmail
        obj = DebugValidateEmail.objects.get(id=id)

        # Validation de l'email
        obj.is_valid = True
        obj.save()

        return HttpResponse('<pre>{} is now valid and {} obsolete.</pre>'.format(obj.email, unique.jeton))
