# Generated by Django 3.0.6 on 2020-06-10 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinetutors', '0016_auto_20200610_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutors',
            name='end_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='tutors',
            name='start_time',
            field=models.DateTimeField(null=True),
        ),
    ]