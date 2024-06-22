from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'store'

router = DefaultRouter()
router.register('movies', views.MovieViewSet)
router.register('stars', views.StarViewSet)
router.register('reviews', views.ReviewViewSet)
router.register('comments', views.CommentViewSet)
router.register('genres', views.GenreViewSet)


urlpatterns = router.urls
