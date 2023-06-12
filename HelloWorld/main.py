# print function
# print("Hello World")
# first_name = "Mikhail"
# last_name = "Jacques"
# print("Hello " + first_name + " " + last_name)
# print("Aren't you are wonderful?")
# print(type(first_name))

# variable = a container for a value. Behaves as the value that it contains
# age = 49
# age = age + 1
# print(age)
# print(type(age))
# print("Your age is: " + str(age))

# height = 250.5
# print(height)
# print("Your height is: " + str(height) + " cm")
# print(type(height))
#
# human = True
# robot = False
# print(human)
# print(robot)
# print(type(robot))
# print("Are you a human: " + str(human))
#
# variable1, variable2, variable3 = "value1", "value2", "value3"
#
# print(variable1)
# print(variable2)
# print(variable3)
# print(len(variable3))

# string manipulation methods
# full_name = "Mikhail Jacques"
# print(len(full_name))
# print(full_name * 3)
# print(full_name.find("ha"))
# print(full_name.upper())
# print(full_name.lower())
# print(full_name.capitalize())
# print(full_name.isdigit())
# print(full_name.isalpha())
# print(full_name.count("a"))
# print(full_name.replace("a", "o"))

# type casting = convert the data type of value to another data type
# x = 1  # int
# y = 2.5  # float
# z = "3"  # str
#
# print(x)
# print(y)
# print(int(y))
# print(y * 3)
# print(z * 3)
#
# x = float(x)
# y = float(y)
# z = float(z)
#
# print(x)
# print(y)
# print(z)

# user input
# name = input("What is your name?: ")
# age = int(input("How old are you?: "))
# height = float(input("How tall are you?: "))
# age += 1
# print("Hello " + name)
# print("You are " + str(age) + " years old")
# print("You are " + str(height) + " cm tall")

# math functions
# import math
#
# print("Math")
#
# pi = 3.14
# x1 = 1
# y1 = 2
# z1 = 3
#
# print(round(pi))
# print(math.ceil(pi))
# print(math.floor(pi))
# print(abs(pi))
# print(max(x1, y1, z1))
# print(min(x1, y1, z1))

# string slicing = create a substring by extracting elements from another string
# first = full_name[:7]  # [0:3]
# print(first)
# last = full_name[8:]  # [8:end]
# print(last)
# funky_name = full_name[::2]  # [0:end:2]
# print(funky_name)
# reversed_name = full_name[::-1]  # [0:end:-1]
# print(reversed_name)
#
# website1 = "http://google.com"
# website2 = "http://wikipedia.com"
# website3 = "http://talentedmike.com"
#
# slice_instruction = slice(7, -4)
# print(website1[slice_instruction])
# print(website2[slice_instruction])
# print(website3[slice(6, -3)])

# if statement = a block of code that will execute if it's condition is true
# age = int(input('How old are you?: '))
#
# if age == 100:
#     print("You are a century old")
# elif age >= 18:
#     print("You are an adult!")
# elif age < 0:
#     print("You have not been born yet")
# else:
#     print("You are a child")


# logical operators (and, or) = used to check if two or more conditional statements are true
#
# temperature = int(input("What is the temperature outside?: "))
#
# if 0 <= temperature <= 30:  # temperature >= 0 and temperature <= 30:
#     print('The temperature is good today!')
#     print('Get outside!')
# elif temperature < 0 or temperature > 30:
#     print('The temperature is bad today!')
#     print('Stay inside!')
#
# if not (0 <= temperature <= 30):  # temperature >= 0 and temperature <= 30:
#     print('The temperature is good today!')
#     print('Get outside!')
# elif not (temperature < 0 or temperature > 30):
#     print('The temperature is bad today!')
#     print('Stay inside!')

# while loop = a statement that will execute its block of code, as long as it's condition remains true (unlimited)
# name = ""
# while len(name) == 0:
#     name = input("Enter your name: ")
# print("Hello " + name)

# for loop = a statement that will execute its block of code a limited number of times (limited)
# for ii in range(10):
#     print(ii+1)

# for ii in range(50, 100):
#     print(ii)

# for ii in range(50, 100+1, 2):
#     print(ii)

# import time
# for seconds in range(10, 0, -1):
#     print(seconds)
#     time.sleep(1)
# print("Happy New Year")

# # nested loops = The "inner loop" will finish all of its iterations before finishing one iteration of the "outer loop"
# rows = int(input("How many rows?: "))
# columns = int(input("How many columns?: "))
# symbol = input("Enter a symbol to use: ")
#
# for ii in range(rows):
#     for jj in range(columns):
#         print(symbol, end="")   # prevents cursor from moving to the next line5
#     print()

# Loop Control Statements = change execution of a loop execution from its normal sequence.
# break = used to terminate the loop entirely
# continue = skips to the next iteration of the loop
# pass = does nothing, acts as a placeholder

# while True:
#     name = input("Enter your name: ")
#     if name != "":
#         break

# phone_number = "123-456-7890"
# for ii in phone_number:
#     if ii == "-":
#         continue
#     print(ii, end="")

# for ii in range(1, 21):
#     if ii == 13:
#         pass
#     else:
#         print(ii)

# # list = used to store multiple items in a single variable
# food = ["pizza", "hamburger", "hotdog", "spaghetti", "pudding"]
#
# print(food[0])
# print(food[1])
# print(food[2])
# print(food[3])
# print(food[4])
# print()
#
# food[0] = "sushi"
#
# print(food[0])
# print(food[1])
# print(food[2])
# print(food[3])
# print(food[4])
# print()
#
# food.append("ice cream")
# for x in food:
#     print(x)
# print()
#
# food.remove("hotdog")
# for x in food:
#     print(x)
# print()
#
# food.pop()
# for x in food:
#     print(x)
# print()
#
# food.insert(0, "cake")
# for x in food:
#     print(x)
# print()
#
# food.sort()
# for x in food:
#     print(x)
# print()
#
# food.clear()
# for x in food:
#     print(x)
# print()

# # 2D lists = a list of separate lists
# drinks = ["coffee", "soda", "tea"]
# dinner = ["pizza", "hamburger", "hotdog"]
# dessert = ["cake", "ice cream"]
#
# food = [drinks, dinner, dessert]
# print(food)
# print()
#
# print(food[0][0])
# print(food[0][1])
# print(food[0][2])
# print()
#
# print(food[1][0])
# print(food[1][1])
# print(food[1][2])
# print()
#
# print(food[2][0])
# print(food[2][1])
# print()

# # tuple = collection which is ordered and unchangeable used to group together related data.
# student = ("Mikhail", 28, "male", "Mikhail")
# for x in student:
#     print(x)
# print()
#
# print("Count: " + str(student.count("Mikhail")))
# print()
#
# print(student.index("Mikhail"))
# print(student.index(28))
# print(student.index("male"))
# print()
#
# if "Mikhail" in student:
#     print("Mikhail is present!")
# print()


# set = collection which is unordered, unindexed. No duplicate values.
# utensils = {"fork", "spoon", "knife"}
# print(utensils)
# print()
#
# utensils.add("napkin")
# utensils.remove("fork")
# print(utensils)
# for x in utensils:
#     print(x)
# print()
#
# dishes = {"bowl", "plate", "cup", "cup", "cup", "knife"}
# print(dishes)
# print()
#
# # print only what utensils set has that dishes set does not have
# print(utensils.difference(dishes))
#
# # print only what dishes set has that utensils set does not have
# print(dishes.difference(utensils))
#
# # print only what both utensils set and dishes set have in common
# print(utensils.intersection(dishes))
#
# # create new set by joining two sets together
# dinner_table = utensils.union(dishes)
# print(dinner_table)
#
# # add all elements found in dishes to utensils set
# utensils.update(dishes)
# print(utensils)
# utensils.clear()

# # dictionary = a changeable, unordered collection of unique key-value pairs.
# # It is fast because it uses hashing and thus allows us to access a value quickly
# capitals = {'USA': 'Washington DC', 'India': 'New Deli', 'China': 'Beijing', 'Russia': 'Moscow', 'Israel': 'Jerusalem'}
# print(capitals)
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())
# print(capitals['Russia'])
# print(capitals.get('Germany'))
# print()
#
# capitals.update({'USA': 'Las Vegas'})
# capitals.update({'Germany': 'Berlin'})
# capitals.pop('China')
# print(capitals)
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())
# print(capitals['Germany'])
# print(capitals.get('Germany'))
# print()
#
# for key, value in capitals.items():
#     print(key, value)

# # index operator [] = gives access to a sequence's element (str, list, tuples)
# name = "mikhail Jacques"
# print(name)
#
# if (name[0].islower()):
#     name = name.capitalize()
# print(name)
#
# first_name = name[:7].upper()
# print(first_name)
# last_name = name[8:].lower()
# print(last_name)
# before_last_character = name[-2]
# print(before_last_character)
# last_character = name[-1]
# print(last_character)

# # function = block of code which is executed only when it is called
# def hello(first_name, last_name, age):
#     print("hello " + first_name + " " + last_name)
#     print("You are " + str(age) + " years old")
#     print("Have a nice day!")
#
#
# hello("Mikhail", "Jacques", 28)

# # return statement = functions send Python values/objects back to the caller.
# # These values/objects are known as the function's return value.
#
# def multiply(number1, number2):
#     return number1 * number2
#
#
# ret_val = multiply(6, 8)
# print(ret_val)

# # keyword arguments = arguments preceded by an identifier when we pass them to a function.
# # The order of the arguments does not matter. Unlike positional arguments Python knows
# # the names of the arguments that our function receives.
# def hello(first, middle, last):
#     print("Hello " + first + " " + middle + " " + last)
#
#
# hello(last="Jacques", middle="Dude", first="Mikhail")

# # nested function calls = function calls inside other function calls. The innermost function
# # calls are resolved first. The returned value is used as argument for the next function
# print(round(abs(float(input("Enter a whole positive number ")))))
#
# num = input("Enter a whole positive number ")
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)

# # scope = the region that a variable is recognized.
# # A variable is only available from inside the region it is created.
# # A global and local scope versions of a variable can be created.
# # LEGB rule = Local, Enclosing, Global, Built-in
#
# name = "Mikhail"  # global scope (available inside and outside functions)
#
#
# def display_name():
#     name = "Jacques"  # local scope (available only inside this function
#     print(name)
#
#
# print(name)
# display_name()


# # *args = parameter that will pack all arguments into a tuple.
# # It allows a function to accept a varying number of arguments
#
# def add(*args):
#     sum = 0
#     stuff = list(args)
#     stuff[0] = 0
#     stuff[5] = 5
#     for ii in stuff:
#         sum += ii
#     return sum
#
#
# print(add(1, 2, 3, 4, 5, 6))


# # **kwargs = parameter that will pack all arguments into a dictionary
# # It allows a function to accept a varying number of keyword arguments
# def hello(**kwargs):
#     # print("Hello " + kwargs['first'] + " " + kwargs['last'])
#     # print("Hello", end=" ")
#     for key, value in kwargs.items():
#         print(key, end=" ")
#         print(value)
#
#     for key, value in kwargs.items():
#         print(key, ":", value, end=" ")
#
#
# hello(title="Mr.", first="Mikhail", middle="Dude", last="Jacques")

# # str.format() = optional method that gives users more control when displaying output
# animal = "cow"
# item = "moon"
# print("The " + animal + " jumped over the " + item)
# print("The {} jumped over the {}".format(animal, item))
# print("The {1} jumped over the {0}".format(animal, item))   # positional argument
# print("The {animal} jumped over the {item}".format(animal="cow", item="moon"))   # keyword argument
# print("The {animal} jumped over the {animal}".format(animal="cow", item="moon"))   # keyword argument
# print("The {item} jumped over the {item}".format(animal="cow", item="moon"))   # keyword argument
#
# text = "The {} jumped over the {}"
# print(text.format(animal, item))
#
# name = "Mikhail"
# print("Hello, my name is {}. Nice to meet you".format(name))
# print("Hello, my name is {:10}. Nice to meet you".format(name))
# print("Hello, my name is {name:10}. Nice to meet you".format(name="Mike"))
# print("Hello, my name is {:<10}. Nice to meet you".format(name))    # left aligned within the padding
# print("Hello, my name is {:>10}. Nice to meet you".format(name))    # right aligned within the padding
# print("Hello, my name is {:^10}. Nice to meet you".format(name))    # centered within the padding
#
# number1 = 3.14159
# number2 = 1000
# print("The number PI is {:.3f}".format(number1))
# print("The number PI is {:,}".format(number2))
# print("The number PI is {:b}".format(number2))
# print("The number PI is {:o}".format(number2))
# print("The number PI is {:X}".format(number2))
# print("The number PI is {:E}".format(number2))

# #  random module for creating pseudo random numbers
# import random
#
# x = random.randint(1, 6)    # generates random integer number between 1 and 6
# print(x)
# y = random.random()         # generates random floating point number between 0 and 1
# print(y)
#
# choicesList = ['rock', 'paper', 'scissors']
# z = random.choice(choicesList)   # generate random choice for list of possible choices
# print(z)
#
# # deck of cards
# cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K", "A"]
# random.shuffle(cards)
# print(cards)

# # exception = events detected during execution that interrupt the flow of a program
# try:
#     numerator = int(input("Enter a number to divide: "))
#     denominator = int(input("Enter a number to divide by: "))
#     result = numerator / denominator
# except ZeroDivisionError as e:
#     print(e)
#     print("You can't divide by zero! Idiot")
# except ValueError as e:
#     print(e)
#     print("Enter only numbers plz")
# except Exception as e:
#     print(e)
#     print("Something went terribly wrong :(")
# else:
#     print(result)
# finally:
#     print("This will always execute")

# # file detection
# import os
#
# path = "D:\\GitHub\\Python\\test.txt"
#
# if os.path.exists(path):
#     print("That location exists!")
#     if os.path.isfile(path):
#         print("That is a file")
#     elif os.path.isdir(path):
#         print("That is a directory")
# else:
#     print("That location doesn't exist!")

# # reading contents of a file line by line
# try:
#     with open('test2.txt') as file:
#         print(file.read())
# except FileNotFoundError:
#     print("That file has not been found) :(")
#
# flag = file.closed
# print(flag)

# # writing to file
# text = "Yooooooooo\nThis is some text\nHave a good one!\n"
# with open('test.txt', 'w') as file:
#     file.write(text)
#
# # appending to file
# text = "Some more text\nIsn't that kewl?"
# with open('test.txt', 'a') as file:
#     file.write(text)

# # copy files
# # copyfile() = copies contents of a file
# # copy() = copyfile() + permission mode + destination can be a directory
# # copy2() = copy() + copies metadata (file's creation and modification times)
# import shutil
#
# # copies contents of a file
# shutil.copyfile('test.txt', 'copy1.txt')
#
# # copies contents of a file + permission mode + destination can be a directory
# shutil.copy('test.txt', 'D:\\GitHub\\Python\\HelloWorld\\copy2.txt')
#
# # copies contents of a file + permission mode + destination can be a directory +
# # copies metadata (file's creation and modification times)
# shutil.copy2('test.txt', 'copy3.txt')

# # moving files and/or directory (folder)
# import os
# source = "copy1.txt"
# destination = "D:\\GitHub\\Python\\copy1.txt"
#
# try:
#     # if you do not care replacing any existing files the following 'if' part may be omitted
#     if os.path.exists(destination):
#         print("There is already a file there")
#     else:
#         os.replace(source, destination)
#         print(source + " was moved to " + destination)
# except FileNotFoundError:
#     print(source + " was not found")

# # deleting files
# import os
# import shutil
# path = 'copy2.txt'
# # path = 'empty_folder'
#
# try:
#     os.remove(path)           # delete a file
#     # os.rmdir(path)            # delete an empty directory or a file
#     # shutil.rmtree(path)       # delete a directory containing files
# except FileNotFoundError:
#     print("That file was not found")
# except PermissionError:
#     print("You do not have permission to delete that")
# except OSError:
#     print("That folder contains files")
# else:
#     print(path + " deletion was successful")

# module = a file containing python code. May contain functions, classes, etc.
# Used with modular programming, which is to separate a program into parts

# import messages
# import messages as m
# from messages import hello.bye
# from messages import * (this one is dangerous)



