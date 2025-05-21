import random

lurido_ingredients = {"affettati": ["prosciutto crudo", "prosciutto cotto", "salame piccante", 
                                    "porchetta", "salame dolce", "bresaola", "mortadella", "meat is murder fuck you"], 
                      "formaggi": ["stracchino", "mozzarella", "fontina"], 
                      "verdure unte": ["zucchine", "carciofi", "peperoni", "enough oily stuff for you fatso"], 
                      "verdure liscie": ["insalata", "pomodoro", "olive"]}

class FoodDecision():
    def __init__(self, ingredients, veggie=False):
        self.possibilities = ingredients
        self.veg_check = veggie
    
    def getIngredients(self):
        return self.possibilities
    
    def getFoodType(self):
        return self.veg_check
    
    def buildPaninoLurido(self, very_oily=False):
        veggie_check = self.getFoodType()
        ingredients = self.getIngredients()
        oily_num = 0
        if veggie_check:
            meat = "no meat"
            oily_num += 1
        else:
            meat = ", ".join(random.sample(ingredients["affettati"], k=1))

        if very_oily:
            oily_num += 1
        dairy = ", ".join(random.sample(ingredients["formaggi"], k=1))
        side = ", ".join(random.sample(ingredients["verdure liscie"], k=2))
        oily_stuff = ", ".join(random.sample(ingredients["verdure unte"], k=oily_num)) if oily_num > 0 else "no greasy veggies"
        PaninoLurido(meat, dairy, side, oily_stuff)


class PaninoLurido(FoodDecision):
    def __init__(self, *args):
        self.chosen_ingredients = ", ".join(args) 
        print(f"Your Panino Lurido has these ingredients: {self.chosen_ingredients}")



decision_meat = FoodDecision(lurido_ingredients)
decision_veg = FoodDecision(lurido_ingredients, veggie=True)
decision_meat.buildPaninoLurido()
decision_veg.buildPaninoLurido(very_oily=True)