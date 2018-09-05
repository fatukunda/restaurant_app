from .food.food import Food
class Foods:
    def __init__(self, foods = []):
        self._foods = foods
    def add(self, name):
        food = Food(name)
        self._foods.append(food)
        return food
    def search(self, id):
        for food in self._foods:
            if food.id == id:
                return food
    def remove(self, id):
        food = self.search(id)
        if food:
            self._foods.remove(food)
    def edit(self, id):
        pass
    
# newfoods = Foods()
# food = newfoods.add('matooke')
# food1 = newfoods.add('rice')

# print(newfoods.search(food.id).name)
# newfoods.remove(food.id)
# for f in newfoods._foods:
#     print(f)



        