from django.db import models
from django.conf import settings
from django.http import HttpResponse, Http404
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User

import datetime
import os
import base64


# cf. article L.6313-1 du Code du travail
class ActionFormation(models.Model):
    code = models.SmallIntegerField(unique=True)
    label = models.CharField(max_length=255)

    def __str__(self):
        return self.label


class Formation(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField()
    prix_ht = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    prix_ttc = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    action_formation = models.ForeignKey(ActionFormation, on_delete=models.PROTECT)

    def __str__(self):
        return self.nom


class Session(models.Model):
    formation = models.ForeignKey(Formation, on_delete=models.CASCADE)

    def __str__(self):
        return "Session de : " + self.formation.nom

    def get_date_debut(self):
        cours = Cours.objects.filter(
            session=self.id).order_by('date_cours_debut')
        if cours.count() > 0:
            return cours[0].get_date_debut()
        return 'Aucun cours dans cette session'


class Catalogue(models.Model):
    nom = models.CharField(max_length=200)
    liste_formations = models.ManyToManyField(Formation, blank=True)

    def __str__(self):
        return self.nom


class Entreprise(models.Model):
    nom = models.CharField(max_length=255)
    # siret = models.CharField(max_length=14, unique=True, default='DEFAULT_SIRET')
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
    representant_prenom = models.CharField(max_length=200)
    representant_nom = models.CharField(max_length=200)

    convention_url = ''

    def __str__(self):
        return "{} - {}".format(self.entreprise, self.nom)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    centre_formation = models.ForeignKey(CentreFormation, default=1, on_delete=models.CASCADE)
    liste_entreprises = models.ManyToManyField(Entreprise)
    liste_catalogues = models.ManyToManyField(Catalogue)
    signature_base64 = models.TextField(blank=True)

    def __str__(self):
        return self.user.first_name

    def get_medias_directory_simple(self):
        return str(self.user.id) + '_' + self.user.username

    def get_medias_directory(self):
        user_folder = str(self.user.id) + '_' + self.user.username
        directory = os.path.join(settings.MEDIA_ROOT, 'admin_documents', user_folder)
        if not os.path.isdir(directory):
            os.mkdir(directory)
        return directory + os.sep

    def save_signature_as_image(self):
        filepath = None
        if self.signatue_base64 != "":
            head, data = self.signature_base64.split(',', 1)
            filepath = os.path.join(self.get_medias_directory(), str(self.user_id)+"_signature.png")
            with open(filepath, "wb") as fh:
                fh.write(base64.decode(data))
                fh.close()
        return filepath

    @staticmethod
    def get_admin_medias_directory():
        return os.path.join(settings.MEDIA_ROOT, 'admin_documents')

    @staticmethod
    def validemail(**kwargs):
        id = kwargs.get('id', None)  # Récupération de l'id (envoyé dans les params)
        # Récupération de l'objet unique
        # L'objet unique est injecté automatiquement dans les kwargs par le linker.
        unique = kwargs.get('unique', None)
        if id is None:
            raise Http404
        unique.perime = True
        unique.save()
        # Récupération du profil
        profil = Profile.objects.get(id=id)

        # Validation de l'email
        profil.user.is_active = True
        profil.user.save()
        return redirect('public_login')


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
    session = models.ForeignKey(Session, default=1, on_delete=models.CASCADE)
    localisation = models.ForeignKey(Localisation, default=1, on_delete=models.CASCADE)

    @staticmethod
    def _get_formated_date(date):
        return date.strftime('%d/%m/%y')

    @staticmethod
    def _get_formated_heure(date):
        return date.strftime('%Hh%M')

    def get_date_debut(self):
        return Cours._get_formated_date(self.date_cours_debut)

    def get_heure_debut(self):
        return Cours._get_formated_heure(self.date_cours_debut)

    def get_interval(self):
        if self.date_cours_debut.date() == self.date_cours_fin.date():
            return 'Le {} de {} à {} (UTC)'.format(
                Cours._get_formated_date(self.date_cours_debut),
                Cours._get_formated_heure(self.date_cours_debut),
                Cours._get_formated_heure(self.date_cours_fin)
            )

        return 'Du {} {} au {} {} (UTC)'.format(
            Cours._get_formated_date(self.date_cours_debut),
            Cours._get_formated_heure(self.date_cours_debut),
            Cours._get_formated_date(self.date_cours_fin),
            Cours._get_formated_heure(self.date_cours_fin)
        )

    def __str__(self):
        return 'Cours de {} le {}'.format(
            self.session.formation.nom,
            self.get_date_debut()
        )


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

    def __str__(self):
        return 'Inscription: {} {} ({})'.format(
            self.prenom,
            self.nom,
            self.client
        )


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
        # Récupération de l'idée (envoyé dans les params)
        id = kwargs.get('id', None)

        # Récupération de l'objet unique
        # L'objet unique est injecté automatiquement dans les kwargs par le
        # linker.
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
