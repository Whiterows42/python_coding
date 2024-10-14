
x = 10
def fun2(n):
    z = x + n

    return z

# print(fun2(10))


def fun3():
    x = 10

    def inner():
        print(x)
    return inner

# result = fun3()
# result()




# pure closuere

def chaiorcode(n):
    print("n" , n)
    def actual(x):
        print("x",x)
        return x ** n
    return actual

f = chaiorcode(2)
g = chaiorcode(3)

print(f(2))