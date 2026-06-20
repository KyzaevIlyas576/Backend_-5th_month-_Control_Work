from django.shortcuts import render
from django.db.models import Q
from rest_framework import generics, permissions
from .serializers import CommentSerializer, PostSerializer
from .models import Comment, Post
from .permissions import IsOwner


class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Post.objects.filter(
                Q(is_published=True) | Q(author=user)
            )
        return Post.objects.filter(is_published=True)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get_permissions(self):
        if self.request.method in ['PUT', 'DELETE']:
            return [permissions.IsAuthenticated(), IsOwner()]
        return [permissions.AllowAny()]

class CommentListView(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs['id']
        return Comment.objects.filter(post_id=post_id)
    

class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        post_id = self.kwargs['id']
        serializer.save(
            author=self.request.user,
            post_id=post_id
        )


def perform_create(self, serializer):
    serializer.save(author=self.request.user)
