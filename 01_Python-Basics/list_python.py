list = ["ajit", "mote" , "orange" , "apple"]

print(list)



print(list[:3])
print(list[3:])
print(list[2:3])
# list[2:3] = "mongo"
# print(list)

list[2:3] = ["mongo"]
print(list)

for c in list:
    if c == "ajit":
        print("hello ajit")

        print(c , end="-")



if "ajit" in list:
    print("ajit present in the chat")



newlist = [x **2 for x in range(10)]
print(newlist)

n = 2
if n%2 ==0:
    print("is")