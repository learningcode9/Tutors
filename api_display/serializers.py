from rest_framework import serializers
from django.contrib.auth.models import User
from onlinetutors.models import ratings,tutors
import datetime


class RatingsSerializer(serializers.ModelSerializer):
 
    class Meta:
        model =  ratings
        fields = ["rating","username","tutorname","created_date"]
    
  

class TutorSerializer(serializers.ModelSerializer):

    class Meta:
         model = tutors
         fields=["name"]


