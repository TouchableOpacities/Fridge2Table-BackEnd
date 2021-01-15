from django.urls import path
from . import views

urlpatterns = [
    path('getRecipesFromIngredients/', views.get_recipes),   # routes to get_recipes function in views.py
]