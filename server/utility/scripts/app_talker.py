import json


# Receives request from frontend, returns list of ingredients
def process_incoming_data(request):
    # Get data from request (a list of strings = ingredients)
    data_in = json.loads(request.body)  # the body of the request is a list of ingredients (list of strings)
    ingredients = data_in['ingredients']

    # Log data received to console
    print("POST INFO: Ingredients = " + ingredients)
    print("(Dish type blank for now...)")

    return ingredients
