import datetime
import recipe

class   book:
    def __init__(self, name):
        self.name = name
        self.lastUp = datetime.datetime.now()
        self.creation = datetime.datetime.now()
        self.reciplist = {"starter" : [myrecipe] , "lunch" : [], "dessert" : []}
    def get_recip_by_name(self, name):
        for i in self.reciplist:
            print (i)
            for rec in self.reciplist[i] :
                if (rec == name) :
                    print(name)
                    return(name)
        else :
            print("this recip doesn't exist")
            return(False)

    def get_recip_by_types(self, recipe_type):
        for i in self.reciplist:
            if (i == recipe_type):
                for j in self.reciplist[i] :
                    print(j.name)

    def add_recipe(self, recipe):
        try :
            self.reciplist[recipe.recipe_type].append(recipe)
        except AttributeError:
           print("This is not a recipe")

