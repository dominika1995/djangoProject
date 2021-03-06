from django.db import models
from datetime import *


class PortfolioCatalog(models.Model):
    id = models.AutoField(primary_key=True)
    data = models.DateField(default=date.today())
    name = models.CharField(max_length=100)

    def __str__(self): return self.name


class Image(models.Model):
    catalog = models.ForeignKey(PortfolioCatalog, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')


class ShortDescription(models.Model):
    text = models.TextField(max_length=300)

    def __str__(self): return 'Text'
