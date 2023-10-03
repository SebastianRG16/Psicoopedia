from rest_framework.views import APIView
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.hashers import make_password

from user.models import User
from user.api.serializers import UserSerializer, UserRegisteSerializer


class UserApiViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


    def create(self, request, *args, **kwargs):
        # request.data['password'] = make_password(request.data['password'])
        # return super().create(request, *args, **kwargs)
        return Response(
            {'error' : 'Metodo no disponible'}, 
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )
    
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        password = serializer.validate_data.pop('password', None)

        if password is not None:
            instance.set_password(password)
        self.perform_update(serializer)

        return Response(serializer.data)

class UserView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

class RegisterApiView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        serializer = UserRegisteSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    