import uuid
class FoodCombination:
    def __init__(self, sauce, price = 0, foods = [], id = uuid.uuid4() ):
        self._sauce = sauce
        self._foods = foods
        self._id = id
        self._price = price
    @property    
    def id(self):
        return self._id
    @id.setter
    def id(self, value):
        self._id = value
    @property
    def sauce(self):
        return self._sauce
    @property
    def foods(self):
        return self._foods
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        self._price = value

        
