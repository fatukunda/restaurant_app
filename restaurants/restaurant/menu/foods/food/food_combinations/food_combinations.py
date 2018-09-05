from .food_combination.food_combination import FoodCombination
class FoodCombinations:
    def __init__(self, combinations = []):
        self._combinations = combinations
    def create_combination(self, sauce, foods, price):
        combination = FoodCombination(sauce, price, foods)
        new_combination = {
                          "id": combination.id,
                           combination.sauce.name: combination.foods,
                           "price": combination.price 
                            }
        self._combinations.append(new_combination)
        return new_combination
    
    def search(self, id):
        for combination in self._combinations:
            if combination['id'] == id:
                return combination

    def remove(self, id):
        for combination in self._combinations:
            if combination['id'] == id:
                self._combinations.remove(combination)