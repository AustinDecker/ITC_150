def calc_distance(speed, time): 
    return float(speed * time)

def mpg(total_dist, fuel_consumed):
    return float(total_dist) / float(fuel_consumed)

def celcius_to_f(temp_c):
    f_conversion = float(9/5) * float(temp_c) + 32
    return f_conversion

def main():
    mph = 70

    print("===Testing distance functions===\n")
    print(f"mph: {mph} hrs driven: {6} total_distance: {calc_distance(mph, 6)}")
    print(f"mph: {mph} hrs driven: {10} total_distance: {calc_distance(mph, 10)}")
    print(f"mph: {mph} hrs driven: {15} total_distance: {calc_distance(mph, 15)}")

    print("===Testing MPG function===\n")
    distance_traveled = input("total distance travelled (miles): ")
    fuel_consumed = input("total fule consumed: ")
    print(f"total distance: {distance_traveled} fuel consumed: {fuel_consumed} MPG: {round(mpg(distance_traveled, fuel_consumed), 2)}")

    print("===Testing Temperature conversion function===")
    temp_c = input("temperature in Celcius:")
    print(f"temp in celcius: {temp_c} temp in Fahrenheit: {celcius_to_f(temp_c)}")

main()