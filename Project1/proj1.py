def calc_compound_interest(initial_amount, annual_interest_rate, n_times_yearly_compound, years):
    amount = float(initial_amount) * (1 + float(annual_interest_rate/n_times_yearly_compound)) ** (n_times_yearly_compound * years)
    return amount


def get_user_input(prompt, answer_obj, valid_type="string"):
    valid_input = False
    match valid_type:
        case "string":
            response = str(input(prompt))
            answer_obj["response"] = response
            valid_input = True

        case "number":

            while not valid_input:
                try:
                    response = float(input(prompt))
                    answer_obj["response"] = response
                    valid_input = True
                except ValueError:
                    print("invalid input, please retype your response.")
        case _:
            print("feature not implemented")


   
p = float(input("initial balance: "))
r = float(input("annual interest rate (ex 5% = 0.05): "))
n = int(input("number of times compounded yearly: "))
t = int(input("total years: "))

print(f"New Balance: ${calc_compound_interest(p, r, n, t):,.2f}")
