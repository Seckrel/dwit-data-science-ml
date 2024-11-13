def logger_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Arguments: {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@logger_decorator
def add(a, b):
    return a + b

print(add(3, b=4))
