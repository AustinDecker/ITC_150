
def calc_population_growth(init_pop_size, growth_rate, days_growing):
    new_pop_size = init_pop_size * (1 + growth_rate)**days_growing;
    return new_pop_size;

def map_population_growth(starting_population, avg_growth_rate, days_growing):
    print(f"{'Days':<5} {'|':<1} {'Population size':<15}");
    print(f"{'-'*20}");

    day = 0;
    while day <= days_growing:
        print(f"{day:<5} {'|':<1} {round(calc_population_growth(starting_population, avg_growth_rate, day)):<15}");
        day += 1;

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

def main():
    initial_pop = get_user_input("initial population size?: ", "int");
    growth_rate = get_user_input("what is the average growth rate of the population? (ex 2% = 0.02): ", "float");
    days_growing = get_user_input("total days population spent growing?: ", "float");

    print("Mapped Population Growth:")
    map_population_growth(initial_pop, growth_rate, days_growing)

main();