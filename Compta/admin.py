from django.contrib import admin

from .import models

admin.site.register(models.Etudiant)
admin.site.register(models.Frais)
admin.site.register(models.Transaction)
admin.site.register(models.Annee)
