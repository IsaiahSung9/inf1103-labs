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


def generate_report(total_units, failed_attempts):
    # Print final report
    print("Total units processed: " + str(total_units))
    print("Number of failed/rejected entries: " + str(failed_attempts))



# Main program
inventory = 0
failed_entry = 0
deliveries = 0

while True:

    quantity = get_valid_input()

    # Quit program
    if quantity == "quit":
        break

    # Invalid input
    if quantity is None:
        failed_entry += 1
        continue

    # Process valid delivery
    inventory = process_delivery(inventory, quantity)

    # Calculate tax for this delivery
    tax = calculate_tax(quantity)
    print("Tax for this delivery: $" + str(tax))

    # Count successful delivery
    deliveries += 1

    # Check if inventory exceeds 500
    if inventory > 500:
        print("ALERT! U have exceeded 500 units. OVERSTOCK!")
        break


# Generate final report
generate_report(inventory, failed_entry)

print("Total Deliveries Processed: " + str(deliveries))