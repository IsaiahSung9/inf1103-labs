def get_valid_input():
    # Ask user for quantity
    quantity = input("Enter a stock quantity or type (quit) to leave: ")

    # Check for quit
    if quantity.lower() == "quit":
        return "quit"

    # Check if input is an integer
    if not quantity.isdigit():
        print("ERROR! Please key in an integer")
        return None

    # Convert quantity to integer
    return int(quantity)

def process_delivery(current_total, new_value):
    # Add delivery to current inventory
    new_total = current_total + new_value
    return new_total


def calculate_tax(amount):
    # Calculate 10% tax for this delivery
    tax = amount * 0.10
    return tax