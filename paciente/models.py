from django.db import models

# Create your models here.

class Paciente(models.Model):
    name = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    dateBirth = models.DateTimeField()
    identification = models.IntegerField()
    genre = models.CharField(max_length=100)
    celphone = models.IntegerField()
    residentialArea = models.CharField(max_length=100)
    maritalStatus = models.CharField(max_length=100)
    rh = models.CharField(max_length=100)
    creed = models.CharField(max_length=100)