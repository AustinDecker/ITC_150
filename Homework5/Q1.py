# below functions are util functions
# ended up making them in between assignments to make my life easier

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

class Pet():
    def __init__(self, name, animal_type, age):
       self.__name = name
       self.__type = animal_type
       self.__age = age

    def __str__(self):
        return f"Animal Type: {self.__type}\nAge: {self.__age} years\nPet Name: {self.__name}"
    
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_animal_type(self):
        return self.__type

    def set_animal_type(self, animal_type):
        self.__type = animal_type

    # Getter for age
    def get_age(self):
        return self.__age

    # Setter for age
    def set_age(self, age):
        self.__age = age

def main():
    query_object = {
        "questions_list": [
            {
                "prompt": "What type of animal is your pet?",
                "response_type": "string"
            },
            {
                "prompt": "How old is your pet?",
                "response_type": "int"
            },
            {
                "prompt": "What is the Name of your pet?",
                "response_type": "string"
            }
        ]
    }
    response_list = []
    create_query(query_object, response_list);
    pet = Pet(response_list[2], response_list[0], response_list[1])
    print(f"Your new pet:\n{pet}")

if __name__ == "__main__":
    main();