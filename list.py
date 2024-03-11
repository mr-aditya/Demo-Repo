# Initialize an empty list to store data
data_list = []

def display_menu():
    print("\nMenu:")
    print("1. Add data")
    print("2. Delete data")
    print("3. Append data")
    print("4. View data")
    print("5. Quit")

def add_data():
    data = input("Enter data to add: ")
    data_list.append(data)
    print(f"Data '{data}' added successfully.")

def delete_data():
    if not data_list:
        print("No data to delete.")
        return

    print("Current Data:")
    for index, data in enumerate(data_list, 1):
        print(f"{index}. {data}")

    try:
        index_to_delete = int(input("Enter the index to delete: "))
        if 1 <= index_to_delete <= len(data_list):
            deleted_data = data_list.pop(index_to_delete - 1)
            print(f"Data '{deleted_data}' deleted successfully.")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")

def append_data():
    data_to_append = input("Enter data to append: ")
    data_list.append(data_to_append)
    print(f"Data '{data_to_append}' appended successfully.")

def view_data():
    if not data_list:
        print("No data to view.")
        return

    print("Current Data:")
    for index, data in enumerate(data_list, 1):
        print(f"{index}. {data}")

# Main program loop
while True:
    display_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add_data()
    elif choice == '2':
        delete_data()
    elif choice == '3':
        append_data()
    elif choice == '4':
        view_data()
    elif choice == '5':
        print("Quitting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
