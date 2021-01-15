# Handles call to RecipePuppy API. get_recipes() returns list of dictionaries representing recipes.

import requests
import json


# ---------------------------------------------------------------------------
# RECIPE PUPPY API DOCUMENTATION
# For example:
# http://www.recipepuppy.com/api/?i=onions,garlic&q=omelet&p=3
#
# Optional Parameters:
# i : comma delimited ingredients (with '-' to exclude)
# q : normal search query (ex: "omelet")
# p : page
# format=xml : if you want xml instead of json
# ---------------------------------------------------------------------------

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


def generate_query_string(ingreds_list, dish_type_str):
    call_str = "http://www.recipepuppy.com/api/?"

    ingreds_str = "i="
    for i in ingreds_list:
        ingreds_str += i + ","
    ingreds_str = ingreds_str[:-1]

    if dish_type_str != "":
        dish_type_str = "&q=" + dish_type_str

    call_str = call_str + ingreds_str + dish_type_str

    return call_str


def get_recipes(ingredients, dish_type_str):
    # Create api call string.
    call_str_template = generate_query_string(ingredients, dish_type_str)
    print(call_str_template)

    # Make GET requests to get a Response object "r"; iterate through pages until no more results are found
    all_recipes_arr = []
    page_num = 0

    while page_num < 10:
        page_num += 1
        print(page_num)
        r = requests.get(call_str_template + "&p=" + str(page_num))
        if r.status_code != 200:
            continue
        curr_page_results = r.json()['results']
        if len(curr_page_results) == 0:
            break
        all_recipes_arr = all_recipes_arr + curr_page_results

    jprint(all_recipes_arr)
    return all_recipes_arr


# ~~~~~~~~~~~~~~~~~~~~ FOR TESTING ONLY ~~~~~~~~~~~~~~~~~~~~
def main():
    test_ingreds_list = ["onions", "chicken"]
    get_recipes(test_ingreds_list, "")

if __name__ == '__main__':
    main()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
