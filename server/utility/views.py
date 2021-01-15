from django.http import HttpResponse
from django.http import JsonResponse
import json
from .scripts import recipe_puppy_api




# @ensure_csrf_cookie
def get_person(request):

    # get data from request
    dataIn = json.loads(request.body)  # {'name':'John', 'age': 42}
    print("Post Info:")
    print(dataIn['ingredients'])
    ingredients = dataIn['ingredients']
    dish_type_str = ""

    # make call to getRecipes function
    recipes = recipe_puppy_api.get_recipes(ingredients, dish_type_str)

    # dataOut= {
    #     'id': 1234,
    #     'name': 'Calvin',
    #     'age': 6,
    #     'known associates': 'Hobbes, Suzie'
    #
    # }
    return JsonResponse(recipes, safe=False)
