numbers = [ 1,2,3,-4,-5,-6 , 44 , 30 , -60]

postive_number_count = 0

for num in numbers:
    if num < 0 :
        postive_number_count +=1

print("postive number count is " , postive_number_count) 