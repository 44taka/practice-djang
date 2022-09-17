from django.db import models
from api.models.sample import SampleModel


class SampleAttributeModel(models.Model):
    attr1 = models.CharField(max_length=50, db_index=True)
    attr2 = models.CharField(max_length=50, db_index=True)
    attr3 = models.CharField(max_length=50, db_index=True)
    attr4 = models.CharField(max_length=50, db_index=True)
    attr5 = models.CharField(max_length=50, db_index=True)
    sample = models.ForeignKey(SampleModel, on_delete=models.CASCADE, related_name='attributes')

    class Meta:
        db_table = 'sample_attribute_tbl'
