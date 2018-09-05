from .sauce.sauce import Sauce

class Sauces:
    def __init__(self, sauces = []):
        self._sauces = sauces
    @property
    def sauces(self):
        return self._sauces
    def create_sauce(self, name):
        sauce = Sauce(name)
        self._sauces.append(sauce)
        return sauce