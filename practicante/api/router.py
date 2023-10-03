from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from practicante.api.views import PracticanteView
from rest_framework import routers



router = routers.DefaultRouter()
router.register(prefix='practicante', basename='practicante', viewset=PracticanteView)

urlpatterns = [
    path('practicantes/', include(router.urls)),
]