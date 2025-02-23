import math

# helper function that strictly looks for number input.
def get_number_input(message, error_message="invalid input, try again."):
    usr_input = "";

    while True:
        try:
            usr_input = int(input(message));
            return usr_input;
        except ValueError:
            print(error_message);

def is_prime(number):
    if number <= 1:
        return False;

    if number == 2 or number == 3:
        return True;

    if number % 2 == 0 or number % 3 == 0:
        return False;

    for i in range(5, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False;
    return True;

def main():
    user_input = get_number_input("Please enter a number: ");
    if(is_prime(user_input)):
        print("This is a prime number.");
    else:
        print("This is not a prime number.");

main()