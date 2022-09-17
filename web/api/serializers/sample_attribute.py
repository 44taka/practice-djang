from rest_framework import serializers

from api import models


class SampleAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SampleAttributeModel
        fields = '__all__'
