# Generated by Django 3.2.6 on 2021-09-30 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='image',
            field=models.URLField(),
        ),
    ]
