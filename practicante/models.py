from django.db import models

# Create your models here.
class Practicante(models.Model):
    name = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    type = models.CharField(max_length=100)