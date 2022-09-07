import imp
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from blog.models import Post
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import mixins

class PostList(ListCreateAPIView):
     ''' getting a list of posts and creating posts '''
     permission_classes = [IsAuthenticated]
     serializer_class = PostSerializer
     queryset = Post.objects.filter(status=True)

class PostDetail(RetrieveUpdateDestroyAPIView):
     ''' getting detail information of a post and updating/delete'''
     permission_classes = [IsAuthenticated]
     serializer_class = PostSerializer
     queryset = Post.objects.filter(status=True)