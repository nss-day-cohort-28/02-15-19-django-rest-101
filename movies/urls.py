from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from movies import views

router = DefaultRouter()
router.register('movies', views.MovieViewSet)
router.register('directors', views.DirectorViewSet)

urlpatterns = [
  path('api/v1/', include(router.urls))
]
