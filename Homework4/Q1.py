#Reads the text file and returns a list of each item on the line.
#assumes that the text file is structured in such a way where each item
#is on its own line.
def load_list_in_memory(filename):
    names_list = [];
    try:
        with open(filename, "r") as file:
            name = file.readline();
            while name:
                names_list.append(name.strip());
                name = file.readline();
        return names_list
    except FileNotFoundError:
        print(f"Could not open the {filename} file.")
        return names_list;

#helper function to get user input.
#same code from previous projects and assignments
def get_user_input(prompt, valid_type="string", error_msg="invalid input, please retype your response."):
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
                    print(error_msg);
        case "float":
            while True:
                try:
                    response = float(input(prompt));
                    return response;
                except ValueError:
                    print(error_msg);
        case _:
            print("feature not implemented");

def main():
    names_path = "./names.txt";
    #get user's name
    name = get_user_input("What is your first name?:");

    #load list of baby names:
    names = load_list_in_memory(names_path);

    if not names:
        print("Could not load names from file.");
        return;

    if name in names:
        print("Your name is present in the list of popular baby names.");
    else:
        print("Your name was not found in the list of popular baby names.");

if __name__ == "__main__":
    main();
