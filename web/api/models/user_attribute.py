from django.db import models
from api.models.user_info import UserInfoModel


class UserAttributeModel(models.Model):
    attr1 = models.CharField(max_length=50, db_index=True)
    attr2 = models.CharField(max_length=50, db_index=True)
    attr3 = models.CharField(max_length=50, db_index=True)
    attr4 = models.CharField(max_length=50, db_index=True)
    attr5 = models.CharField(max_length=50, db_index=True)
    user_info = models.ForeignKey(UserInfoModel, on_delete=models.CASCADE, related_name='attributes')

    class Meta:
        db_table = "user_attribute_tbl"
