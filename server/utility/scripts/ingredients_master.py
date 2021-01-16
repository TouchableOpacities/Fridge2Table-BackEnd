# Script to find "all" (most) ingredients returned by Recipe Puppy
from typing import List, Dict
import random
import json
from server.utility.scripts.recipe_class import Recipe
from server.utility.scripts.recipe_puppy import get_recipes

ESSENTIAL_INGREDIENTS = [
    "salt",
    "sugar",
    "butter",
    "water",
    "vegetable oil",
    "olive oil",
    "black pepper",
    "vanilla extract",
    "cinnamon",
    "powdered sugar",
    "paprika",
    "ice",
    "honey",
    "garlic salt",
    "balsamic vinegar",
    "red pepper",
    "kosher salt",
    "oregano",
    "cayenne",
    "baking soda",
    "chili powder"
    "white pepper"]


# Make empty query to RecipePuppy to get random recipes, then parse to list of Recipe objects
def get_recipe_objects(ingreds: List[str], num_pages: int):
    query_result = get_recipes(ingreds, "", num_pages)
    recipes = []
    for rec in query_result:
        recipes.append(Recipe(rec["href"], rec["ingredients"], rec["thumbnail"], rec["title"]))
    return recipes


# Build (or modify) dictionary of ingredients found in list of recipes w/ count of appearances as value
# Returns dictionary and the number of keys added (ingredients)
def build_ingred_dict(recipes: List[Recipe], curr_dict: Dict[str, int]):
    keys_added = 0

    for rec in recipes:
        for ingr in rec.ingred_list:
            if ingr in curr_dict:
                curr_dict[ingr] = curr_dict[ingr] + 1
            else:
                curr_dict[ingr] = 1
                # print("\t\t\tAdding " + ingr + "...")
                keys_added += 1

    return curr_dict, keys_added


def str_sorted_ingred_dict(ingred_dict: Dict[str, int]):
    result = ""
    sorted_ingreds = sorted(ingred_dict.items(), key=lambda item: -item[1])
    for (x, y) in sorted_ingreds:
        result += x + " (" + str(y) + ")\n"
    return result.strip()


def convert_to_frontend_format(ingreds_w_counts_filepath: str):
    f1 = open(ingreds_w_counts_filepath, "r")
    contents = f1.read()
    f1.close()

    items = []
    id_num = 1
    for line in contents.splitlines():
        name = line[:line.find("(") - 1]
        if name in ESSENTIAL_INGREDIENTS:
            continue
        items.append({"id": id_num,
                      "name": name,
                      "count": int(line[line.find("(") + 1:line.find(")")])})
        id_num += 1

    f2 = open("ingreds_for_frontend.txt", "w")
    f2.write(json.dumps(items))
    f2.close()


# ~~~~~~~~~~~~~~~~~~~~ MAIN ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Makes a series of blank queries to RecipePuppy and iteratively builds the ingredients dictionary.
# Stops when the ingrediens dictionary is relatively static.
def main():
    # # Make initial (blank) call
    # all_ingredients = {}
    # print("ROUND 1")
    # starting_num = len(all_ingredients.keys())
    # print("\tWe start with " + str(starting_num) + " ingredients...")
    # query_recipes = get_recipe_objects([], 5)
    # all_ingredients, num_added = build_ingred_dict(query_recipes, all_ingredients)
    # print("\tAdded " + str(num_added) + " ingredients this time...")
    #
    # # Make iterative calls based off a random ingredient (to get new results each time)
    # for i in range(249):
    #     print("ROUND " + str(i + 2))
    #     starting_num = len(all_ingredients.keys())
    #     print("\tWe start with " + str(starting_num) + " ingredients...")
    #     search_ingred = random.choice(list(all_ingredients.keys()))
    #     print("\t\tQuerying based off \"" + search_ingred + "\"...")
    #     query_recipes = get_recipe_objects([search_ingred], 5)
    #     all_ingredients, num_added = build_ingred_dict(query_recipes, all_ingredients)
    #     print("\tAdded " + str(num_added) + " ingredients this time...")
    #
    # # Print results and write to file
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nALL INGREDIENTS FOUND:")
    # result = str_sorted_ingred_dict(all_ingredients)
    # print(result)
    # f = open("ingreds_w_counts.txt", "w")
    # f.write(result)
    # f.close()

    convert_to_frontend_format("ingreds_w_counts.txt")


if __name__ == '__main__':
    main()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
