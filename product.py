class Product:
    def __init__(self, name, price, quantity, description):
        self.name = name
        self.__price = float(price)
        self.quantity = int(quantity)
        self._description = description
        
    def get_price(self):
        return self.__price
    
    def set_price(self, price):
        if price > 0:
            self.__price = price
        else:
            print("Cena mora biti pozitivna!")
            
    def get_description(self):
        return self._description
    
    def set_description(self, description):
        self._description = description
    
    def check_quantity(self):
        if self._quantity <10:
            print("Mala kolicina prozicvoda!")
            return False
        else:
            return True
            
