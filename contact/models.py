from django.db import models


class ShortDescription(models.Model):
    text = models.TextField(max_length=300)

    def __str__(self):
        return 'Text'


class MyEmailAddress(models.Model):
    eMail = models.EmailField(default='admin@example.com')

    def __str__(self):
        return 'Adres e-mail'
