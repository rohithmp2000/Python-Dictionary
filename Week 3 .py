pantry = {
   "chicken": 500,
   "lemon": 2,
   "cumin": 24,
   "paprika": 18,
   "chilli powder": 7,
   "yogurt": 300,
   "oil": 450,
   "onion": 5,
   "garlic": 9,
   "ginger": 2,
   "tomato puree": 125,
   "almonds": 75,
   "rice": 500,
   "coriander": 20,
   "lime": 3,
   "pepper": 8,
   "egg": 6,
   "pizza": 2,
   "spam": 1,
 }

recipes = {
"Butter chicken":
       [
        "chicken",
        "lemon",
        "cumin",
        "paprika",
        "chilli powder",
        "yogurt",
        "oil",
        "onion",
        "garlic",
        "ginger",
        "tomato puree",
        "almonds",
        "rice",
        "coriander",
        "lime",
        ],
"Chicken and chips": 
        [
       "chicken",
       "potatoes",
       "salt",
       "malt vinegar",
        ],
"Pizza": 
        [
        "pizza",
        ],
"Egg sandwich": 
        [
        "egg",
        "bread",
        "butter",
        ],
"Beans on toast": 
        [
        "beans",
        "bread",
        ],
"Spam a la tin": 
        [
        "spam",
        "tin opener",
        "spoon",
        ],
}

def show_pantry(pantry_list):
    for i in pantry_list:
        print(f"{i} : {pantry[i]}")

def choose_recipe(recipe):
    for i in recipe:
        print(i)
    return input("Please enter the recipe you want to make = ")

def show_recipeitems(selected_recipe,recipes):
    for k, v in recipes:
        if k == selected_recipe:
            print(v)

def cook_recipe(recipeitem,recipelist,pantry):
    cookable = True
    if recipeitem in recipelist:
        for i in recipelist[recipeitem]:
            if i in pantry:
                pass
            else:
                cookable = False
        if cookable == True:
            for i in recipelist[selected_recipe]:
                pantry[i] = pantry[i] - 1
        else:
            print("No items to cook the food")
    else:
        print("No such recipe")


a = int(input("1 = Cook the recipe \n2 = List pantry items \nEnter the number for the process = \n"))
if a == 1:
    show_pantry(pantry)
    print("\n")
    selected_recipe = choose_recipe(recipes)
    print("\n")
    print(selected_recipe,"=",recipes[selected_recipe])
    print("\n")
    cook_recipe(selected_recipe,recipes,pantry)
    print("\n")
    show_pantry(pantry)
elif a == 2:
    show_pantry(pantry)
else:
    print("Invalid Input")