age = 25 #integer
height = 5.75 #float
name = "John" #string
is_student = True #boolean

print(f'Name: {name}, Age: {age}, Height: {height}, Is Student: {is_student}')

print(type(name)) #outputs name data type
print(type(age)) #outputs age data type
print(type(height)) #outputs height data type
print(type(is_student)) #outputs is_student data type

#Dynamic Typing
my_age = 21
print(my_age) #outputs 21
my_age = "21 years old" #outputs 21 years old
print(my_age)

print(my_age) #outputs 21 years old
print(f'I am {my_age}') #outputs I am 21 years old

