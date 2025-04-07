class BookManager:
    book_map = {}
    
    @classmethod
    def load_book_database(cls, filepath):
        pass

    @classmethod
    def save_book_database(cls, filepath):
        pass

    @classmethod
    def is_in_database(cls, book_title):
        return book_title in cls.book_map 

    @classmethod
    def get_book(cls, book_title):
        return cls.book_map.get(book_title)

    @classmethod
    def remove_book(cls, book_title):
        if cls.is_in_database(book_title):
            cls.book_map.pop(book_title, None)
            return True
        else:
            return False;

    @classmethod
    def add_book(cls, book):
        if not cls.is_in_database(book.get_title()):
            cls.book_map[book.get_title()] = book
            return True
        else:
            return False;
    
    @classmethod
    def set_book_price(cls, book_title, new_price):
        if new_price <= 0:
            return False

        if not cls.is_in_database(book_title):
            return False

        book = cls.get_book(book_title)
        book.set_price(new_price)
        return True

    @classmethod
    def set_book_qty(cls, book_title, new_qty):
        if new_qty < 0:
            return False

        if not cls.is_in_database(book_title):
            return False

        book = cls.get_book(book_title)
        book.set_quantity(new_qty)
        return True

    @classmethod
    def print_book_database(cls):
        print("\n===Book Inventory===")
        for key in cls.book_map.keys():
            print(cls.book_map[key]);




class Book:
    def __init__(self, title, author, price, quantity):
        self._title = title
        self._author = author
        self._price = price
        self._quantity = quantity

    def __str__(self):
        return f"Title: {self._title}\tAuthor: {self._author}\tPrice: ${self._price}\tQty: {self._quantity}";

    def set_title(self, title):
        self._title = title
    
    def set_author(self, author):
        self._author = author

    def set_price(self, price):
        self._price = price
    
    def set_quantity(self, qty):
        self._quantity = qty

    def get_title(self):
        return self._title
    
    def get_author(self):
        return self._author

    def get_price(self):
        return self._price
    
    def get_quantity(self):
        return self._quantity 

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

def create_menue(options):
    print(f"\nOptions:");
    for index, option in enumerate(options):
        print(f"\t{index + 1}: {option}");

    usr_input = get_user_input("choice: ", valid_type="int");
    
    return usr_input - 1 #converting the option back to 0 based indexing

def display_book_inventory():
    BookManager.print_book_database()

def add_book_to_inventory():

    def book_validator(book_title):
        result = BookManager.is_in_database(book_title)
        if result:
            print("Book Title already exists inside the database, try again.")
            return False
        return True
            
    def price_validator(price):
        if price > 0:
            return True;
        else:
            print("Price cannot be less than or equal to 0")
            return False;

    def qty_validator(price):
        if price > 0:
            return True;
        else:
            print("qty cannot be less than 0")
            return False;

    display_book_inventory();
    print("\n===Add Book===")
    query_object = {"questions_list": [{"prompt": "Book Title", "response_type": "string", "validator": book_validator},
                                   {"prompt": "Book Author", "response_type": "string"},
                                   {"prompt": "Book Price", "response_type": "float", "validator": price_validator},
                                   {"prompt": "Book Quantity", "response_type": "int", "validator": qty_validator}]}
    response_list = []
    create_query(query_object, response_list);
    
    newBook = Book(response_list[0], response_list[1], response_list[2], response_list[3])
    result = BookManager.add_book(newBook)

    if result:
        print(f"{newBook}\nhas been added to the database.")
    else:
        print("Book already exists.")
        
def del_book_from_inventory():
    display_book_inventory()
    print("\n===Delete Book===")
    book_title = get_user_input("Book Title: ", valid_type="string");
    removed_book = BookManager.get_book(book_title)
    result = BookManager.remove_book(book_title)

    if result:
        print(f"Successfully removed Book from the database.\n{removed_book}")
    else:
        print(f"Could not remove book from database. Title {book_title} does not match any book titles.")

def change_book_quantity():
    def book_validator(book_title):
        if BookManager.is_in_database(book_title):
            return True
        else:
            print("Book Title was not found in the database, try again.")
            return False;

    display_book_inventory()
    print("\n===Modify Book: Quantity===")
    query_obj = {"questions_list":[{"prompt": "Book Title", "response_type": "string", "validator": book_validator},
                               {"prompt": "New Quantity", "response_type": "int", "validator": lambda x: x >= 0}]}
    response = []

    create_query(query_obj, response)
    result = BookManager.set_book_qty(response[0], response[1])
    book = BookManager.get_book(response[0])

    if result:
        print(f"updated book:\n{book}")

def change_book_price():
    def book_validator(book_title):
        if BookManager.is_in_database(book_title):
            return True
        else:
            print("Book Title was not found in the database, try again.")
            return False;
    display_book_inventory()
    print("\n===Modify Book: Price===")
    query_obj = {"questions_list":[{"prompt": "Book Title", "response_type": "string", "validator": book_validator},
                               {"prompt": "New Price", "response_type": "float", "validator": lambda x: x > 0}]}
    response = []

    create_query(query_obj, response)
    result = BookManager.set_book_price(response[0], response[1])
    book = BookManager.get_book(response[0])

    if result:
        print(f"updated book:\n{book}")

def main():
    running = True;
    while running:
        print("\n===Bookstore Inventory Management System===");
        user_option = create_menue(["Display Current Inventory", 
                                    "Add Book To Inventory", 
                                    "Delete Book From Inventory", 
                                    "Change Quantity of Book", 
                                    "Change Price of Book", 
                                    "Exit Program"]);

        match user_option:
            case 0:
                display_book_inventory()
            case 1:
                add_book_to_inventory()
            case 2:
                del_book_from_inventory()
            case 3:
                change_book_quantity()
            case 4:
                change_book_price()
            case 5: 
                running = False
            case _:
                print("Not a valid option.")


if __name__ == "__main__":
    main()