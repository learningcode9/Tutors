# Generated by Django 3.0.6 on 2020-09-17 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlinetutors', '0044_auto_20200917_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratings',
            name='tutorname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tutorname', to='onlinetutors.tutors'),
        ),
        migrations.AlterField(
            model_name='tutors',
            name='name',
            field=models.CharField(db_index=True, max_length=100),
        ),
    ]
