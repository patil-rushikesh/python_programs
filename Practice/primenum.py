#Write a program to print all the prime numbers in the given range
def checkprime(num):
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                break
        else:
            print(num)

n = int(input("Enter the range"))
i = 1
while i<=n:
    checkprime(i)
    i=i+1