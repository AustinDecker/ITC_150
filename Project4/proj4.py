import json

class Contact:
    def __init__(self, name, phone_num, email):
        self.name = name;
        self.phone_num = phone_num;
        self.email = email;

    def __str__(self):
        return f"Name: {self.name} Email: {self.email} phone number: {self.phone_num}";

    def save_to_json(self, filepath):
        contact_dict = {
            "name": self.name,
            "phone_num": self.phone_num,
            "email": self.email
        }
        with open(filepath, "a") as file:
            json.dump(contact_dict, file, indent=4);
            file.write(",\n")



def create_menue(options):
    print(f"\nOptions:");
    for index, option in enumerate(options):
        print(f"\t{index + 1}: {option}");

    usr_input = get_user_input("choice: ", valid_type="int");
    
    return usr_input - 1 #converting the option back to 0 based indexing

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
    # static info
    #contact lookup table
    contact_map = {};

    def print_contact_info():
        print("\n===Individual Contact Lookup===");
        contact_email = get_user_input("What is the email of the contact you wish to look up?: ");

        if contact_email in contact_map:
            print(contact_map[contact_email]) 
        else:
            print(f"A contact was not found with the email: {contact_email}. The email is case sensitive.")
    
    def print_all_contact_info():
       print("\n===Contacts List===")
       for key in contact_map.keys():
           print(contact_map[key]);

    def add_contact():
        user_input = "";
        tokens = [];
        name = "";
        email = "";
        phone_number = "";

        while True:
            user_input = get_user_input("Please enter the contact information in the format: [first_name] [last_name] [email] [phone_number]: ").strip();
            tokens = user_input.split(" ");

            if len(tokens) != 4:
                print("Invalid input. Please provide name, email, and phone number.")
                return
            
            name = tokens[0] + " " + tokens[1];
            email = tokens[2];
            phone_number = tokens[3];

            validate = get_user_input(f"The following contact with the information: name: {name} email: {email} phone_number: {phone_number} will be added to the contacts list. Is this information correct? y/n: ") 

            if validate == "y":
                break;
        
        if email in contact_map:
            print("a contact is already associated with that email.");
            return;
        contact_map[email] = Contact(name, phone_number, email);
        print(f"a new contact: {contact_map[email]} has been added to the contacts list.");
    
    def remove_contact():
        email = "";
        while True:
            email = get_user_input("What is the email of the contact you wish to remove from the contacts list?: ");
            if email.strip() not in contact_map:
                print(f"a contact with the email {email} was not found in the contacts list");
                return;
        
            validate_input = get_user_input(f"The contact you wish to remove is: {contact_map[email]}, correct? y/n: ");
            if validate_input == "y":
                break;
        
        deleted_contact = contact_map[email];
        del contact_map[email];
        print(f"The contact {deleted_contact} has been removed from the contacts list.")

    def save_contacts():
        for contact_key in contact_map:
            contact_map[contact_key].save_to_json("contacts_list.json");
        print("Contacts have been saved.");

    running = True;
    while running:
        print("\n===Contact Registery===");
        user_option = create_menue(["look-up contact", "view all contacts", "add new contact", "remove existing contact", "save contacts", "exit program"]);

        match user_option:
            case 0:
                print_contact_info();
            case 1:
                print_all_contact_info();
            case 2:
                add_contact();
            case 3:
                remove_contact();
            case 4:
                save_contacts();
            case 5: 
                running = False;
            case _:
                print("Not a valid option.")


if __name__ == "__main__":
    main()