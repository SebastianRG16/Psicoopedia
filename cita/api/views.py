from cita.models import Cita
from cita.api.serializers import CitaSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets


class CitaView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CitaSerializer
    queryset = Cita.objects.all()