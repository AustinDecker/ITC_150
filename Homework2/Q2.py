# helper function that strictly looks for number input.
def get_number_input(message, error_message="invalid input, try again."):
    usr_input = "";

    while True:
        try:
            usr_input = float(input(message));
            return usr_input;
        except ValueError:
            print(error_message);

def calc_discount(quantity_sold, item_cost):
    discounts = [.10, .20, .30, .40];
    discount = 0.0;

    if quantity_sold >= 100:
        discount = discounts[3];
    elif quantity_sold >= 50:
        discount = discounts[2];
    elif quantity_sold >= 20:
        discount = discounts[1];
    elif quantity_sold >= 10:
        discount = discounts[0];

    total_cost = round(quantity_sold * item_cost, 2);
    discount_amount = round(total_cost * discount, 2);
    discounted_cost = round(total_cost - discount_amount, 2);

    discount_results = {
        "discount": discount,
        "discounted_cost": discounted_cost,
        "saved": discount_amount
    };

    return discount_results

    

def main():
    num_products = get_number_input("what was the total number of products sold?: ");
    product_cost = get_number_input("what is the cost per product?: ");

    discount_results = calc_discount(num_products, product_cost);
    print(f"Discounted cost of {num_products} items with a product cost of ${product_cost} is ${discount_results['discounted_cost']}.");
    print(f"Saved ${discount_results['saved']} with a {discount_results['discount'] * 100}% discount.")

main();