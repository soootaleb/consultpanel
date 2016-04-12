# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-11 16:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalogue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Cours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_cours', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmailForBeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Entreprise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Formation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Localisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('latitude', models.CharField(max_length=200)),
                ('longitude', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liste_catalogues', models.ManyToManyField(to='consult_panel.Catalogue')),
                ('liste_entreprises', models.ManyToManyField(to='consult_panel.Entreprise')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consult_panel.Formation')),
            ],
        ),
        migrations.AddField(
            model_name='cours',
            name='localisation',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='consult_panel.Localisation'),
        ),
        migrations.AddField(
            model_name='cours',
            name='session',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='consult_panel.Session'),
        ),
        migrations.AddField(
            model_name='catalogue',
            name='liste_formations',
            field=models.ManyToManyField(to='consult_panel.Formation'),
        ),
    ]