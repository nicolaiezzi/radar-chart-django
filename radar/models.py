from django.db import models

class SauvegardeRadar(models.Model):
    nom = models.CharField(max_length=200)
    date_sauvegarde = models.DateTimeField(auto_now_add=True)
    parametres = models.JSONField(default=dict)
