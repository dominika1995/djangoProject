# Generated by Django 2.1.4 on 2019-01-07 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PriceList',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name_of_service', models.CharField(max_length=40)),
                ('price', models.IntegerField()),
                ('number_of_photos', models.IntegerField()),
            ],
        ),
    ]
