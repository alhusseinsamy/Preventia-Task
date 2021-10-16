from rest_framework import serializers
from usersApp import models

class CreateUpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NormalUser
        fields = '__all__'

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        try:
            user = models.NormalUser.objects.create_user(**validated_data)
        except ValueError as e:
            raise serializers.ValidationError(
                {'details': [e]}
            )
        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
            instance.save()

        return super().update(
            instance, validated_data)