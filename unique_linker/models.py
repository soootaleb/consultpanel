import json
import uuid
from _datetime import datetime
from importlib import import_module

from django.contrib.auth.models import User
from django.db import models

from unique_linker.UniqueLinkerException import UniqueLinkerException


class Unique(models.Model):
    jeton = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    auteur = models.ForeignKey(to=User)
    methode = models.CharField(max_length=255) #module/object/method
    params = models.TextField()
    date_creation = models.DateTimeField(default=datetime.now)
    perime = models.BooleanField(default=False)

    def __init__(self, *args, **kwargs):
        params = kwargs.get('params', None)
        try:
            json_object = json.loads(params)
        except TypeError:
            kwargs['params'] = json.dumps(params)
        super().__init__(*args, **kwargs)

    def __str__(self):
        return "Jeton: {}\nAuteur: {}\nMethode: {}\nParams: {}\nDate Creation: {}\nPerime: {}\n"\
            .format(self.jeton, self.auteur, self.methode, self.params, self.date_creation, self.perime)

    def exec_methode(self):
        refs = self.methode.split('/')

        if len(refs) != 3:
            raise UniqueLinkerException("Invalid 'methode' fideld. (Format: module/object/method)")

        module = import_module(refs[0])
        object = getattr(module, refs[1])
        method = getattr(object, refs[2])

        params = json.loads(self.params)

        params['unique'] = self

        return method(**params)

    def get_url(self):
        return '/u/{}'.format(self.jeton.hex)