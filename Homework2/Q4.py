# helper function that strictly looks for number input.
def get_number_input(message, error_message="invalid input, try again."):
    usr_input = "";

    while True:
        try:
            usr_input = int(input(message));
            return usr_input;
        except ValueError:
            print(error_message);

def main():
    total = 0;
    while True:
        usr_input = get_number_input("Enter a positive number to add to the sum, or a negative to calculate the total and exit: ");
        if(usr_input < 0):
            print(f"The total of your entered numbers is {total}");
            break;
        total += usr_input;
main();