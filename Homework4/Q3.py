
class Course:
    def __init__(self, course_num, room_num, instructor, textbook_title):
        self.course_num = course_num;
        self.room_num = room_num;
        self.instructor = instructor;
        self.textbook_title = textbook_title;

    def __str__(self):
        return f"Course num: {self.course_num} Room num: {self.room_num} Instructor: {self.instructor} Textbook title: {self.textbook_title}";

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

def create_menue(options):
    print(f"Options:");
    for index, option in enumerate(options):
        print(f"\t{index + 1}: {option}");

    usr_input = get_user_input("choice: ", valid_type="int");
    
    return usr_input - 1 #converting the option back to 0 based indexing

def main():
    # static info
    #course lookup table
    course_map = {
        "ECET114": Course("ECET114", "ET241", "Otto", "Starting out with Python"),
        "CPET101": Course("CPET101", "ET305", "Dr. Alasti", "Introductory Circuit Analysis"),
        "ITC145": Course("ITC145", "ET115", "Steffen", "Digital Electronics: A Practical Approach with VHDL"),
        "MET335": Course("MET335", "ET124", "Jason Moyer", "N/A")
    };

    def print_course_info():
        print("===Individual Course Lookup===");
        course_number = get_user_input("What is the course number for the course you are trying to look up?: ");

        if course_number in course_map:
            print(course_map[course_number]) 
        else:
            print(f"A course was not found with the course number: {course_number}. The course number is case sensitive.")
    
    def print_all_course_info():
       print("===Course List===")
       for key in course_map.keys():
           print(course_map[key]);

    running = True;
    while running:
        print("===Course Lookup Registery===");
        user_option = create_menue(["look-up course", "view all courses", "exit program"]);

        match user_option:
            case 0:
                print_course_info();
            case 1:
                print_all_course_info();
            case 2:
                running = False;
            case _:
                print("Not a valid option.")


if __name__ == "__main__":
    main()