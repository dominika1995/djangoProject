from django.db import models

class PriceList(models.Model):
    id = models.AutoField(primary_key=True)
    name_of_service = models.CharField(max_length=40)
    price = models.IntegerField()
    number_of_photos = models.IntegerField()
    visible = models.BooleanField(default=True)
    def __str__(self):
        return self.name_of_service

class shortDescription(models.Model):
    text = models.TextField(max_length=300)
    def __str__(self):
        return 'Text'