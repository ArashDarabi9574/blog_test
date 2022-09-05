from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from blog.models import Post
from rest_framework import status
from django.shortcuts import get_object_or_404
@api_view()
def PostList(request):
     posts = Post.objects.filter(status=True)
     serializer = PostSerializer(posts,many=True)
     return Response(serializer.data)



@api_view()
def PostDetail(request, id):
     try:
          # post = get_object_or_404(Post, pk=id) 
          post = Post.objects.get(pk=id,status=True)
          serializer = PostSerializer(post)
          return Response(serializer.data)
     except Post.DoesNotExist:
          return Response({'detail':'psot does not exist'},status=status.HTTP_404_NOT_FOUND)