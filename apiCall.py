import requests
import json


# RECIPE PUPPY API DOCUMENTATION
# For example:
# http://www.recipepuppy.com/api/?i=onions,garlic&q=omelet&p=3
#
# Optional Parameters:
# i : comma delimited ingredients
# q : normal search query (ex: "omelet")
# p : page (???)
# format=xml : if you want xml instead of json

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


def generate_query_string(ingreds_list, dish_type_str):
    call_str = "http://www.recipepuppy.com/api/?"

    ingreds_str = "i="
    for i in ingreds_list:
        print(i)
        ingreds_str += i + ","
    ingreds_str = ingreds_str[:-1]

    if dish_type_str != "":
        dish_type_str = "&q=" + dish_type_str

    call_str = call_str + ingreds_str + dish_type_str

    return call_str


def main():
    # Get ingredients from user.
    ingredients = ["onions", "garlic"]

    # Get dish type search string from user.
    dish_type_str = ""

    # Create api call string.
    call_str_template = generate_query_string(ingredients, dish_type_str)
    print(call_str_template)

    # # Make GET requests to get a Response object "r" until no more results are found
    # r = requests.get("http://www.recipepuppy.com/api/?i=onions,garlic&q=omelet&p=3")
    #
    # # Test jprint r.json().
    # jprint(r.json())


if __name__ == "__main__":
    main()
