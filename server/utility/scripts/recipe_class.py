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

    # Method to update thumbnail to default set of icons.
    def replace_thumbnail(self):
        ICONS_DICT = {"salad": "https://img.icons8.com/plasticine/100/000000/salad.png",
                      "chicken": "https://img.icons8.com/cotton/64/000000/thanksgiving-turkey.png",
                      "soup": "https://img.icons8.com/doodle/100/000000/soup-plate.png",
                      "pasta": "https://img.icons8.com/officel/16/000000/spaghetti.png"}
        DEFAULT_ICON = "https://www.diginico.com/wp-content/uploads/2020/01/fridge.jpg"

        matched = False
        for keyword in ICONS_DICT.keys():
            if self.title.lower().find(keyword) != -1:
                self.thumbnail = ICONS_DICT[keyword]
                matched = True
                break

        if not matched:
            self.thumbnail = DEFAULT_ICON

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
