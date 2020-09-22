from django.urls import path,include
from api_display import views
from api_display.views import Ratings_list
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url
from rest_framework import routers



# router = routers.DefaultRouter()
# router.register(r'ratings', Ratings_list)
# router.register(r'tutors', Tutors_list)

# urlpatterns = router.urls




urlpatterns = [
    path('ratings/', views.Ratings_list),
    # path('tutors/', views.Tutors_list),
]

urlpatterns = format_suffix_patterns(urlpatterns)


# urlpatterns = [
#     # path('article/',views.article_list,name="article"),
#     path('ratings/',views.RatingsList.as_view(),name="rating"),
#     path('tutors/',views.TutorList.as_view(),name="tutors"),
     
   
#     ]
# urlpatterns = format_suffix_patterns(urlpatterns)