import imp
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer,CategorySerializer
from blog.models import Category, Post
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import mixins
from rest_framework import viewsets
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from .paginations import LargeResultsSetPagination


class PostModelViewSet(viewsets.ModelViewSet):
     permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
     serializer_class = PostSerializer
     queryset = Post.objects.filter(status=True)
     filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
     filterset_fields = ['author', 'category','status']
     search_fields = ['title', 'content']
     ordering_fields = ['published_data']
     pagination_class = LargeResultsSetPagination

class CategoryModelViewSet(viewsets.ModelViewSet):
     permission_classes = [IsAuthenticatedOrReadOnly]
     serializer_class = CategorySerializer
     queryset = Category.objects.all()