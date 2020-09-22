from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User
from onlinetutors.models import ratings,tutors
from api_display.serializers import RatingsSerializer
from rest_framework import generics
from django.db.models import Avg
from rest_framework.generics import ListAPIView
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.authentication import SessionAuthentication,BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated



# class RatingsViewList(viewsets.ModelViewSet):
#     queryset = ratings.objects.all()
#     serializer_class = RatingsSerializer


# class TutorsViewList(viewsets.ModelViewSet):
#     queryset = tutors.objects.all()
#     serializer_class = TutorSerializer

@api_view(['GET', 'POST'])
def Ratings_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    
    if request.method == 'GET':
        Rating = ratings.objects.all()
        serializer = RatingsSerializer(Rating, many=True)
        
        return Response(serializer.data)

    elif request.method == 'POST':
        print(request.data)
        serializer = RatingsSerializer(data=request.data)
        # print(serializer.data)
        # print(request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def Tutors_list(request):
    """
    List all code snippets, or create a new snippet.
    """

    if request.method == 'GET':
        Tutor = tutors.objects.all()
        
        serializer = TutorSerializer(Tutor, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer =TutorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)