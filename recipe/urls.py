from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_recipe_intro, name="get_recipe_intro"),
    path("details", views.get_recipe_details, name="get_recipe_details"),
]