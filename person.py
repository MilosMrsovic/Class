import abc

class Person(abc.ABC):
    def __init__(self, name, email, address):
        self.name = name
        self._email = email
        self._address = address
        
    def get_email(self):
        return self._email
    
    def set_email(self, email):
        if "@" in email:
            self._email = email
        else:
            print("Novi email mora sadrzati :'@'")
        
    def get_address(self):
        return self._address
    
    def set_address(self, address):
        self._address = address
        
    
    def check_email(self):
        if "@" in self._email:
            return True
        else:
            print("Greska email ne sadrzi @!")
            return False
        
    @abc.abstractmethod
    def display_info(self):
        pass
    
        