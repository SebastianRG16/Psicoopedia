from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from user.api.views import UserView

urlpatterns = [
    path('auth/login', TokenObtainPairView.as_view()),
    path('auth/me', UserView.as_view()),
]