from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from consultorio.api.views import ConsultorioView
from rest_framework import routers



router = routers.DefaultRouter()
router.register(prefix='consultorio', basename='consultorio', viewset=ConsultorioView)

urlpatterns = [
    path('consultorio/', include(router.urls)),
]