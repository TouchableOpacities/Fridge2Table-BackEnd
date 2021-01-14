from django.urls import path
from . import views

urlpatterns = [
    path('getRecipesFromIngredients/', views.get_person, name='index'),
]