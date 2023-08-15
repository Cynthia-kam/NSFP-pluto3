from . import Stock, Cart, User, UserManagement, BookRecords, Wrapper, Prescription
import json
MSG_WRONG_INPUT = "Wrong input. Try again!"
class Menu:
   
    def __init__(self, stock: Stock, profiles: UserManagement, pharmacist: User, records_file: str, prescriptions_file: str, stock_file: str) -> None:
        self.stock = stock
        self.profiles = profiles
        self.pharmacist = pharmacist
        self.cart = Cart(stock = stock)
        # use the file instead of the object so that we can keep track
        self.records_file = records_file
        self.prescriptions_file = prescriptions_file
        self.stock_file = stock_file

    def show_main_menu(self):
        try:
            print("Main Menu:")
            print("1. Order management")
            print("2. Analytics")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.order_management_menu()
            elif choice == "2":
                self.analytics_menu()
        except ValueError:
                print(MSG_WRONG_INPUT)
    
    def order_management_menu(self):
        try:
            print("Order Management:")
            print("1. Adding to cart")
            print("2. Remove from cart")
            print("3. Clear the cart")
            print("4. Checkout")
            print("5. Go back to main menu")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_to_cart()
            elif choice == "2":
                self.remove_from_cart()
            elif choice == "3":
                self.clear_cart()
            elif choice == "4":
                self.checkout()
            elif choice == "5":
                return
        except ValueError:
                print(MSG_WRONG_INPUT)

    def analytics_menu(self):
        try:
            print("Analytics:")
            print("1. Total income from purchases")
            print("2. Prescription statistics")
            print("3. Purchases for a user")
            print("4. Sales by an agent")
            print("5. Top sales")
            print("6. Go back to main menu")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.total_income()
            elif choice == "2":
                self.prescription_statistics()
            elif choice == "3":
                self.purchases_for_user()
            elif choice == "4":
                self.sales_by_agent()
            elif choice == "5":
                self.top_sales()
            elif choice == "6":
                return
        except ValueError:
                print(MSG_WRONG_INPUT)

    
    def add_to_cart(self):
        # Implement adding items to the cart
        pass

    def remove_from_cart(self):
        # Implement removing items from the cart
        pass

    def clear_cart(self):
        # Implement clearing the cart
        pass

    def checkout(self):
        # Implement the checkout process
        pass

    def total_income(self):
        # Implement calculating total income from purchases
        pass

    def prescription_statistics(self):
        # Implement prescription statistics
        pass

    def purchases_for_user(self):
        # Implement showing purchases for a specific user
        pass

    def sales_by_agent(self):
        # Implement showing sales by a specific agent
        pass

    def top_sales(self):
        # Implement showing top sales
        pass


# profiles = UserManagement()  # Initialize UserManagement object
# pharmacist = User()  # Initialize pharmacist User object
# menu = Menu( profiles, pharmacist, "records.txt", "prescriptions.txt", "stock.txt")
# menu.show_main_menu()