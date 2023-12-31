from rest_framework import serializers
from practicante.models import Practicante

class PracticanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Practicante
        fields = '__all__'