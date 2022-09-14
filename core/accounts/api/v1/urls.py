from django.urls import path, include
from . import views

app_name = 'api-v1'
urlpatterns = [
     path('registration/', views.RegisterationApiView.as_view(), name='registration'),
]