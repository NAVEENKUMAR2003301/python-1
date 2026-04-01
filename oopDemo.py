#Combined Real-Time
 
class User:
    users_count = 0   # class variable
 
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd
        User.users_count += 1
 
    def get_name(self):
        return self.name
 
    def register(self):
        print(f"{self.name} registered")
        return self
 
    def login(self):
        print(f"{self.name} logged in")
        return self
 
    def greet(self):
        print("Welcome User")
        return self
 
 
class Student(User):
    def __init__(self, name, pwd):
        super().__init__(name, pwd)
 
    def greet(self):   # overriding
        print("Welcome Student")
        return self
 
 
class Faculty(User):
    def _init_(self, name, pwd):
        super()._init_(name, pwd)
    def greet(self):   # overriding
        print("Welcome Faculty")
        return self
 
