import time

# Record the start time
start_time = time.time()

# Your code block
numbers = [23, 37, 84, 56, 78, 34, 23, 37, 81, 56, 74, 46]

for num in numbers:
    if num % 2 == 0:
        print(num)

# Record the end time
end_time = time.time()

# Calculate and display the execution time
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")