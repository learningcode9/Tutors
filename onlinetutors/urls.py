from django.urls import path
from onlinetutors import views


app_name='onlinetutors'

urlpatterns = [
    
    path("",views.home,name='home'),
    path("Arts/",views.arts,name="Arts"),
    path(r'^(?P<category_slug>[-\w]+)/$', views.arts, name='arts'),
    path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.tutor_detail, name='tutor_detail'),
    path("tutorprofile/",views.profile,name="tutorprofile"),
    # path("registration/",views.registration,name="registration"),
    path("thankyou/",views.thankyou,name="thankyou"),
    path("checkout/",views.checkout,name="checkout"),
   
    path('add_comments/<int:pk>/',views.AddCommentView,name="add_comments"),
    path('ratings/<int:pk>/',views.ratings,name="ratings"),
    path('datePicker',views.datePicker,name="datePicker"),
    # path(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$', views.AddCommentView,name="add_comments"), 
   
    
    ]