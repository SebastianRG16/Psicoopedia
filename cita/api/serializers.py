from rest_framework import serializers
from cita.models import Cita
from paciente.api.serializers import PacienteSerializer
from consultorio.api.serializers import ConsultorioSerializer
from practicante.api.serializers import PracticanteSerializer

class CitaSerializer(serializers.ModelSerializer):
    id_paciente = PacienteSerializer(read_only=True)
    id_consultorio = ConsultorioSerializer(read_only=True)
    id_practicante = PracticanteSerializer(read_only=True)
    class Meta:
        model = Cita
        fields = ['id','name','id_paciente', 'id_consultorio', 'id_practicante', 'date', 'state']