import uuid
class Drink:
    def __init__(self, name, id = uuid.uuid4()):
        self._id = id
        self._name = name
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, value):
        self._id = value
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value