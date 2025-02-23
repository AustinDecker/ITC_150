def read_numbers_from_file(file_name):
    try:
        # Open the file for reading
        with open(file_name, 'r') as file:
            numbers = [float(line.strip()) for line in file.readlines()]
        
        # Return the list of numbers
        return numbers
    except FileNotFoundError:
        print(f"The file '{file_name}' does not exist.")
        return []

def calculate_sum_and_average(numbers):
    # Calculate sum and average
    total = sum(numbers)
    average = total / len(numbers) if numbers else 0
    return total, average

def main():
    # Specify the file name (you can adjust this as needed)
    file_name = 'Numbers.txt'  # Replace with the correct file name if different

    # Read numbers from the file
    numbers = read_numbers_from_file(file_name)
    
    if len(numbers) != 0:
        # Calculate the sum and average
        total, average = calculate_sum_and_average(numbers)
        
        # Print the results
        print(f"Sum: {round(total, 3)}")
        print(f"Average: {round(average, 3)}")
    else:
        pass

main()