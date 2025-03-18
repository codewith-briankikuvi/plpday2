# Dictionaries use key-value pairs and they're mutable
# Dictionaries are unordered, but they maintain the order of insertion in Python 3.7 and later

countries = {
    'Kenya':'Nairobi', 
    'Uganda': 'Kampala', 
    'Tanzania':'Dodoma', 
    'Rwanda':'Kigali'}
print(countries)
print(countries['Kenya']) #Nairobi

"""Kenya - Key
   Nairobi - Value
   The key and value are separated by a colon
"""

students = {
    'name': 'Brian',
    'age': 21,
    'course': 'Computer Science',
    'gender': 'male',
    'hobbies': ['coding', 'nature walks', 'swimming'],

    'my_name': {
        'first_name': 'Brian',
        'last_name': 'Kikuvi'
    }
}
print(students)
print(students['name']) #Brian
print(students['hobbies']) #['coding', 'nature walks', 'swimming']

# we can also add a key and value inside the students
students['email'] = 'brian@gmail.com'
students['height'] = 5.4
print(students)