from paciente.models import Paciente
from paciente.api.serializers import PacienteSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets


class PacienteView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PacienteSerializer
    queryset = Paciente.objects.all()