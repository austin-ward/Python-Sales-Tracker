
class Customer:
    def __init__(self, name, phone, make, model):
        self.name = name
        self.phone = phone
        self.make = make
        self.model = model

    def display_info(self):
        return f"{self.name}, {self.phone}, {self.make} {self.model}"
    

# subclass for customers who paid in cash
class CashCustomer(Customer):
    def display_info(self):
        return super().display_info() + " (Paid in Cash)"
    
# subclass for customers who financed their vehicle
class FinanceCustomer(Customer):
    def display_info(self):
        return super().display_info() + " (Financed Vehicle)"
    


def main():
    customers = []

    while True:
        print("Sales Tracker")
        print("1. Add new customer")
        print("2. Add cash customer")
        print("3. Add finance customer")
        print("4. Show all customers")
        print("5. Quit")

        choice = input("Enter menu option 1-5: ")

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
            name = input("Enter customer name: ")
            phone = input("Enter customer phone number: ")
            make = input("Enter vehicle make: ")
            model = input("Enter vehicle model: ")
            cash_customer = CashCustomer(name, phone, make, model)
            customers.append(cash_customer)
            print("Cash customer added successfully.")


        elif choice == "3":
            name = input("Enter customer name: ")
            phone = input("Enter customer phone number: ")
            make = input("Enter vehicle make: ")
            model = input("Enter vehicle model: ")
            customer = FinanceCustomer(name, phone, make, model)
            customers.append(customer)
            print("Finance customer added successfully.")

        elif choice == "4":
            if not customers:
                print("No recent sales to display.")
            else:
                print("Recent Sales:")
                for idx, customer in enumerate(customers, start=1):
                    print(f"{idx}. {customer.display_info()}")

        elif choice == "5":
            print("Closing Sales Tracker.")
            break

        else:
            print("Invalid option. Please enter a number between 1 and 5.")
            
if __name__ == "__main__":
    main()
