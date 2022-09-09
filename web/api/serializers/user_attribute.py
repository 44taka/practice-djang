from rest_framework import serializers

from api import models


class UserAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserAttributeModel
        fields = '__all__'
