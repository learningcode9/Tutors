from django.urls import path
from django.conf.urls import include
from account import views


app_name='account'

urlpatterns = [
   
    path("signup/",views.signUp,name="signup"),
    path("login/",views.login,name="login"),
    path("registration/",views.registration,name="registration"),
    path('Logout/',views.Logout,name="logout"),
    path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate_account, name='activate'),
  
]