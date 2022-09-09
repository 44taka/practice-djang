from rest_framework import serializers

from api import models
from api.serializers.user_attribute import UserAttributeSerializer


class UserInfoSerializer(serializers.ModelSerializer):
    attributes = UserAttributeSerializer(many=True)

    class Meta:
        model = models.UserInfoModel
        fields = ["username", "password", "info", "attributes"]
