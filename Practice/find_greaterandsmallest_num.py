a = int(input("Num 1 : "))
b = int(input("Num 2 : "))
c = int(input("Num 3 : "))

#finding largest

if a > b and a > c :
    print("Largest Number is : ", a)
elif b > a and b > c :
    print("Largest Number is : ", b)
else : 
    print("Largest Number is : ", c)

#finding Smallest

if a < b and a < c :
    print("Smallest Number is : ", a)
elif b < a and b < c :
    print("Smallest Number is : ", b)
else : 
    print("Smallest Number is : ", c)