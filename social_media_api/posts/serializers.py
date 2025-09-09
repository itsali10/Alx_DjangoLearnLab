from .models import *
from rest_framework import serializers
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'author', 'content', 'created_at', 'updated_at', 'title']
    
    def validate(self, attrs):
        return super().validate(attrs)

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at', 'updated_at']

    def validate(self, attrs):
        return super().validate(attrs)

