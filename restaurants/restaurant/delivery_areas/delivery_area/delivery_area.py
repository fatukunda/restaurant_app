class DeliveryArea:
    def __init__(self, name, delivery_time = 10):
        self._name = name
        self._delivery_time = delivery_time
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value
    @property
    def delivery_time(self):
        return self._delivery_time
    @delivery_time.setter
    def delivery_time(self, value):
        self._delivery_time = value
