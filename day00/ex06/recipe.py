
rec = ["sandwich", "cake", "salad"]

cookbook =  {rec[0] : {'ingredients' : ["ham", "bread", "cheese"], 'meal' : 'lunch', 'prep_time' : 10},
            rec[1] : {'ingredients' : ["floor", "sugar", "eggs",], 'meal' : 'dessert', 'prep_time' : 60},
            rec[2] : {'ingredients' : ["avocado", "arugula", "tomatoes", "spinach",], 'meal' : 'lunch', 'prep_time' : 15} 
            }

def add():

        
    print("add")
def dlt(rec):

    print("delete")
def p_rec(recipe):
    print("\nRecipe for", recipe, ":\nIngredients list:", cookbook[recipe]['ingredients'], "\nTo be eaten for", cookbook[recipe]['meal'], "\nTakes", cookbook[recipe]['prep_time'], " minutes of cooking.")
def p_all():
    print("ok")
    for i in rec :
        p_rec(i)

mode = '0';
print("Please select an option by typing the corresponding number:\n1: Add a recipe\n2: Delete a recipe\n3: Print a recipe\n4: Print the cookbook\n5: Quit")
while (mode != '5'):
    mode = input()
    if (mode == '1'):
        add()
    elif (mode == '2'):
        dlt()
    elif (mode == '3'):
        mode = input("Please enter the recipe's name to get its details:\n")
        p_rec(mode)
    elif (mode == '4'):
        p_all()
    elif (mode == '5'):
        print("Cookbook closed.")
    else :
       print("This option does not exist, please type the corresponding number.\nTo exit, enter 5.")



