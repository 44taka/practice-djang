from rest_framework import serializers

from api import models


class SampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SampleModel
        fields = ["id", "title", "description"]