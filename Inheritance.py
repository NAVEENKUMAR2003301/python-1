class User :                              

# parent class

    def register(self) :
        print("register...")

    def login(self) :
        print("login")


class Student(User) :
# child class 
    def student_greet(self) :
      print("hi student")


class Faculty(User) :
# child class
    def faculty_greet(self) :
       print("hi Teacher")


class TempFaculty(Faculty) :

# grand Child class
   def tempFaculty_greet(self) :
       print("hello")


