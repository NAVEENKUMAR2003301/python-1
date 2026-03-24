# print("hello world", end=" ")
# print("welcome python")
# print("laptop","mouse","keyboard",sep="\'")


# # escape sequence

# # \n
# # \t


# # jgjgvghfghfhg - single line comment

# '''
# print("hello")
# print("welcome")
# print("hi")

# multiline command
# '''

# # data Types

# '''
# simple dataType

# 1. integer  - 100

# 2. string   - "whatever"

# 3. float    - 50.2

# 4. boolean  - True , False

# '''

# '''
# complex DataType

# 1. list

# 2. Dictionary

# 3. Tuple

# 4. set

# '''

# # variables 

# name = "navi"
# age = 15

# print(name,age , sep=",")

# # assignment 

# # single assignment

# n = 5

# print("sigle assignment :- ", n)

# # multi assignment

# name1,age1,launguage = "navi",15,True

# print("multi assignment :- ", name1, age1,launguage)



# # Indexing

# name2 = "john"

# print(name2[0])

# # immutability

# # name2[0] = "R"

# # print(name2)



# # operators


# '''
# 1 . arithmetic operator
# 2 . assignment operator
# 3 . comparision operator
# 4 . logical operator
# 5 . bitwise operator
# 6 . membership operator
# '''

# # 1. arithmetic operator 

# # addition      +

# print(1 + 3)

# # subraction    -

# print(2 - 1)

# # multiplication *

# print(3*3)

# # division   /

# print(5 / 5)

# # modulus    %

# print(9%10)

# # Exponencial **

# print(4**2) # 4^2 = 4*4 = 16


# # floar division // 

# print(10 // 2)

# '''
# Bodmas 

# b - bracket
# o - order
# d - diviaion
# m - multiplication
# a - addition
# s - subraction
# '''



# print(2**3**(2%10)) #        2**3**2 = 2^9

# print(2**9)



# # Assignment operator

# num1 = 10
# additionVal = 100

# num1 /=  additionVal

# print(num1)


# # comparision & Relational operator

# '''
# lessThen     <       (5<5)     False

# greaterThen  >       (5>5)     False

# lessThenEq   <=      (5<=5)    True

# GreaterThenEq >=     (10>=2)   True

#    ==     (10=="10") False

#    !=     (10 != "10") True



# '''
# print(10>10)
# print(10>.5)
# print(10=="10")

# print("10")
# print(10)


# a = "siva"
# b = "Siva"

# print("s :-", ord("s"))
# print("S :-", ord("S"))

# print(a==b)



# a = 5
# b = 7

# print(a,b)

# # temp = a

# # a = b 

# # b = temp

# # print(a,b)

# a,b = b,a

# print(a,b)



# # membership operator [in] , [not in]

# group = [1,2,3,4,5]

# print(50 not in group)


# # logical operator

# '''
# AND   -- > and
# OR    -- > or
# NOT   -- > not

# '''


# # AND 

# # True and True and True = True 
# # True and False and True = False


# # OR

# # True or False or False = True
# # False or False or False = False

# # NOT

# # not(True) = False
# # not(False) = True 


# print(5>5 and 5==5 and 1>=.1000) # False
# print(5==5 or 5>=3 and 2==2) # True
# print(not(6>=2) and 8>3) #False


# # Bitwise operator 

# '''
# AND  - &
# OR   - |
# NOT  - ~
# XOR  - ^
# leftShift - <<
# RightShift - >>
# '''

# '''
# XOR - ^


# T   T    - F
# T   F    - T
# F   T    - T
# F   F    - F
# '''


# a = 5

# b = 7


# print(a & b)
# print(a | b)
# print(~b)
# print(a ^ b)


# print(12 << 1) 
# print(12 >> 1)



# # String - "Adsf"

# # string Replication 


# a = "hello"

# print(a * 5)

# # string concatination  +

# str1 = "iron"
# str2 = "man"
# str3 = " "

# print(str1 +str3 + str2)


# # user Input Console    (input())

# # name = input("enter your name : - ")

# # print("userName :- ",type(name))


# # age = input("enter your age :- ")
# # print("userAge :- ",type(age))


# # TypeCasting 


# # num2 = int(input("enter your mark Maths :- "))
# # num3 = int(input("enter your mark Science :- "))

# # print((num2+num2)/2)


# # a = int(input("enter first value :- ")) #3
# # b = int(input("second first value :- ")) #2

# # print(3*a*2+b - 2) #error #18


# #unit digit


# # num = input() #10000 , 0 - 1, 1 - 0 , 2 - 0 , 3 - 0 ,4 - 0
# # print(num[len(num)-1]) # num[len(num)-2]

# # print(1234//10) --> 123


# # num1 = int(input())

# # num1 //= 10 #num1 = num1 // 10 = 1234 // 10 -- > 123

# # print(num1 % 10) #123 % 10 --> 3


# # flow control Statement

# # # 1. conditional statement

# # # 1. if statement

# # # if condition = true --> next line , false --> if inside not allow

# # # example 

# # if (5>=5) :
# #     print("now i think condition true")


# # # 2.if else statement

# # # if (5>5) :
# # #     print("condition true")
# # # else :
# # #     print("condition false")


# # # # 3. Elif Statement

# # # time = int(input("enter the time Now :- 24hrs"))

# # # if (time >= 1 and time <= 6) : 
# # #     print("good morning")
# # # elif (time >= 7 and time <=12) :
# # #     print("morning")
# # # elif (time >= 13 and time <= 17) : 
# # #     print("Good Afternoon")
# # # elif (time >= 18 and time <= 20) :
# # #     print("Good Evening")
# # # else :
# # #     print("Good night")


# # # #4. Nested If Statement 


# # # # uniform entrance selection application
# # # name = input("enter your name")
# # # age = int(input("enter your age"))
# # # height = int(input("enter you height using cm"))
# # # weight = int(input("enter your weight using kg"))

# # # if (age >= 18) :
# # #     if (height >= 160) : 
# # #         if (weight >= 60) :
# # #             print(name ," congradulation your selected 😊😊😊")
# # #         else : 
# # #             print(name, " your weight is not eligible")

# # #     else : 
# # #         print(name, "  your height is not eligible")
# # # else : 
# # #     print(name, " your age is not eligible")


# # # 5. match statement


# # # match variable :
# # # #     case value : statement


# # # # example 


# # # day = int(input("enter the today number :- "))


# # # match day :
# # #     case 1 :
# # #         print("sunday")
# # #     case 2 :
# # #         print("monday")
# # #     case 3 :
# # #         print("tuesday")
# # #     case 4 :
# # #         print("wednesday")
# # #     case 5 :
# # #         print("thursay")
# # #     case 6 :
# # #         print("friday")
# # #     case 7 :
# # #         print("saturday")
    


# # # looping Statement 
# # print("normal statement")
# # print(1)
# # print(2)
# # print(3)
# # print(4)
# # print(5)


# # print("looping statement")
# # # for loop

# # # for i in range(1,6) :
# # #     print(i)


# # # list1 = [1,3,5,7,9]

# # # for i in list1 :
# # #     print(i)


# # # nested loop statement

# # # for i in range(1,4) : 
    
# # #     for j in range(1,6) :
        
# # #         print(i ,j , end=" ")


# # # i j = 1 1 , 1 2 , 1 3 , 1 4  , 15 , 2 1 , 2 2, 2 3 , 2 4 , 2 5 , 3 1 , 3 2 , 3 3 , 3 4 , 3 5 




# # # while loop 

# # # num = 1     intialiazation

# # # while num<=100 : while condition
    
# #    #  print(num)  statement

# #    #  num = num + 1 iteration



# # # letter = "" 

# # # while not letter.isalpha() :
    
# # #     letter = input("enter an alphabet")

# # # print("you have eneter " + letter)



# # # break 
# # #  1,6
# # # lst = [] 

# # # while True :
# # #    input1 = input("enter value :- ")

# # #    if input1 == "z" :

# # #       break

# # #    lst.append(int(input1))


# # # print(lst)



# # Continue


# # str = "A,B,C,D,E,F"

# # str1 = ""

# # for i in str:
    
# #    if i == "," : 
# #       continue
   
# #    str1 = str1 + i 

# # print(str1)




# #  String function - [start : stop : step]

# name = "firstBatch"

# print(name)
# print(name[0])

# print(name[0:5])
# print(name[ : 5])
# print(name[5 : 8])

# print(name[0 : ])

# print(name[0 : 7 : 3])

# print(name[-5 : : 2])

# print(name[ : : -1])


# #  slice - sI, eI+1

# name = "helloworld"

# x = slice(2,5)

# print(name[x])



# # list - we can store multiple value - [start : stop : step]


# cities = ["trichy","chennai","bangalore","salem"]

# print(cities)
# print(cities[0])
# print(cities[-1])

# print(cities[0 : 3])
# print(cities[0 : 3 : 2])
# print(cities[ : : -1])
# print(cities[0 : 4 : 3])


# # mutable 

# cities[3] = "karur"

# print(cities)


# # add value - (append())

# cities.append("salem")
# cities.append("coiambatore")

# print(cities)

# #insert(index , value) - spec place

# cities.insert(2, "thanjavur")

# print(cities)



# # delete - del

# del cities[3]

# print(cities)


# # pop() - delete last of list value

# re1 = cities.pop()

# print(re1)


# returnVal = cities.pop(1)

# print(returnVal)
# print(cities)


# #remove("value")

# cities.remove("salem")

# print(cities)

# #clear()

# cities.clear()

# print(cities)


# cities.append("chennai")
# cities.append("madurai")
# cities.append("coiambatore")

# print(cities)


# # sort 

# cities.sort()

# print(cities)

# # reverse 

# cities.reverse()

# print(cities)

# # length

# print(len(cities))


# Tuples - () - immutable


tup1 = (1,2,3)

print(type(tup1))

# tup1[1] = 5

print(tup1[2])


tup = (1,2,2,2,3,5,7)

print(tup.count(2))


for i in tup :
    print(i)


if 1 in tup:
    print("yes")
else:
    print("no")









# Dictionary 

user = {"name" : "john","age" : 23 , "role" : "developer"}

print(user)
print(user["role"])


# add value

user["city"] = "chennai"

print(user)

#modify

user["age"] = 26

print(user)

#delete

del user["role"]

print(user)


# dictionary in loop 

user = {"name" : "john","age" : 23 , "role" : "developer"}

user["salary"] = 100000

for a,b in user.items():  
    print(a,b)



# key name

for one in user.keys():
    print("keys :-",one)

# values

for two in user.values():
    print("values :-",two)


# list of dictionary

user_List=[]

user = {"name" : "john","age" : 23 , "role" : "developer"}

user["name"] = "ronaldo"

user_List.append(user)

print(user_List)

user1 = {"name" : "paul","age":25 , "role" : "python developer"}

user_List.append(user1)

print(user_List)


# Dictionary in list

user2 = {"name" : "dhoni","role" : "keeper","strength" : "bat"}


user2["played games"] = ["t20","world cup"] 

print(user2)

user2_list = ["t20","world cup"]

print(user2_list[0])

print(user2["played games"][0])





# set   - unique element only , not order - {}

color = {"black","red","white","orange","red"}

print(sorted(color))

print(list(color))

list_ran = ["1","2","3"]

print(set(list_ran))







# string formatting

name = "arun"

fruit1 = "apple"

fruit2 = "banana"

print(name + " like " + fruit1 + " and " + fruit2)


# formatting

text = '{0} like {2} and {1}'

print(text.format(name,fruit1,fruit2))



# padding 


print("***{msg:<10}***".format(msg="welcome"))
print("***{msg:>10}***".format(msg="welcome"))
print("***{msg:^11}***".format(msg="welcome"))



# formatting number

getVal = 3.2345

print("got the value : {:.1f}".format(getVal))

money = 10000000

print("have money {:,}".format(money))

num = 10 

print("101 binary value :- {:b}".format(num))
print("101 octal value :- {:o}".format(num))
print("101 hexa value :- {:x}".format(num))
print("101 scientific value :- {:e}".format(num))




"""


FUNCTION 

1. reusable
2. maintain , easy readable
3. making program
4. easy debugging and testing
5. easy to manipulate
6. perform functionality
7. we can give block (multiple code) inside
8. efficicency

"""


# def greet(parameter) :
#     print("hello")
#     print(parameter)

# greet("hi")


# def multiple_code(name) :

#     print(name)

#     for i in range(0,10):
#         print(i)

#     if(name) : 
#         print("condition true")

#     num1 = 10

#     print("number is {}".format(num1))

#     num2 = {"hello" : 60}

#     print(num2)

# multiple_code("ram")



# reusable


def form(name,department,cgpa):

    print("name : ", name)
    print("department : ",department)
    print("cgpa : ",cgpa)


form("praveen","ece",9)
form("kamal","Cse",8.56)


# program :  natural number find

def sum(num):

    print(num*(num+1)/2)

sum(20)



# return


def first_Val(value1,value2) :

    return value1+value2

print(first_Val(10,20))  

second_val = first_Val(20,20)

print(second_val)



def random(one) :

    print(one + second_val)

random(10)



def two() :
    print("two")

two()


def form1(name,department,disability="no"):

    print("name : ", name)
    print("department : ", department)
    print("disability : ",disability)

form1("john","EEE","yes")
form1("paul","IT")







