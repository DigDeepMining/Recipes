import functions

# This App will create some Random Recipes

# This section contains the Variables and Startup Options
veg = functions.veg()
spices = functions.spices()
carbs = functions.carbs()
protein = functions.protein()
sauces = functions.sauces()

vegArray = []
spicesArray = []
carbsArray = []
proteinArray = []
saucesArray = []

vegQty = 0
spicesQty = 0
carbsQty = 0
proteinQty = 0
saucesQty = 0

print("Please choose how many of the Veg ingredients below you want...")
for key,value in veg.items():
    print(f"Ingredient: {value}")
    #print(len(veg))
vegQtyCheck = False
vegQty = int(input())
while vegQtyCheck == False:
    if vegQty > len(veg):
        print(f"You have chosen a higher Qty than we have in stock.\nPlease choose less than {len(veg)}")
        vegQty = int(input())
    else:
        vegQtyCheck = True
        break

print("Please choose how many of the Spices ingredients below you want...")
for key,value in spices.items():
    print(f"Ingredient: {value}")
spicesQty = int(input())

print("Please choose how many of the Carbs ingredients below you want...")
for key,value in carbs.items():
    print(f"Ingredient: {value}")
carbsQty = int(input())

print("Please choose how many of the Protein ingredients below you want...")
for key,value in protein.items():
    print(f"Ingredient: {value}")
proteinQty = int(input())

print("Please choose how many of the Sauces ingredients below you want...")
for key,value in sauces.items():
    print(f"Ingredient: {value}")
saucesQty = int(input())
# End

# Game Logic
count = 0
while count < vegQty:
    ingredient = functions.randomIngredients()
    ingredientText = veg[ingredient]
    if ingredientText not in vegArray:
        vegArray.append(ingredientText)
        count = count+1
    #print(vegArray)

count = 0
while count < spicesQty:
    ingredient = functions.randomIngredients()
    ingredientText = spices[ingredient]
    if ingredientText not in spicesArray:
        spicesArray.append(ingredientText)
        count = count+1
    #print(spicesArray)

count = 0
while count < carbsQty:
    ingredient = functions.randomIngredients()
    ingredientText = carbs[ingredient]
    if ingredientText not in carbsArray:
        carbsArray.append(ingredientText)
        count = count+1
    #print(carbsArray)

count = 0
while count < proteinQty:
    ingredient = functions.randomIngredients()
    ingredientText = protein[ingredient]
    if ingredientText not in proteinArray:
        proteinArray.append(ingredientText)
        count = count+1
    #print(proteinArray)

count = 0
while count < saucesQty:
    ingredient = functions.randomIngredients()
    ingredientText = sauces[ingredient]
    if ingredientText not in saucesArray:
        saucesArray.append(ingredientText)
        count = count+1
    #print(saucesArray)

recipeText = open("recipe.txt", "a")
recipeText.write("Below are the Ingredients you have chosen for the Random Recipe\n")
recipeText.write("---------------------------------------------------------------\n")
print("Below are the Ingredients for the Random Recipe")
print("---------------------------------------------------------------")
recipeText.write("Veg:\n")
print("Veg:")
for item in vegArray:
    recipeText.write(f"{item}\n")
    print(item)
recipeText.write("---------------------------------------------------------------\n")
recipeText.write("Spices:\n")
print("---------------------------------------------------------------")
print("Spices:")
for item in spicesArray:
    recipeText.write(f"{item}\n")
    print(item)
recipeText.write("---------------------------------------------------------------\n")
recipeText.write("Carbs:\n")
print("---------------------------------------------------------------")
print("Carbs:")
for item in carbsArray:
    recipeText.write(f"{item}\n")
    print(item)
recipeText.write("---------------------------------------------------------------\n")
recipeText.write("Protien:\n")
print("---------------------------------------------------------------")
print("Protein:")
for item in proteinArray:
    recipeText.write(f"{item}\n")
    print(item)
recipeText.write("---------------------------------------------------------------\n")
recipeText.write("Sauces:\n")
print("---------------------------------------------------------------")
print("Sauces:")
for item in saucesArray:
    recipeText.write(f"{item}\n")
    print(item)

recipeText.close()
# End