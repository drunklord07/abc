import random

# Function to print 30 lines with random but ascending line numbers
def print_mobile_numbers():
    print("\033[95mStarting script to identify mobile numbers...\033[0m")  # Purple text for start message

    dummy_mobile_number = "1234567890"  # Dummy mobile number for demonstration

    # Generate 30 random line numbers between 1 and 1000
    random_line_numbers = random.sample(range(1, 1001), 30)  # 30 unique random numbers between 1 and 1000

    # Sort the line numbers in ascending order
    random_line_numbers.sort()

    # Print the sorted random line numbers with dummy mobile number
    for line_number in random_line_numbers:
        print(f"\033[91m[Line {line_number}] Found mobile number: {dummy_mobile_number}\033[0m")  # Red text for line number

# Main function
def main():
    print_mobile_numbers()

if __name__ == '__main__':
    main()
