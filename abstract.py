# class User:

#     username = None
#     pwd      = None


#     def __init__(self,username,pwd,courseName,courseFee):
#         self.username  = username
#         self.pwd       = pwd
#         self.courseName = courseName
#         self.courseFee  = courseFee

#     def register(self) :
#         print("register " + self.username)

#     def login(self) :
#         print("login")


# class Student(User) :

#     def __init__(self, username, pwd, courseName , courseFee):
#         super().__init__(username,pwd,courseName,courseFee)
#         super().register()
        

        
#     def student_greet(self):
#         print("hi student " + self.username )
       

# class Faculty(User) :
#     def fuculty_greet(self):
#         print("hi faculty")




# abstract
from abc import ABC,abstractmethod

class Vechile(ABC) : 
    @abstractmethod
    def start(self):
        print("hello")

 
        

    def stop(self) :
        pass


class Bike(Vechile) :
    def start(self) :
        print("your riding bike")

    def __init__(self,brand,price):
        self.username = brand
        self.pwd      = price

    def stop(self):
        print("stop the bike " + self.username)

    def hello1(self):
        print("welcome to all " + self.username)

class Car(Bike)  :

    def __init__(self,brand,price) :
        super().__init__(brand,price)
        super().hello1
    def start(self) :
        print("your riding car" )

    def stop(self):
        print("stop the car")

class Aero(Vechile) :
    def start(self):
        print("fling now")