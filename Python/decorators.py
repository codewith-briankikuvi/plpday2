import time

def timer_decorator(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f"Execution Time: {end_time - start_time:.4f} seconds")
    return wrapper

@timer_decorator
def slow_function():
    time.sleep(2)
    print("Finished running slow function!")

# Call the decorated function
slow_function()
