from restaurant.restaurant import Restaurant
class Restaurants:
    def __init__(self, restaurants = []):
        self._restaurants = restaurants
    def __call__(self):
        pass
    """Get a list of all restaurants"""
    @property
    def restaurants(self):
        return self._restaurants
    """Add a new restaurant"""
    def add_restaurant(self, name, location):
        restaurant = Restaurant(name, location)
        self._restaurants.append(restaurant)
        return restaurant
    """ Search for a specific restaurant"""
    def search(self, id):
        for restaurant in self._restaurants:
            if restaurant._id == id:
                return restaurant
    """Edit a specific restaurant. This can be done by the owner or the app admin"""
    def edit_restaurant(self, restaurant):
        pass
    """Remove a specific restaurant. This can be done by the owner or the app admin"""
    def remove_restaurant(self, id):
        restaurant = self.search(id)
        if restaurant:
           del restaurant
        else:
            return 'Restaurant not found'

new_restaurants = Restaurants()
restaurant = new_restaurants.add_restaurant('Maama Willy', 'Makerere Kikoni')
print(restaurant.id)
print(restaurant.name)
print(restaurant.location)
print(restaurant.is_open)
restaurant.create_delivery_areas('kikoni')
restaurant.create_delivery_areas('kawempe')
for deliveryArea in restaurant.delivery_areas:
    print(deliveryArea.name)
# restaurant.create_delivery_areas('Kawempe')

print(restaurant)