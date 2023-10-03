from consultorio.models import Consultorio
from consultorio.api.serializers import ConsultorioSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets


class ConsultorioView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ConsultorioSerializer
    queryset = Consultorio.objects.all()