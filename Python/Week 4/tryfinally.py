try:
    with open('languages.txt', 'r') as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print("The file does not exist.")
finally:
    # file.close()
    print("File closed.")