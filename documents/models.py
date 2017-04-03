from django.db import models
import os
from consult_panel.models import Profile, Client, Session


def upload_destination(instance, filename):
    return os.path.join('admin_documents', instance.profile.get_medias_directory(), instance.label + '.pdf')


class Convention(models.Model):
    client = models.ForeignKey(Client)
    session = models.ForeignKey(Session)
    signed_by_client = models.BooleanField(default=False)
    signed_by_formateur = models.BooleanField(default=False)
    document = models.FileField(
        upload_to=upload_destination, default="DEFAULT_CONVENTION_DOCUMENT")


class DocumentType(models.Model):
    label = models.CharField(max_length=100)
    slug = models.SlugField(max_length=110)

    def __str__(self):
        return self.label


class Template(models.Model):
    type = models.ForeignKey('DocumentType', on_delete=models.CASCADE)
    label = models.CharField(max_length=100)
    slug = models.SlugField(max_length=110)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    document = models.FileField(upload_to=upload_destination, max_length=500)

    def __str__(self):
        return self.label
