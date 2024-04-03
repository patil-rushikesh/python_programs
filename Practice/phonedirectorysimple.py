def add_entry(directory):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    place = input("Enter place: ")

    if len(phone) != 10 or not phone.isdigit():
        print("Phone number should be a 10-digit number.")
        return

    directory[name] = {"phone": phone, "place": place}
    print("Entry added successfully!")

def remove_entry(directory):
    name = input("Enter name to remove: ").lower()
    if name in directory:
        del directory[name]
        print("Entry removed successfully!")
    else:
        print("Entry not found.")
def search_entry(directory):
    search_type = input("Enter search type (name/phone/place): ").lower()
    search_query = input("Enter search query: ").lower()
    found = False

    if search_type == "name":
        for name, details in directory.items():
            if search_query in name.lower():
                print("Name:", name)
                print("Phone:", details["phone"])
                print("Place:", details["place"])
                found = True
    elif search_type == "phone":
        for name, details in directory.items():
            if search_query in details["phone"]:
                print("Name:", name)
                print("Phone:", details["phone"])
                print("Place:", details["place"])
                found = True
    elif search_type == "place":
        for name, details in directory.items():
            if search_query in details["place"].lower():
                print("Name:", name)
                print("Phone:", details["phone"])
                print("Place:", details["place"])
                found = True
    else:
        print("Invalid search type.")

    if not found:
        print("Entry not found.")




def view_directory(directory):
    if not directory:
        print("Directory is empty.")
    else:
        for name, details in directory.items():
            print("Name:", name)
            print("Phone:", details["phone"])
            print("Place:", details["place"])
            print()


def phone_directory():
    directory = {}

    while True:
        print("\nPhone Directory Options:")
        print("1. Add entry")
        print("2. Remove entry")
        print("3. Search entry")
        print("4. View directory")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_entry(directory)
        elif choice == "2":
            remove_entry(directory)
        elif choice == "3":
            search_entry(directory)
        elif choice == "4":
            view_directory(directory)
        elif choice == "5":
            print("Exiting phone directory.")
            break
        else:
            print("Invalid choice. Please choose again.")


if __name__ == "__main__":
    phone_directory()
