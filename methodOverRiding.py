# Usage

from oopDemo import User, Student , Faculty

s = Student("john", "123")
f = Faculty("admin", "999")
 
s.login().greet().register()
print() 
f.login().greet().register()
print()
 
print("Total Users:", User.users_count)