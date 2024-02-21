#Practice Question
dict = {"marks":[]}
while True:
    user_input = input("Enter a number (or 'n' to finish): ")
    if user_input.lower() == 'n':
        break
    num = int(user_input)
    dict["marks"].append(num)
print(dict)
dict["marks"].sort()
print(dict)