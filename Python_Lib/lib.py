import math

def transpose_matrix(array_2d: list[list[int]]):

    if len(array_2d) == 0:
        return [[0]]
    
    row_size = len(array_2d)
    col_size = len(array_2d[0])

    transposed_matrix = [[0] * row_size for _ in range(col_size)]

    for row in range(row_size):
        for col in range(col_size):
            transposed_matrix[col][row] = array_2d[row][col]

    return transposed_matrix

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

def create_menue(options):
    print(f"\nOptions:");
    for index, option in enumerate(options):
        print(f"\t{index + 1}: {option}");

    usr_input = get_user_input("choice: ", valid_type="int");
    
    return usr_input - 1 #converting the option back to 0 based indexing

def get_column(array_2d, col_index):
    col_items = [];

    for row in array_2d:
        col_items.append(row[col_index])
    return col_items

def create_table(headers, rows):
    header_widths = list(map(lambda x: len(x), headers));
    max_column_widths = []

    # determine the max column width for the values.
    for col in range(len(headers)):
        col_nums = get_column(rows, col);
        max_widths = list(map(lambda x: len(str(x)), col_nums))
        max_column_widths.append(max(max_widths[col], header_widths[col]))

    # Create the format string for each row (with dynamic column width)
    row_format = " | ".join([f"{{:<{width}}}" for width in max_column_widths])

    # Print the headers
    print(row_format.format(*headers))
    sep_length = sum(max_column_widths) + len(max_column_widths) * 3 - 1
    print("-" * int(sep_length))  # Print separator

    # Print the rows
    for row in rows:
        print(row_format.format(*[str(value) for value in row]))


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
    for response_type, prompt in query_object["questions_list"]:
        user_response = get_user_input(prompt + ": ", valid_type=response_type)
        response_list.append(user_response)
def test():
    def test_1():
        print("Test 1")
        matrix = [[5, 7, 8], [2, 6, 1], [3, 9, 0]]
        print(transpose_matrix(matrix))

    def test_2():
        print("Test 2")
        matrix = [[5, 7, 8, 0], [2, 6, 1, 7], [3, 9, 0, 5]]
        print(transpose_matrix(matrix))

    def test_3():
        print("Test 3")
        matrix = [[1, 2], [3, 4], [5, 6]]
        print(transpose_matrix(matrix))

    def test_4():
        print("Test 4")
        matrix = [[1]]
        print(transpose_matrix(matrix))

    def test_5():
        print("Test 5")
        matrix = [[1, 2, 3]]
        print(transpose_matrix(matrix))

    def test_6():
        print("Test 6")
        matrix = []
        print(transpose_matrix(matrix))

    test_1()
    test_2()
    test_3()
    test_4()
    test_5()
    test_6()

test()