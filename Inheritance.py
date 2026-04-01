class User :                              

    username = None
    pwd      = None

    def __init__(self,username,pwd):

       self.username = username
       self.pwd      = pwd
# parent class

    def register(self) :
        print("register...")

    def login(self) :
        print("login")


class Student(User) :

    def __init__(self, username, pwd,course,fee):
      super().__init__()
      self.course = course       
      self.fee = fee       
# child class 
    def student_greet(self) :
      print("hi student" +" "+ self.course)


class Faculty(User) :
# child class
    def faculty_greet(self) :
       print("hi Teacher")


class TempFaculty(Faculty) :

# grand Child class
   def tempFaculty_greet(self) :
       print("hello")


