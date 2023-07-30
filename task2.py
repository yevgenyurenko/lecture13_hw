import functools

def stop_words(words: list):
    def decorator(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            for word in words:
                result = result.replace(word, "*")
            return result
        return inner
    return decorator

@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
