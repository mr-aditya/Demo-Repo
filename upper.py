def convert_last_char_to_uppercase(input_str):
    words = input_str.split()
    result_words = []

    for word in words:
        if word:
            # Extract the last character, convert it to uppercase, and concatenate with the rest of the word
            modified_word = word[:-1] + word[-1].upper()
            result_words.append(modified_word)

    result_string = ' '.join(result_words)
    return result_string

# Get input from the user
input_string = input("Enter the string: ")

# Convert the last character of each word to uppercase and display the result
result = convert_last_char_to_uppercase(input_string)
print(f"Result after converting the last character of each word to uppercase: {result}")
