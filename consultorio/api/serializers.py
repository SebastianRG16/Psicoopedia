from rest_framework import serializers
from consultorio.models import Consultorio

class ConsultorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultorio
        fields = '__all__'