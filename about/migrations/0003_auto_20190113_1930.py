# Generated by Django 2.1.4 on 2019-01-13 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_remove_descriptionabout_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='descriptionabout',
            name='text',
            field=models.TextField(),
        ),
    ]
