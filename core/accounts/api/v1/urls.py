from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

app_name = "api-v1"
urlpatterns = [
    # registration
    path("registration/", views.RegisterationApiView.as_view(), name="registration"),
    # password-change
    path(
        "password-change/",
        views.PasswordChangeApiView.as_view(),
        name="password-change",
    ),
    # login token
    path("token/login/", views.CustomObtainAuthToken.as_view(), name="token-login"),
    path("token/logout/", views.CustomDiscardAuthToken.as_view(), name="token-logout"),
    # profile
    path("profile/", views.ProfileApiView.as_view(), name="profile"),
    # activate
    path("test-email/", views.TestEmailView.as_view(), name="test-email"),
    path(
        "activation/confirm/<str:token>",
        views.ActivationView.as_view(),
        name="activation",
    ),
    # reset activate
    path("activation/resent/", views.ActivationRestView.as_view(), name="resent"),
    # jwt
    path("jwt/create/", views.CustomTokenObtainPairView.as_view(), name="jwt-create"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="jwt-refresh"),
    path("jwt/verify/", TokenVerifyView.as_view(), name="jwt-verify"),
]
