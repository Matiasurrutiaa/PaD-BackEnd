from django.urls import path, include
from rest_framework import routers
from noticias import views

from . import views

router = routers.DefaultRouter()
router.register(r'news', views.NewsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]