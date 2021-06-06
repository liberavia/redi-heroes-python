from django.db import models


class Kommentar(models.Model):
    autor = models.CharField(max_length=100, default='')
    kommentar = models.TextField(default='')

    def __str__(self):
        return self.autor
