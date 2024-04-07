from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'store'

router = DefaultRouter()
router.register('movies', views.MovieViewSet, basename='movies')
router.register('stars', views.StarViewSet, basename='stars')


urlpatterns = router.urls
