#Write a program to print all the prime numbers in the given range using recursion
def checkprime(num, x=None):
    if num < 2:
        return False

    if x is None:
        x = num - 1

    if x == 1:
        return True

    if num % x == 0:
        return False

    return checkprime(num, x - 1)

n = int(input("Enter the range: "))
for i in range(1, n + 1):
    if checkprime(i):
        print(i)
