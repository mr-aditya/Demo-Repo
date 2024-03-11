def is_armstrong_number(num):
    order = len(str(num))
    sum_of_digits = sum(int(digit) ** order for digit in str(num))
    return num == sum_of_digits

def armstrong_numbers_in_interval(start, end):
    print(f"Armstrong numbers in the interval [{start}, {end}]:")
    for number in range(start, end + 1):
        if is_armstrong_number(number):
            print(number)

# Get input from the user
start_interval = int(input("Enter the start of the interval: "))
end_interval = int(input("Enter the end of the interval: "))

# Print Armstrong numbers in the interval
armstrong_numbers_in_interval(start_interval, end_interval)
