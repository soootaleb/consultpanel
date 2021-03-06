# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-01-07 15:32
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Unique',
            fields=[
                ('jeton', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('methode', models.CharField(max_length=255)),
                ('params', models.TextField()),
                ('date_creation', models.DateTimeField(default=datetime.datetime.now)),
                ('perime', models.BooleanField(default=False)),
                ('auteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
