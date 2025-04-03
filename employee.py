from person import Person

class Employee(Person):
    def __init__(self, name, email, address, salary):
        super().__init__(name, email, address)
        self.__salary = salary 
        
    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Plata mora biti pozitivna!")
        
    def get_salary(self):
        return self.__salary   
            
    def check_email(self):
        if "@" in self.get_email():
            return True
        else:
            print("Greska email ne sadrzi @!")
            return False
        
    def increase_salary(self, percentage):
        self.__salary = self.__salary * (1 + percentage/100)
        
    def display_info(self):
        print(f"Zaposleni: {self.name} \nEamil adresa: {self.get_email()} \nAdresa stanovanja: {self.get_address() }\nPlata na mesecnom nivou :{self.get_salary()} dinara")
    