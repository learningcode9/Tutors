# Generated by Django 3.0.3 on 2020-08-18 00:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinetutors', '0028_auto_20200611_1209'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='email',
        ),
    ]
