from django.urls import path, include
from rest_framework import routers
from .api import ExercicioViewSet, ExercicioViewSet


api_router = routers.DefaultRouter()
api_router.register(r"exercicio", ExercicioViewSet)

urlpatterns = [
    path("api/", include(api_router.urls)),
]