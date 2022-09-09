from rest_framework import serializers
from blog.models import Category, Post
class PostSerializer(serializers.ModelSerializer):
     class Meta:
          model = Post
          fields = ['id', 'author', 'title','category', 'content', 'status', 'created_date', 'published_data']

class CategorySerializer(serializers.ModelSerializer):

     class Meta:
          model = Category
          fields = ['id', 'name']