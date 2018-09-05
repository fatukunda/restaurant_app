import uuid
from restaurant.delivery_areas.delivery_areas import DeliveryAreas
class Restaurant:
    def __init__(self, name, location, id = uuid.uuid4(), menu = [],delivery_areas = [], is_open = False):
        self._id = id
        self._name = name
        self._location = location
        self._menu = menu
        self._is_open = is_open
        self._delivery_areas = delivery_areas
    """Get the id of a restaurant"""
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, value):
        self._id = value 
    """declare the name property"""
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = self
    
    @property
    def location(self):
        return self._location
    @location.setter
    def location(self, value):
        self._location = value
    @property
    def menu(self):
        return self._menu
    @menu.setter
    def menu(self, value):
        self._menu = value
    @property
    def is_open(self):
        return self._is_open
    @is_open.setter
    def is_open(self, value):
        self._is_open = value
    """Open the restaurant"""
    def open(self):
        self._is_open = True
    """Close the restaurant"""
    def close(self):
        self._is_open = False
    """List all the areas where the restaurant delivers food"""
    @property
    def delivery_areas(self):
        return self._delivery_areas
    def create_delivery_areas(self, name):
        delivery_areas =  DeliveryAreas()
        delivery_area = delivery_areas.add(name)
        self._delivery_areas.append(delivery_area)
