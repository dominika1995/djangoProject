# Generated by Django 2.1.4 on 2019-01-13 18:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfoliocatalog',
            name='data',
            field=models.DateField(default=datetime.date(2019, 1, 13)),
        ),
    ]