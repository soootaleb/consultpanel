# Generated by Django 2.0.5 on 2018-05-13 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consult_panel', '0011_remove_formation_prix_ttc'),
    ]

    operations = [
        migrations.AddField(
            model_name='entreprise',
            name='siret',
            field=models.CharField(default='DEFAULT_SIRET', max_length=14, unique=True),
        ),
    ]
