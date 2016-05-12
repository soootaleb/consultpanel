from django.db import models

class DocumentType(models.Model):
    label = models.CharField(max_length=100)
    slug = models.SlugField(max_length=110)

class Template(models.Model):
    type = models.ForeignKey('DocumentType', on_delete=models.CASCADE)
    label = models.CharField(max_length=100)
    slug = models.SlugField(max_length=110)
