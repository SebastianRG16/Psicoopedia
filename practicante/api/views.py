from practicante.models import Practicante
from practicante.api.serializers import PracticanteSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets


class PracticanteView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PracticanteSerializer
    queryset = Practicante.objects.all()