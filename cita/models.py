from django.db import models
from paciente.models import Paciente
from consultorio.models import Consultorio
from practicante.models import Practicante


# Create your models here.
class Cita(models.Model):
    name = models.CharField(max_length=100)
    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    id_consultorio = models.ForeignKey(Consultorio, on_delete=models.CASCADE)
    id_practicante = models.ForeignKey(Practicante, on_delete=models.CASCADE)
    date = models.DateTimeField()
    state = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.name)