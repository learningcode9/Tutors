from onlinetutors.models import ratings
from rest_framework import serializers
from django.contrib.auth.models import User
from onlinetutors.models import tutors


class RatingSerializer(serializers.ModelSerializer):
    model=ratings
    fields=[rating,tutorname,created_date,updated]
    