from django.http import JsonResponse
from server.utility.scripts import utils
from server.utility.scripts import recipe_puppy


# Uses RecipePuppy API to get list of recipes with given ingredients.
# Routed from urlpattern "getRecipesFromIngredients/" in urls.py.
def get_recipes(request):
    # Receive request from app, get list of ingredients (list of strings)
    ingredients = utils.process_incoming_data(request)

    # Query RecipePuppy for specified list of ingredients
    # Returns list of dicts of recipes that look like:
    # [{'href': 'http://allrecipes.com/Recipe/Ds-Famous-Salsa/Detail.aspx',
    #   'ingredients': 'green chilies, garlic, lime, onions, salt',
    #   'thumbnail': 'http://img.recipepuppy.com/29584.jpg',
    #   'title': "D's Famous Salsa"}, ...]
    query_result = recipe_puppy.get_recipes(ingredients, "", 10)  # empty string placeholder for, e.g., "omelet"

    # Process query results. Result is final list of dictionaries for returning to frontend.
    final_result = utils.process_query_result(query_result)

    return JsonResponse(final_result, safe=False)
