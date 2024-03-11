def count_chars(input_str):
    # Initialize counters
    count_alphabets = 0
    count_digits = 0
    count_spaces = 0

    # Convert the string to uppercase
    input_str = input_str.upper()

    # Count alphabets, digits, and spaces
    for char in input_str:
        if char.isalpha():
            count_alphabets += 1
        elif char.isdigit():
            count_digits += 1
        elif char.isspace():
            count_spaces += 1

    return count_alphabets, count_digits, count_spaces

# Get input from the user
input_string = input("Enter the string: ")

# Count alphabets, digits, and spaces, and display the result
alphabets, digits, spaces = count_chars(input_string)
print(f"Number of Alphabets: {alphabets}")
print(f"Number of Digits: {digits}")
print(f"Number of Spaces: {spaces}")
