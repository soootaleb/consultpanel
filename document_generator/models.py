from django.db import models
import os
from consult_panel.models import Profile


def upload_destination(instance, filename):
    print(instance.profile)
    return os.path.join('admin_documents', instance.profile.get_medias_directory(), instance.label + '.pdf')


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
