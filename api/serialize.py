from rest_framework import serializers
from api import models
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Tag
        fields='__all__'
class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Car
        tags=TagSerializer(many=True,read_only=True)
        fields="__all__"