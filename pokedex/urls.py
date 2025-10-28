from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("pokemon/<int:id>/", views.pokemon, name="pokemon"),
    path("trainers/", views.trainer_list, name="trainers"),
    path("trainers/<int:trainer_id>/", views.trainer, name="trainer"),
]