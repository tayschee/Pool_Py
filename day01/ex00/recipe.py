import sys

class recipe :
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, recipe_type, description = ""):
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        if (isinstance(description, str)):
            self.recipe_type = recipe_type
        if not (isinstance(name, str)) :
            print("name must be str")
            sys.exit()
        if (isinstance(cooking_lvl, int) == False or cooking_lvl < 1 or cooking_lvl > 5) :
            print("cooking_lvl must be int beetwen 1 and 5")
            sys.exit()
        if (isinstance(cooking_time, int) == False or cooking_time < 0):
            print("cooking_time must be positive int")
            sys.exit()
        if not (isinstance(ingredients, list)):
            print("ingredients must be list")
            sys.exit()
        if (isinstance(recipe_type, str) == False or (recipe_type != "starter" or recipe_type != "lunch" or recipe_type("dessert"))):
            print("recipe_type must be str")
            sys.exit()


    def __str__(self):
        return("recipe :{}\ncooking_lvl:{}\ncooking_time:{}\ningredients : {}\ndescription: {}\nrecipe_type : {}".format(self.name, self.cooking_lvl, self.cooking_time, self.ingredients, self.description, self.recipe_type))


#grec = recipe("test", 5, 10, ["a"], "a", "bcde")
#print(grec)


