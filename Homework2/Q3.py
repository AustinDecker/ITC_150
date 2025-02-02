def get_number_input(message, error_message="invalid input, try again."):
    usr_input = "";

    while True:
        try:
            usr_input = float(input(message));
            return usr_input;
        except ValueError:
            print(error_message);

def calc_distance(speed, time): 
    return float(speed * time);

def map_distance(mph, hours_driven):
    print(f"{'Hour':<5} {'|':<1} {'Distance (miles)':<15}");
    print(f"{'-'*30}");
    count = 1;
    while count <= hours_driven:
        print(f"{count:<5} {'|':<1} {calc_distance(mph, count):<15}");
        count = count + 1;

def main():
    mph = get_number_input("what is the average speed of the vehicle in mph?: ");
    total_hours_driven = get_number_input("How long have you been driving the vehicle? (hours): ");
    map_distance(mph, total_hours_driven);
    return;

main();