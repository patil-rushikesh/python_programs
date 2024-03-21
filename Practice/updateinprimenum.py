#Write a program to print all the prime numbers in the given range from a to b
def checkprime(num):
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                break
        else:
            print(num)

a = int(input("Enter the starting range : "))
b = int(input("Enter the Ending range : "))
i = a
while i<=b:
    checkprime(i)
    i=i+1