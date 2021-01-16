# Script to find "all" (most) ingredients returned by Recipe Puppy
from server.utility.scripts.recipe_class import Recipe
from server.utility.scripts.recipe_puppy import get_recipes


# Make empty query to RecipePuppy to get random recipes, then parse to list of Recipe objects
def make_blank_query(num_pages: int):
    query_result = get_recipes("", "", num_pages)
    recipes = []
    for rec in query_result:
        recipes.append(Recipe(rec["href"], rec["ingredients"], rec["thumbnail"], rec["title"]))
    return recipes


# Build (or modify) dictionary of ingredients found in list of recipes w/ count of appearances as value
def build_ingred_dict(recipes: list[Recipe], ingred_dict: dict[str, int]):
    for rec in recipes:
        for ingr in rec.ingred_list:
            if ingr in ingred_dict:
                ingred_dict[ingr] = ingred_dict[ingr] + 1
            else:
                ingred_dict[ingr] = 1

    return ingred_dict


# ~~~~~~~~~~~~~~~~~~~~ FOR TESTING ONLY ~~~~~~~~~~~~~~~~~~~~
def main():
    all_ingredients = {}

    print(len(all_ingredients.keys()))


if __name__ == '__main__':
    main()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
