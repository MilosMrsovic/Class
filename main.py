from product import Product
from employee import Employee
from user import User

products = [
    Product("Mouse", 1299.99, 22, "Mouse for PC"),
    Product("Keyboard", 2499.99, 12, "Keyboard for PC"),
    Product("Monitor", 23000, 18, "Monitor for PC"),
    Product("Phone", 99000, 42, "Mobile device"),
    Product("Computer", 129000, 7, "Computer with high performance")
]

employees = [
    Employee("Marko", "masa1212@gmail.com","Pedje Jovanovica 17", 89000),
    Employee("Petar", "pera2323@gmail.com","Juzni Bulevar 23", 125000)
]

users = [
    User("Milan", "Micko2222@gmail.com", "Milana zoporubca 23", "381615478931", None),
    User("Jovan", "Joca221@gmail.com","Marka Zrenajnian 12", "381625578531", None),
    User("Mladen", "mladja@gmail.com","Petra Petrovic 222", "381655547891",  None)
]


users[0].add_product(products[0])  
users[0].add_product(products[1]) 
 
users[1].add_product(products[2])  
users[1].add_product(products[3])  

users[2].add_product(products[4])  
users[2].add_product(products[0]) 

for user in users:
    print(f"Korsinik {user.name} je potrosio: {user.total_spent():.2f} dinara u kupovini")
    
print()

for user in users:
    user.display_info()

print()

for employee in employees:
    employee.display_info()
    
print()

print("Promena cene za proizvod: ")
products[2].set_price(2225)
print(f"Nova promenjena cena za {products[2].name} iznosi {products[2].get_price()}")

print("Promena plate za zaposlenog: ")
employees[1].set_salary(138250)
print(f"Korisinik {employees[1].name} sada ima mesecnu platu od {employees[1].get_salary()}")