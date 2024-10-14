

score = int(input("Enter your scroe"))

if score >= 101 :
    print("verify your grade")
    exit()

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"

elif score >= 70:
    grade = "C"
elif score >= 60 :
    grade = "d"

else :
    grade = "F"
print(grade)   