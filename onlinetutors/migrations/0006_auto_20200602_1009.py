# Generated by Django 3.0.6 on 2020-06-02 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinetutors', '0005_auto_20200602_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='phonenumber',
            field=models.CharField(max_length=13, unique=True),
        ),
    ]