# Generated by Django 3.0.6 on 2020-06-03 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinetutors', '0007_auto_20200603_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='resume',
            field=models.FileField(null=True, upload_to='resume/'),
        ),
    ]