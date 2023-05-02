# print
print("Hello World")
first_name = "Mikhail"
last_name = "Jacques"
print("Hello " + first_name + " " + last_name)
print("Aren't you are wonderful?")
print(type(first_name))

# variable = a container for a value. Behaves as the value that it contains
age = 49
age = age + 1
print(age)
print(type(age))
print("Your age is: " + str(age))

height = 250.5
print(height)
print("Your height is: " + str(height) + " cm")
print(type(height))

human = True
robot = False
print(human)
print(robot)
print(type(robot))
print("Are you a human: " + str(human))

variable1, variable2, variable3 = "value1", "value2", "value3"

print(variable1)
print(variable2)
print(variable3)
print(len(variable3))

# string manipulation methods

full_name = "Mikhail Jacques"
print(len(full_name))
print(full_name * 3)
print(full_name.find("ha"))
print(full_name.upper())
print(full_name.lower())
print(full_name.capitalize())
print(full_name.isdigit())
print(full_name.isalpha())
print(full_name.count("a"))
print(full_name.replace("a", "o"))

# type casting = convert the data type of value to another data type

x = 1  # int
y = 2.5  # float
z = "3"  # str

print(x)
print(y)
print(int(y))
print(y * 3)
print(z * 3)

x = float(x)
y = float(y)
z = float(z)

print(x)
print(y)
print(z)

# user input

# name = input("What is your name?: ")
# age = int(input("How old are you?: "))
# height = float(input("How tall are you?: "))
# age += 1
# print("Hello " + name)
# print("You are " + str(age) + " years old")
# print("You are " + str(height) + " cm tall")

# math functions
import math

print("Math")

pi = 3.14
x1 = 1
y1 = 2
z1 = 3

print(round(pi))
print(math.ceil(pi))
print(math.floor(pi))
print(abs(pi))
print(max(x1, y1, z1))
print(min(x1, y1, z1))

# string slicing = create a substring by extracting elements from another string

first = full_name[:7]  # [0:3]
print(first)
last = full_name[8:]  # [8:end]
print(last)
funky_name = full_name[::2]  # [0:end:2]
print(funky_name)
reversed_name = full_name[::-1]  # [0:end:-1]
print(reversed_name)

website1 = "http://google.com"
website2 = "http://wikipedia.com"
website3 = "http://talentedmike.com"

slice_instruction = slice(7, -4)
print(website1[slice_instruction])
print(website2[slice_instruction])
print(website3[slice(6, -3)])

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

temperature = int(input("What is the temperature outside?: "))

if 0 <= temperature <= 30:  # temperature >= 0 and temperature <= 30:
    print('The temperature is good today!')
    print('Get outside!')
elif temperature < 0 or temperature > 30:
    print('The temperature is bad today!')
    print('Stay inside!')

if not (0 <= temperature <= 30):  # temperature >= 0 and temperature <= 30:
    print('The temperature is good today!')
    print('Get outside!')
elif not (temperature < 0 or temperature > 30):
    print('The temperature is bad today!')
    print('Stay inside!')
