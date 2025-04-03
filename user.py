from person import Person

class User(Person):
    def __init__(self, name, email, address, phone, shopping_history):
        super().__init__(name, email, address)
        self.phone = phone
        self.shopping_history = list(shopping_history) if shopping_history else []
    
    def get_phone(self):
        return self.phone
        
    def set_phone(self, phone):
        self.phone = phone
    
    def check_email(self):
        if "@" in self._email:
            return True
        else:
            print("Greska email ne sadrzi @!")
            return False
        
    def total_spent(self):
        return sum(product.get_price() for product in self.shopping_history)
        
    def add_product(self, product):
        self.shopping_history.append(product)
        
    def display_info(self):
        product_names = [product.name for product in self.shopping_history]
        print(f"Korisinik: {self.name} je kupio proizvode: {", ".join(product_names)} u totalnom iznosu od: {self.total_spent()}")
        
