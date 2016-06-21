from django.contrib import admin

from .models import *

admin.site.register(Formation)
admin.site.register(Session)
admin.site.register(Catalogue)
admin.site.register(Entreprise)
admin.site.register(Client)
admin.site.register(Profile)
admin.site.register(Localisation)
admin.site.register(Cours)
admin.site.register(Inscription)

admin.site.register(PreferenceType)
admin.site.register(Preference)

admin.site.register(EmailForBeta)
