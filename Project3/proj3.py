import random

def get_random_value():
    return random.randint(0, 2)

def valid_input(user_input, options):
    try:
        options[user_input]
        return True;
    except IndexError:
        return False;

def won(usr_input, generated_input):
    if usr_input - generated_input == 0:
        return 0;

    match usr_input:
        case 0:
            if generated_input == 1: return -1
            elif generated_input == 2: return 1
        case 1:
            if generated_input == 2: return -1
            elif generated_input == 0: return 1
        case 2:
            if generated_input == 0: return -1
            elif generated_input == 1: return 1
        case _:
            return -1

def print_list(header, options):

    print(header)
    print("+" * 50)
    for count, option in enumerate(options):
        print(f"{count + 1}) {option}");
    print();

def get_user_input(prompt, valid_type="string"):
    match valid_type:
        case "string":
            response = str(input(prompt));
            return response;

        case "int":

            while True:
                try:
                    response = int(input(prompt))
                    return response;
                except ValueError:
                    print("invalid input, please retype your response.");
        case "float":

            while True:
                try:
                    response = float(input(prompt));
                    return response;
                except ValueError:
                    print("invalid input, please retype your response.");
        case _:
            print("feature not implemented");

def main():
    wins = 0;
    losses = 0;
    ties = 0;

    options = ["Rock", "Paper", "Scissors"]

    while True:
        print("Lets Play a Game...")
        print_list("Rock Paper Scissors", options);

        usr_input = get_user_input("Pick an option: ", valid_type="int");
        generated_input = get_random_value();

        if valid_input(usr_input - 1, options):
            print(f"User picks {options[usr_input - 1]}");
        else:
            print("invalid option");
            continue;

        result = won(usr_input - 1, generated_input)
        if result == 1:
            print("The User won")
            wins = wins + 1;
        elif result == -1:
            print("The User lost")
            losses = losses + 1;
        else:
            print("It was a tie")
            ties = ties + 1;

        print(f"Wins: {wins} Losses: {losses} Ties: {ties}");
        usr_input = get_user_input("Do you wish to play again? y/n:");

        if(usr_input == "n"):
            print("Thanks for playing");
            break;

main()