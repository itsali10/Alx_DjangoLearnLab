from django.shortcuts import render
from rest_framework import viewsets

from social_media_api.notifications.models import Notification
from .models import Like, Post,Comment
from .serializers import PostSerializer,CommentSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from accounts.models import *
from rest_framework import permissions,generics
from rest_framework.views import APIView

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class FeedView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        following_users = request.user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
class LikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if created:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb='liked',
                target=post
            )
            return Response({'message': 'Post liked'})
        return Response({'message': 'Already liked'}, status=400)
    

class UnlikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)
        try:
            like = generics.get_object_or_404(Like, user=request.user, post=post)
            like.delete()
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb='unliked',
                target=post
            )
            return Response({'message': 'Post unliked'})
        except Like.DoesNotExist:
            return Response({'message': 'You haven’t liked this post'}, status=400)