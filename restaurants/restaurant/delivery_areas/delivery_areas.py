from .delivery_area.delivery_area import DeliveryArea
class DeliveryAreas:
    def add(self, name):
        delivery_area = DeliveryArea(name)
        return delivery_area