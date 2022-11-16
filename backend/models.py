from django.db import models

class Odam(models.Model):
    ismi = models.CharField(max_length=30)
    familais = models.CharField(max_length=30)
    yoshi = models.IntegerField()
