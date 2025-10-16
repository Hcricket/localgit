# print ("Hello World")
# print("Hello New York City")
# print(3*5)
# print(input("what is your name:"))
# my_name = input("what is your name:")
# print("Hello"+ my_name)

# first_num = int(input("enter your first number:"))
# second_num= int(input("enter your second number:"))
# print("The sum of your number is:"+ str(first_num + second_num))
# age = 30
# print(age)
# first_name = "HCricket"
# last_name  = "Aung"
# full_name  = first_name + last_name
# print (full_name)
# x=5
# y=7
# z =x+y
# print(z)
# Data types number
# int
# x = 5 
# y = -12
# floats x=3.124


# String 
# name ="HCricket"
# message= "Hello world"
# full_name=name+"Hein"


# Boolean 
# is_student = True
# is_enrolled = False
# print(is_student and is_enrolled) #Output: True and False = False

# Lists (collection of items and mutable which means you can change their content)
# Lists = Arry in JS
# fruits =["apple","banana","orange"]
# print(fruits[0])  #"apple"
# fruits.append("grape") #append means add
# print(fruits)

# Tuple(lists-immutable(cannot change))
# numbers = (1,2,3)
# print(numbers[0])

# Dictionaries
# person = { "name": "John","age":30}
# print(person["name"])  #"John"

#  add or modify
# person["salary"]=2500.50
# person["age"]=31
# print(person)

# Numeric operations in Python
# a = 10
# b = 3
# addition +
# subtraction -
# multiplication(*)
# division  a/b
# modulo  a%b (remainder)
# exponent a ** b (2*2*2)
# c = 7
# d = 2
# floor_division c//d  #3
# abosolute = abs (-10) #10
# rounding= round(3.14159,2)  #rounding:3.14


# Logical operation
# AND,OR,not

# if-else statement
# number = 7
# if number % 2 == 0:
#  print ("The number is even")
# else:
#  print("The number is odd.")

# score = 85
# if score >= 90:
#   print("Grade-A")
# elif score >= 80:
#   print("Grade-B")
# elif score >=70:
#   print("Grade-C")


# temperature = float(input("Enter the temperature in Celsius:"))
# if temperature < 0:
#   print("It is freezing")
# elif temperature>25:
#   print("It is hot")
# else:
#   print("Temperature is pleasant")


# username = input("Enter your username:")
# password = input("enter your password:")
# if username == "admin"  and password == "password":
#   print("login successful!")
# else: print("Invalid username or password")


# Built-in data structures
# List [order collection -commonly use][mutable][]
# my_list = [1,2,3,4,5]
# print(my_list[-1]) #5
# print(my_list[2])  #3
# my_list[2]=10
# my_list.append(6)
# my_list.remove(4)
# print(my_list)

# tuple(immutable-cannot modified) (comma-separated values)()
# my_tuple = (1,2,3,4,5)
# print(my_tuple[-3])
# print(my_tuple[1])


# Sets(unorder collection/unique elements)without any duplicates {} or ()
# set1 = {1,2,3}
# set2 ={3,4,5}
# print(set1.union(set2)) #{1,2,3,4,5}
# print(set1.intersection(set2)) {3}
# print(set1.difference(set2)) {1,2}
# print(set2.difference(set1)) {4,5}


# c = 7
# d = 2
# Logical operation in Python
# AND OR NOT 
# number = 7
# if number % 2 == 1:
#   print("the number is even")
# else:
#     print("the number is odd.")

# score = 85 
# if score >= 90:
#   print("gradeA")
# elif score >= 80:
#   print("gradeB")
# elif score >= 70:
#   print("gradeC")
# elif score >= 60:
#   print("gradeF")
# else:
#   print("fail")


# temperature = float (input ( "Enter the temperature in Celsius"))
# if temperature < 0:
#   print("It is freezing cold")
# elif temperature > 25:
#   print("It is hot outside")
# else:
#   printl("the temperature is pleasant")


# username = input("Enter your username")
# password = input ("Enter your password")
# if username == "CRICKET" and password == "password":
#   print("login successful")
# else:
#   print("Invalid username or password")

#  Python built-in data structures/List,Tuples,Sets,Dictionaries
#  List [] mutable 
# my_list = [1,2,3,4,5] []][][][[][]][][[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
# # print(my_list[0])
# # print(my_list[-1])
# # print(my_list[2])
# # print(my_list[-2])
# my_list[2]=10
# my_list.append(6)
# my_list.remove(4)
# print(my_list)

# Tuples /immutable /cannot be modified ()()()(()()()()()()()())
# my_tuple =(1,2,3,4,5)
# print(my_tuple[3])
# print(my_tuple[-3])

# SET /unordered collections of unique elements/not duplicate
# my_set = {1,2,3,4,5}
# set1 = {1,2,3}
# set2 ={3,4,5,6}
# print(set1.union(set2))
# print(set1.intersection(set2))
# print(set1.difference(set2))
# print(set2.difference(set1))

# # Dictionaries/key-value pairs ,
# my_dict = {"name":"John","age":25,"city":"New York"}
# print(my_dict["name"])
# print(my_dict["age"])
# print(my_dict["city"])
# my_dict["name"]="cricket"
# my_dict["age"]="21"
# my_dict["city"]="LA"

# print(my_dict["name"])
# print(my_dict["age"])
# print(my_dict["city"])
#  Function /def/
# def greet():
#   print("Hello World")
#   greet()
# def greet(name,age):
#   print(f"Hello,{name}! You are{age}years old")
# greet("Hein",21)
  
#  def calculate_area(radius):
#   return math.pi   *radius**2
#   circle_radius = 5
#   area = calculate_area(circle_radius)
#   
# def happy_birthday(name,age):
#   print(f"Happy birthday to {name}!")
#   print(f"You are {age} old")
#   print("Happy birthday to you")

# happy_birthday("bro",21)
# happy_birthday("Cricket",34)
# happy_birthday("Hein",35)

# def display_invoice(username,amount,due_date):
#     print(f"Hello{username}")
#     print(f"Your bill of ${amount:.2f},your due date:{due_date}")

# display_invoice("Cricket",2500,"01/01")

# def Cricket(name,age,nickname):
#     print(f"your name is {name}")
#     print(f"your age is {age} and your nickname is {nickname}")

# Cricket("Hein",21,"HCricket")


# def my_memory(country,time,work):
#     print(f"I came to the  {country}. in 2017 december,on December 07{time}to kentucky")
#     print(f"I work at active duty {work}")
# my_memory("USA",1200,"Army")

# def my_mother(city,trip,age):
#   print(f"I am Daw phwar than came to {city}went to {trip} and i am  {age} year old")


# my_mother("NYC","washigton",67)


# def my_mother(city, trip, age):
#     print(f"I am Daw Phwar Than. I came to {city}, went to {trip}, and I am {age} years old.")

# my_mother("NYC", "Washington", 67)

# def greet(name):
#   print(f"Hi{name}")
# greet("Circket")


# def increment(number,by=1):
#     return number + by
# # print(increment(1,2))

# result =increment(2)
# print(result)    

login_attempt =0
max_attempt = 3
authenicated = False

while login_attempt < max_attempt:
 username = input("Enter your username")
 password = input ("enter your password")

if (username=="Cricket") and (password=="USA123"):
    authenicated = True
    break
else:
    print("invalid username or password")
    login_attempt +=1


if authenicated:
      print("Authentication successful")
else:
      print("max login attempts")  