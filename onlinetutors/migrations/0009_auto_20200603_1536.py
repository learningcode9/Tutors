# Generated by Django 3.0.6 on 2020-06-03 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinetutors', '0008_application_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='Gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'other')], max_length=50),
        ),
    ]