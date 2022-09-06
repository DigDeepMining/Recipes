import random

def randomIngredients():
    ingredient = random.randint(1,7)
    return ingredient

def veg():
    vegDictionary = {
        1:"Cauliflower",
        2:"Aubergine",
        3:"Broccoli",
        4:"Sweet Potato",
        5:"Peas",
        6:"Carrots",
        7:"Sweetcorn"
    }
    return vegDictionary

def spices():
    spicesDictionary = {
        1:"Tumeric",
        2:"Black Pepper",
        3:"Cinnamon",
        4:"Cumin",
        5:"Ginger",
        6:"Coriander",
        7:"Paprika"
    }
    return spicesDictionary

def carbs():
    carbsDictionary = {
        1:"Rice",
        2:"Bread",
        3:"Potatoes",
        4:"Pasta",
        5:"Wheat",
        6:"Noodles",
        7:"Oats"
    }
    return carbsDictionary

def protein():
    proteinDictionary = {
        1:"Beef",
        2:"Chicken",
        3:"Eggs",
        4:"Lamb",
        5:"Duck",
        6:"Quorn",
        7:"Turkey"
    }
    return proteinDictionary

def sauces():
    sauceDictionary = {
        1:"Ketchup",
        2:"Mustard",
        3:"Mayo",
        4:"Sweetchilli",
        5:"Cheese Sauce",
        6:"BBQ",
        7:"Hoisin"
    }
    return sauceDictionary