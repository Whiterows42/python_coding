chai = "masala chai"

print(chai)


newcha = chai[0:6]
print(newcha)


list = [1,2,3,4,5]

print(list[3:])


cha2 = "    masala chai     "
print(cha2.strip())


chai3 = "lemon chai"
chai3replace = chai3.replace("lemon","mint")

print(chai3replace)


listString = "lemon , mint , coffee, taza"

print(listString.split(", "))

fintchai = "lemon chai"
print(fintchai.find("chai"))

countChai = "chai chai chai"
print(countChai.count("chai"))


fname = "ajit"
lname = "mote"

xyz = " hello my name is {} {}"
# print(xyz.format(fname = fname, lname = lname))
print(xyz.format(fname , lname ))


string_list = ["masala", "ginger" , "min"]
list_to_string = "-".join(string_list)
print(list_to_string)



folderpath = r"c:\user\aksha"
print(folderpath)