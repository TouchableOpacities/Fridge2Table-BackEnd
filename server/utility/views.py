from django.http import JsonResponse
import json
from .scripts import recipe_puppy_api


# Uses RecipePuppy API to get list of recipes with given ingredients.
# Routed from urlpattern "getRecipesFromIngredients/" in urls.py.
def get_recipes(request):

    # Get data from request (a list of strings = ingredients)
    data_in = json.loads(request.body)          # the body of the request is a list of ingredients (strings)
    ingredients = data_in['ingredients']
    dish_type_str = ""                          # placeholder for now


    # Log data received to console
    print("POST INFO: Ingredients = " + ingredients)
    print("(Dish type blank for now...)")

    # Call recipe_puppy_api.get_recipes with specified ingredients.
    # Returns list of dicts of recipes that look like:
    # [{'href': 'http://allrecipes.com/Recipe/Ds-Famous-Salsa/Detail.aspx',
    #   'ingredients': 'green chilies, garlic, lime, onions, salt',
    #   'thumbnail': 'http://img.recipepuppy.com/29584.jpg',
    #   'title': "D's Famous Salsa"}, ...]
    recipes = recipe_puppy_api.get_recipes(ingredients, dish_type_str)

    return JsonResponse(recipes, safe=False)
