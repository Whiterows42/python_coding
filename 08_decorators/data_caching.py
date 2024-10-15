

import time
def cache(fun):

    cached_value = {}
    print(cached_value)

    def wrapper(*args , **kwargs):
      if args in cached_value:
         return cached_value[args]
      
      result =  fun(*args , **kwargs)
      cached_value[args] = result

      return result
    return wrapper

@cache
def example_fun(a,b):
   time.sleep(4)
   return a+b
   

print(example_fun(4,5))
print(example_fun(4,5))
print(example_fun(4,7))