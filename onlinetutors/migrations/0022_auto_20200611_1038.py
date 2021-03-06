# Generated by Django 3.0.6 on 2020-06-11 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinetutors', '0021_auto_20200611_1034'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tutors',
            old_name='enter_days',
            new_name='enter_friday',
        ),
        migrations.RenameField(
            model_name='tutors',
            old_name='enter_timings',
            new_name='enter_fridaytimings',
        ),
        migrations.AddField(
            model_name='tutors',
            name='enter_monday',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tutors',
            name='enter_mondaytimings',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tutors',
            name='enter_saturday',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tutors',
            name='enter_saturdaytimings',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tutors',
            name='enter_sunday',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tutors',
            name='enter_sundaytimings',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tutors',
            name='enter_thursday',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tutors',
            name='enter_thursdaytimings',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tutors',
            name='enter_tuesday',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tutors',
            name='enter_tuesdaytimings',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tutors',
            name='enter_wednesday',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tutors',
            name='enter_wednesdaytimings',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
