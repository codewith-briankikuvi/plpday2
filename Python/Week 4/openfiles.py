# Simple code to open and read a file
try:
    with open('Week 4/example.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("The file does not exist.")

"""
file.readline() outputs the first line
file.readlines() ouputs all the lines in a list, each line separated by a comma.
"""

# Example of writing to a file
with open('output.txt', 'w') as file:
    file.write('This is a test.')

# Example of appending to a file; writing to a file that already exists without overwriting
with open('output.txt', 'a') as file:
    file.write('\nThis is an appended line.')
    print('Appended to file.')

# writing multiple lines to a file
with open('languages.txt', 'w') as file:
    lines = ['Python\n', 'JavaScript\n', 'C++\n', 'Java\n', 'Swift\n']
    file.writelines(lines)
    print('Multiple lines written to file.')