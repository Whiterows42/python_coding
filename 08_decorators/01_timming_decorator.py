

import time

def timmer(fun):
    def wrapper(*args, **kwargs):
        star = time.time()
        result = fun(*args, **kwargs)
        end = time.time()

        print(f"{fun.__name__} ran in {end} time ")

        return result
    return wrapper

@timmer
def example_fun(n):
    print(time.time())
    time.sleep(n)
    print("hello ajit")
    print(time.time())


example_fun(2)