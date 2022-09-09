import imp
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer,CategorySerializer
from blog.models import Category, Post
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import mixins
from rest_framework import viewsets

class PostModelViewSet(viewsets.ModelViewSet):
     permission_classes = [IsAuthenticated]
     serializer_class = PostSerializer
     queryset = Post.objects.filter(status=True)

class CategoryModelViewSet(viewsets.ModelViewSet):
     permission_classes = [IsAuthenticated]
     serializer_class = CategorySerializer
     queryset = Category.objects.all()