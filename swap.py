def swap_odd_even_positions(input_str):
    chars = list(input_str)
    for i in range(0, len(chars)-1, 2):
        chars[i], chars[i+1] = chars[i+1], chars[i]
    return ''.join(chars)

# Get input from the user
input_string = input("Enter the string: ")

# Swap odd and even positions and display the result
result = swap_odd_even_positions(input_string)
print(f"Result after swapping odd and even positions: {result}")
