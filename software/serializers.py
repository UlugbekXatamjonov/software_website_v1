from rest_framework import serializers
from .models import *


class GameCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Game_Category
        fields = ('__all__')


class SoftwareCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Software_Category
        fields = ('__all__')


class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = ('__all__')


class SoftwareSerializer(serializers.ModelSerializer):
    
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Software
        fields = ('__all__')


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('__all__')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'name', 'software', 'body','created_at','status']
        # fields = ['__all__']


    def create(self, validated_data):
        return Comment(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.name = validated_data.get('name', instance.name)
        instance.software = validated_data.get('software', instance.software)
        instance.body = validated_data.get('body', instance.body)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.status = validated_data.get('status', instance.status)
        
        instance.save()
        return instance