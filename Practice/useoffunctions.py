#Practice Question
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
        return x / y

def display_menu():
    print("Welcome to the calculator:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")


while True:
    display_menu()
    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice in ('1', '2', '3', '4'):
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        dict = dict(x = 23, y = 56)
        if choice == '1':
            print("Result:", add(**dict))
        elif choice == '2':
            print("Result:", subtract(a, b))
        elif choice == '3':
            print("Result:", multiply(a, b))
        elif choice == '4':
            print("Result:", divide(a, b))
    elif choice == '5':
        print("Thank you for using the calculator.")
        break
    else:
        print("Invalid input. Please enter a valid choice.")
        