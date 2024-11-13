import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution Time: {end_time - start_time} seconds")
        return result
    return wrapper

# @timer_decorator
# def slow_function():
#     time.sleep(2)
#     print("Function complete!")

# slow_function()

@timer_decorator
def fibo(num):
    if num <= 1:
        return num

    return fibo(num - 1) + fibo(num - 2)


print(fibo(5))

