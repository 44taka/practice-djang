from rest_framework import serializers

from api import models
from api.serializers.sample_attribute import SampleAttributeSerializer


class SampleSerializer(serializers.ModelSerializer):
    attributes = SampleAttributeSerializer(many=True)

    class Meta:
        model = models.SampleModel
        fields = ['id', 'title', 'description', 'attributes']
