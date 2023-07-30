def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        def wrapper(*args, **kwargs):
            
            if len(args) != 1:
                print("Error: The function must take exactly 1 argument.")
                return False
            
            arg = args[0]
            
            if not isinstance(arg, type_):
                print(f"Error: Argument should be of type {type_.__name__}.")
                return False
            
            if len(arg) > max_length:
                print(f"Error: Argument length exceeds the maximum allowed length of {max_length}.")
                return False
            
            for symbol in contains:
                if symbol not in arg:
                    print(f"Error: Argument should contain all of the following symbols: {', '.join(contains)}.")
                    return False
          
            return func(*args, **kwargs)
        
        return wrapper
    return decorator


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'

