import json
from .recipe_class import Recipe


# Receives request from frontend, returns list of ingredients
def process_incoming_data(request):
    # Get data from request (a list of strings = ingredients)
    data_in = json.loads(request.body)  # the body of the request is a list of ingredients (list of strings)
    ingredients = data_in['ingredients']

    # Log data received to console
    print("POST INFO: Ingredients = " + str(ingredients))
    print("(Dish type blank for now...)")

    return ingredients


# Parse RecipePuppy result. Returns a list of Recipe objects.
def process_query_result(query_result):
    # Turn each dict in the query result into a Recipe object.
    recipes = []
    for rec in query_result:
        recipes.append(Recipe(rec["href"], rec["ingredients"], rec["thumbnail"], rec["title"]))

    # ... DO SOME STUFF ...
    for recipe in recipes:
        recipe.replace_thumbnail()
        recipe.clean_title()

    # "Dictify" each recipe and return list of dicts ready for sending to frontend as JSON
    result = []
    for recipe in recipes:
        result.append(recipe.dictify())

    return result
