from django.urls import path
from . import views

urlpatterns = [
    path('getRecipesFromIngredients/', views.get_recipes, name='person'),
]