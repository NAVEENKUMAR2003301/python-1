from Inheritance import User,Student,Faculty,TempFaculty

student1 = Student()

student1.student_greet()


faculty1 = Faculty()

faculty1.faculty_greet()

student1.register()
faculty1.login()


user1 = User()
# user1.student_greet() - its not possible

#  child to parent data we can access
#  parent to child we cannot access

# multilevel inheritance

TempFac1 = TempFaculty()

TempFac1.tempFaculty_greet()
TempFac1. faculty_greet()
TempFac1.register()

