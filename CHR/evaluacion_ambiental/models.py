from django.db import models
import json

# Create your models here.
class Project(models.Model):
    id = models.IntegerField(verbose_name="N°", primary_key=True)
    name = models.CharField(verbose_name="Nombre", max_length=100, null=True, blank=True)
    type = models.CharField(verbose_name="Tipo", max_length=10, null=True, blank=True)
    region = models.CharField(verbose_name="Región", max_length=50, null=True, blank=True)
    typology = models.CharField(verbose_name="Tipología", max_length=10, null=True, blank=True)
    holder = models.CharField(verbose_name="Titular", max_length=100, null=True, blank=True)
    investment = models.FloatField(verbose_name="Inversión", null=True, blank=True)
    presentation_date = models.DateField(verbose_name="Fecha Presentación", null=True, blank=True)
    state = models.CharField(verbose_name="Estado", max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
    