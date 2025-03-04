numbers = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
even_numbers = []
odd_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)
print('Even Numbers:')
print(even_numbers)
print('Odd Numbers:')
print(odd_numbers)

