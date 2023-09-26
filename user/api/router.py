from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from user.api.views import UserView, UserApiViewSet


router_user = DefaultRouter()
router_user.register(prefix='users', basename='users', viewset=UserApiViewSet)

urlpatterns = [
    path('auth/login', TokenObtainPairView.as_view()),
    path('auth/me', UserView.as_view()),
]