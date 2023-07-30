def logger(func):
    def wrapper(*args, **kwargs):
        arg_list = ", ".join([str(arg) for arg in args] + [f"{k}={v}" for k, v in kwargs.items()])
        print(f"{func.__name__} called with {arg_list}")
        return func(*args, **kwargs)
    return wrapper

@logger
def add(x, y):
    return x + y

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

add(4, 5)
square_all(1, 2, 3)
