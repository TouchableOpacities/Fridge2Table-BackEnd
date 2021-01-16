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

# determines # of additional ingredients in recipe
def num_of_additional_ingredients(recipe, givenIngredients):
    print(recipe.title)
    print(recipe.ingred_list)
    print(givenIngredients)
    add_ingred = 0
    for ingr in recipe.ingred_list:
        found = False
        for given in givenIngredients:
            if ingr == given:
                found = True
        if not found:
            add_ingred += 1

    print(add_ingred)
    return add_ingred


# Parse RecipePuppy result. Returns a list of Recipe objects.
def process_query_result(query_result, given_ingredients):
    # Turn each dict in the query result into a Recipe object.
    recipes = []
    for rec in query_result:
        recipes.append(Recipe(rec["href"], rec["ingredients"], rec["thumbnail"], rec["title"]))

    # ... DO SOME STUFF ...
    for recipe in recipes:
        recipe.replace_thumbnail()
        recipe.clean_title()

    recipes.sort(key=lambda x: num_of_additional_ingredients(x, given_ingredients))

    # "Dictify" each recipe and return list of dicts ready for sending to frontend as JSON
    result = []
    for recipe in recipes:
        result.append(recipe.dictify())

    return result
