# Generated by Django 3.0.6 on 2020-08-24 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinetutors', '0032_auto_20200824_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratings',
            name='rating',
            field=models.FloatField(),
        ),
    ]
