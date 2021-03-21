from django.db import models


class Namensliste(models.Model):
    name = models.CharField(max_length=100)
    punkte = models.IntegerField(default=0)

    def __str__(self):
        return self.name
