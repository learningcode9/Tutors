from django.urls import path
from onlinetutors import views

app_name='onlinetutors'

urlpatterns = [
    path("",views.home,name='home'),
    path("Arts/",views.arts,name="Arts"),
    path(r'^(?P<category_slug>[-\w]+)/$', views.arts, name='arts'),
    path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.tutor_detail, name='tutor_detail'),
    path("tutorprofile/",views.profile,name="tutorprofile"),
     path("application/",views.application,name="application"),
    path("checkout/",views.checkout,name="checkout"),

   
    ]