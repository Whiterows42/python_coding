

def even_genrator(limit):
    for i in range(2 , limit +1 , 2):
        yield i

for i in even_genrator(10):
    print(i)
