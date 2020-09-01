from django.urls import path,include
from api_basic import views
from api_basic.views import GenericAPIView,ArticleViewSet,ArticleAPIView
from rest_framework.routers import DefaultRouter



app_name='api_basic'

router = DefaultRouter()
router.register('article',ArticleViewSet,basename='article')

urlpatterns = [
    # path('article/',views.article_list,name="article"),
    path('article/',ArticleAPIView.as_view()),
    # path('article_detail/<int:pk>/',views.article_detail,name="article_detail"),
    # path('detail/<int:id>/',ArticleDetails.as_view()),
    path('viewset/',include(router.urls)),
    path('genericarticle/<int:id>/',GenericAPIView.as_view()),
    ]