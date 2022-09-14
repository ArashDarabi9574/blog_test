from django.urls import path, include

from . import views

app_name = 'api-v1'
urlpatterns = [
     # registration
     path('registration/', views.RegisterationApiView.as_view(), name='registration'),

     # login
     path('token/login/', views.CustomObtainAuthToken.as_view(), name='token-login'),
     path('token/logout/', views.CustomDiscardAuthToken.as_view(), name='token-logout'),
]
