from django.db import models


class Kommentar(models.Model):
    autor = models.CharField(max_length=100, default='')
    kommentar = models.TextField(default='')

    def __str__(self):
        return self.autor


class Charakter(models.Model):
    name = models.CharField(max_length=150)
    bild = models.CharField(max_length=255)
    funktion = models.CharField(max_length=255, null=True)
    familie = models.BooleanField(default=False)

    def __str__(self):
        return self.name
