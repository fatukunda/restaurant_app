import uuid
class Food:
    def __init__(self, name,  id = uuid.uuid4()):
        self._name = name
        self._id = id
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, value):
        self._id = value