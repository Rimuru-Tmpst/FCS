#Exercise 3: POS for aamo el dekanje


inventory = {
    "123": {"name": "Milk", "price": 2.5},
    "124": {"name": "Bread", "price": 1.0},
    "125": {"name": "Eggs", "price": 0.2},
    "126": {"name": "Butter", "price": 3.0},
}

def pos_system():
    while True:
        start_receipt = input("Start a new receipt? (yes/no): ").strip().lower()
        if start_receipt == "no":
            print("Exiting POS system. Goodbye!")
            break
        elif start_receipt == "yes":
            receipt = []
            total_amount = 0
            while True:
                barcode = input("Enter item barcode: ")
                if barcode not in inventory:
                    print("Item not found. Please try again.")
                    continue

                quantity = int(input("Enter quantity: "))
                item = inventory[barcode]
                total_cost = item["price"] * quantity
                receipt.append(f"{item['name']} - {quantity} x ${item['price']} = ${total_cost:.2f}")
                total_amount += total_cost

                another_item = input("Add another item? (yes/no): ").strip().lower()
                if another_item == "no":
                    print("\n--- Receipt ---")
                    for line in receipt:
                        print(line)
                    print(f"Total Amount: ${total_amount:.2f}\n")
                    break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

pos_system()
