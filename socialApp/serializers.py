from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from socialApp import models

class PostCreateUpdateSerializer(serializers.ModelSerializer):
    likes_count = serializers.ReadOnlyField()
    class Meta:
        model = models.Post
        fields = '__all__'


class CommentCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = '__all__'

class LikeCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Like
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=models.Like.objects.all(),
                fields=['normal_user', 'post']
            )
        ]