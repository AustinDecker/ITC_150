# this programs asks for the user's age and displays whether or not 
# this individual is a an infant, child, teenager, or adult.

# helper function that strictly looks for number input.
def get_number_input(message, error_message="invalid input, try again."):
    usr_input = "";

    while True:
        try:
            usr_input = int(input(message));
            return usr_input;
        except ValueError:
            print(error_message);

#logic for checking user age.
def check_age(user_age):
    INFANT, CHILD, TEEN = 1, 12, 19;
    if(user_age < 0):
        return "UNBORN"

    if user_age > TEEN:
        return "ADULT";
    elif user_age > CHILD:
        return "TEEN";
    elif user_age > INFANT:
        return "CHILD"
    else:
        return "INFANT"

#entrypoint of program
def main():
    user_age = get_number_input("What is your age?: ");
    response = check_age(user_age);
    print(f"You are a(an) {response} because you are {user_age} years old.");


main();