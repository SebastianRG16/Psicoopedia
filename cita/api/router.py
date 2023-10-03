from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from cita.api.views import CitaView
from rest_framework import routers



router = routers.DefaultRouter()
router.register(prefix='cita', basename='cita', viewset=CitaView)

urlpatterns = [
    path('cita/', include(router.urls)),
]