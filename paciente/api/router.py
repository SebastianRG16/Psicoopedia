from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from paciente.api.views import PacienteView
from rest_framework import routers



router = routers.DefaultRouter()
router.register(prefix='paciente', basename='paciente', viewset=PacienteView)

urlpatterns = [
    path('pacientes/', include(router.urls)),
]