# A class representing a recipe object.
class Recipe:

    # Constructor method with instance variables set.
    def __init__(self, href: str, ingredients: str, thumbnail: str, title: str):
        self.href = href
        self.ingred_list = ingredients.split(", ")
        self.thumbnail = thumbnail
        self.title = title

    # str() method to give string representation
    def __str__(self):
        result = "RECIPE: " + self.title
        result += "\n\tIngredients:\n"
        for i in range(len(self.ingred_list)):
            result += "\t\t" + self.ingred_list[i] + "\n"
        result += "\tLink: " + self.href + "\n"
        result += "\tImage: " + self.thumbnail
        return result

    # Method to "dict-ify" Recipe for JSON
    def dictify(self):
        recipe_dict = {"href": self.href,
                       "ingredients": ", ".join(self.ingred_list),
                       "thumbnail": self.thumbnail,
                       "title": self.title}
        return recipe_dict


# ~~~~~~~~~~~~~~~~~~~~ FOR TESTING ONLY ~~~~~~~~~~~~~~~~~~~~
def main():
    test = {"href": "http://allrecipes.com/Recipe/Ds-Famous-Salsa/Detail.aspx",
            "ingredients": "green chilies, garlic, lime, onions, salt",
            "thumbnail": "http://img.recipepuppy.com/29584.jpg",
            "title": "D's Famous Salsa"}

    test_recipe = Recipe(test["href"], test["ingredients"], test["thumbnail"], test["title"])
    print(test_recipe)
    test_dictified = test_recipe.dictify()
    print(test_dictified)


if __name__ == '__main__':
    main()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
