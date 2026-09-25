def load_inventory():
    # Try to load previous inventory information
    try:
        file = open("inventory.txt", "r")

        # Read saved total inventory
        inventory = int(file.readline().strip())

        # Read saved transaction history
        history_line = file.readline().strip()

        if history_line == "":
            history = []
        else:
            history = history_line.split(",")

            # Convert each transaction back to integer
            history = [int(value) for value in history]

        file.close()

        return inventory, history

    # If inventory.txt does not exist, start fresh
    except FileNotFoundError:
        return 0, []
