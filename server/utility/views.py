from django.http import HttpResponse
from django.http import JsonResponse
import json
from .scripts import apiCall


def index(request):
    return HttpResponse("<H1>Test</H1>")

# @ensure_csrf_cookie
def get_person(request):

    # get data from request
    dataIn = json.loads(request.body)  # {'name':'John', 'age': 42}
    print("Post Info:")
    print(dataIn['ingr'])
    ingredients = dataIn['ingr']
    dish_type_str = ""

    # make call to getRecipes function
    recipes = apiCall.get_recipes(ingredients, dish_type_str)

    # dataOut= {
    #     'id': 1234,
    #     'name': 'Calvin',
    #     'age': 6,
    #     'known associates': 'Hobbes, Suzie'
    #
    # }
    return JsonResponse(recipes, safe=False)
