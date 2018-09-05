from .drink.drink import Drink
class Drinks:
    def __init__(self, drinks = []):
        self._drinks = drinks
    @property
    def drinks(self):
        return self._drinks
    def add_drink(self, name):
        drink = Drink(name)
        self._drinks.append(drink)
        return drink
    def search_drink(self, id):
        for drink in self._drinks:
            if drink.id == id:
                return drink
    def remove_drink(self, id):
        drink = self.search_drink(id)
        if drink:
            self._drinks.remove(drink)

