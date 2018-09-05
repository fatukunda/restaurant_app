from .foods.food.food_combinations.food_combinations import FoodCombinations
from .drinks.drinks import Drinks
class Menu:
    categories = ('break fast', 'lunch', 'dinner')
    def __init__(self, name, food_combinations = [], drinks = [], desserts = []):
        self._name = name
        self._food_combinations = food_combinations
        self._drinks = drinks
        self._desserts = desserts
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value
    @property
    def food_combinations(self):
        return self._food_combinations
    @property
    def drinks(self):
        return self._drinks
    @property
    def desserts(self):
        return self._desserts
    # Add food combination to the menu
    def add_food_combination(self, sauce, foods, price):
        food_combinations = FoodCombinations()
        food_combination = food_combinations.create_combination(sauce, foods, price)
        self._food_combinations.append(food_combination)
        return food_combination
    #Add drinks to your menu
    def add_drink(self, name):
        drinks = Drinks()
        drink = drinks.add_drink(name)
        self._drinks.append(drink)
        return drink




class BreakfastMenu(Menu):
    def __init__(self, name):
        super().__init__(self, name)

class LunchMenu(Menu):
    def __init__(self, name):
        super().__init__(self, name)

class DinnerMenu(Menu):
    def __init__(self, name):
        super().__init__(self, name)