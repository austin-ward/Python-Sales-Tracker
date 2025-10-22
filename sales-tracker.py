
class Customer:
    def __init__(self, name, phone, make, model):
        self.name = name
        self.phone = phone
        self.make = make
        self.model = model

    def display_info(self):
        return f"{self.name}, {self.phone}, {self.make} {self.model}"
    
    

def main():
    customers = []

    while True:
        print("Sales Tracker")
        print("1. Add new customer")
        print("2. Show all customers")
        print("3. Quit")

        choice = input("Enter menu option 1-3: ")

        if choice == "1":
            name = input("Enter customer name: ")
            phone = input("Enter customer phone number: ")
            make = input("Enter vehicle make: ")
            model = input("Enter vehicle model: ")
            # Creating Customer object instead of using the dictionary method
            customer = Customer(name, phone, make, model)

            customers.append(customer)
            print("Customer added successfully.")
        # This is accessing attributes from each Customer object
        elif choice == "2":
            if not customers:
                print("No sales yet.")
            else:
                print("Past sales")
                for i, customer in enumerate(customers, 1):
                    print(f"{i}. {customer.name}, {customer.phone}, {customer.make} {customer.model}")

        elif choice == "3":
            print("Bye")
            break
        else:
            print("Invalid option, please choose 1, 2, or 3 from the menu.")


if __name__ == "__main__":
    main()
