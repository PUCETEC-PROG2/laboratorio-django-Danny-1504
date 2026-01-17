from django.urls import path, include
from rest_framework import routers
from . import views
from .views import TrainerViewSet, PokemonViewSet

router = routers.DefaultRouter()
router.register(r'pokemons', views.PokemonViewSet)
router.register(r'trainers', TrainerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]