from django.shortcuts import render
from rest_framework import authentication, permissions, viewsets, views, filters
from django_filters.rest_framework import DjangoFilterBackend
from socialApp import serializers
from socialApp import models
from socialApp import paginations

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = serializers.PostCreateUpdateSerializer
    queryset = models.Post.objects.all()
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['title', 'id', 'created_at']
    filterset_fields = ['normal_user',]
    pagination_class = paginations.StandardResultsSetPagination
    
    def create(self, request, *args, **kwargs):
        for key in ['user']:
            request.data.pop(key, None)
        request.data['normal_user'] = request.user.id
        return super().create(request, *args, **kwargs)


class CommentViewSet(viewsets.ModelViewSet):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = serializers.CommentCreateUpdateSerializer
    queryset = models.Comment.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['post',]
    
    def create(self, request, *args, **kwargs):
        for key in ['user']:
            request.data.pop(key, None)
        request.data['normal_user'] = request.user.id
        return super().create(request, *args, **kwargs)

class LikeViewSet(viewsets.ModelViewSet):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = serializers.LikeCreateUpdateSerializer
    queryset = models.Like.objects.all()
    
    def create(self, request, *args, **kwargs):
        for key in ['user']:
            request.data.pop(key, None)
        request.data['normal_user'] = request.user.id
        return super().create(request, *args, **kwargs)

