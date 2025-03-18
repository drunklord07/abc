import random

# Function to generate a random 10-digit mobile number
def generate_random_mobile_number():
    return ''.join([str(random.randint(0, 9)) for _ in range(10)])

# Function to print 30 lines with random but ascending line numbers and random mobile numbers
def print_mobile_numbers():
    print("\033[95mStarting script to identify mobile numbers...\033[0m")  # Purple text for start message

    # Generate 30 random line numbers between 1 and 1000
    random_line_numbers = random.sample(range(1, 1001), 30)  # 30 unique random numbers between 1 and 1000

    # Sort the line numbers in ascending order
    random_line_numbers.sort()

    # Print the sorted random line numbers with random 10-digit mobile numbers
    for line_number in random_line_numbers:
        random_mobile_number = generate_random_mobile_number()  # Generate random mobile number
        print(f"\033[91m[Line {line_number}] Found mobile number: {random_mobile_number}\033[0m")  # Red text for line number

# Main function
def main():
    print_mobile_numbers()

if __name__ == '__main__':
    main()
