def display_menu():
    print("\nMenu:")
    print("1. Union of Sets")
    print("2. Intersection of Sets")
    print("3. Difference of Sets")
    print("4. Symmetric Difference of Sets")
    print("5. Quit")

def perform_union(set1, set2):
    return set1.union(set2)

def perform_intersection(set1, set2):
    return set1.intersection(set2)

def perform_difference(set1, set2):
    return set1.difference(set2)

def perform_symmetric_difference(set1, set2):
    return set1.symmetric_difference(set2)

# Main program loop
while True:
    display_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        set1 = set(input("Enter elements of the first set (comma-separated): ").split(','))
        set2 = set(input("Enter elements of the second set (comma-separated): ").split(','))
        result = perform_union(set1, set2)
        print(f"Union of Sets: {result}")
    elif choice == '2':
        set1 = set(input("Enter elements of the first set (comma-separated): ").split(','))
        set2 = set(input("Enter elements of the second set (comma-separated): ").split(','))
        result = perform_intersection(set1, set2)
        print(f"Intersection of Sets: {result}")
    elif choice == '3':
        set1 = set(input("Enter elements of the first set (comma-separated): ").split(','))
        set2 = set(input("Enter elements of the second set (comma-separated): ").split(','))
        result = perform_difference(set1, set2)
        print(f"Difference of Sets: {result}")
    elif choice == '4':
        set1 = set(input("Enter elements of the first set (comma-separated): ").split(','))
        set2 = set(input("Enter elements of the second set (comma-separated): ").split(','))
        result = perform_symmetric_difference(set1, set2)
        print(f"Symmetric Difference of Sets: {result}")
    elif choice == '5':
        print("Quitting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
