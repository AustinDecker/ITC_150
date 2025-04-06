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
        case "boolean":
            while True:
                response = str(input(prompt))
                if response.upper() == "YES" or response.upper() == "Y":
                    return True
                elif response.upper() == "NO" or response.upper() == "N":
                    return False
                else:
                    print("Invalid input, please retype your response.")
        case _:
            print("feature not implemented");

def create_query(query_object, response_list):
    for query in query_object["questions_list"]:

        response_type = query["response_type"]
        prompt = query["prompt"]
        validator = query.get("validator") 
        user_response = get_user_input(prompt + ": ", valid_type=response_type)

        if validator is not None:
            while not validator(user_response):
                user_response = get_user_input(prompt + ": ", valid_type=response_type)
        response_list.append(user_response)

class Person:
    def __init__(self, name="", address="", age=0, phone_number=""):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone_number = phone_number

    # Getters
    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age

    def get_phone_number(self):
        return self.__phone_number

    # Setters
    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_age(self, age):
        self.__age = age

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

class Customer(Person):
    def __init__(self, name="", address="", age=0, phone_number="", customer_number=0, mailing_list=False):
        super().__init__(name, address, age, phone_number)
        self.__customer_number = customer_number
        self.__mailing_list = mailing_list

    def __str__(self):
        return (
            f"Customer Info:\n"
            f"  Name: {self.get_name()}\n"
            f"  Address: {self.get_address()}\n"
            f"  Age: {self.get_age()}\n"
            f"  Phone: {self.get_phone_number()}\n"
            f"  Customer Number: {self.get_customer_number()}\n"
            f"  On Mailing List: {self.get_mailing_list()}"
        )

    # Getters
    def get_customer_number(self):
        return self.__customer_number

    def get_mailing_list(self):
        return self.__mailing_list

    # Setters
    def set_customer_number(self, customer_number):
        self.__customer_number = customer_number

    def set_mailing_list(self, mailing_list):
        self.__mailing_list = mailing_list


def main():
    
    query_object = {
        "questions_list": [
            {"prompt": "What is your name?", "response_type": "string"},
            {"prompt": "What is your address?", "response_type": "string"},
            {"prompt": "How old are you?", "response_type": "int"},
            {"prompt": "What is your phone number?", "response_type": "string"},
            {"prompt": "What is your customer number?", "response_type": "int"},
            {"prompt": "Would you like to be on the mailing list? (yes/no)", "response_type": "boolean"},
        ]
    }
    response_list = []
    create_query(query_object, response_list)

    customer = Customer(
        response_list[0], #name
        response_list[1], #address
        response_list[2], #age
        response_list[3], #phone number
        response_list[4], #customer number
        response_list[5]  #mailing list
    )

    print(f"Created Customer:\n\n\t{customer}")

if __name__ == "__main__":
    main();