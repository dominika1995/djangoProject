from django.db import models


class DescriptionAbout(models.Model):
    text = models.TextField()

    def __str__(self):
        return 'Text'
