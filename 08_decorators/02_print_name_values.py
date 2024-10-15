


def debug(fun):
    def wrapper(*args , **kwargs):

        arges_value = ", ".join(str(arg) for arg in args)

        key_values = ", ".join(f"{k} = {v}" for k , v in kwargs.items())

        print(f"calling {fun.__name__} with args {arges_value}  and kwargs {key_values}")
        return fun(*args, **kwargs)
    return wrapper
 



@debug
def greet(name , greeting = "hello"):

    print(f"{name}  {greeting} ")


greet("ajit" , greeting= "chai")