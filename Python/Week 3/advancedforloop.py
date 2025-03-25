import time
start_time = time.time()
numbers = [23, 37, 84, 56, 78, 34, 23, 37, 81, 56, 74, 46]

even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
        even_numbers.sort(reverse=True)

print(f'even numbers: {even_numbers}')
end_time = time.time()
print(f'Time taken: {end_time - start_time} seconds')