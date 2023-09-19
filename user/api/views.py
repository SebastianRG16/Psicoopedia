from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from user.models import User
from user.api.serializers import UserSerializer

class UserView(APIView):
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
