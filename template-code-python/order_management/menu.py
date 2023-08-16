from . import Stock, Cart, User, UserManagement, BookRecords, Wrapper, Prescription

MSG_WRONG_INPUT = "Wrong input. Try again!"
class Menu:
    """Represents the menu class for the project

    Attributes: 
        stock: stock variable
        profiles: user management module
        pharmacist: account of the salesperson
        records_file: path to the file containing the sales
        prescriptions_file: path to the file containing the prescriptions.
        stock_file: path to the file containing the stock data
    """
    def __init__(self, stock: Stock, profiles: UserManagement, pharmacist: User, records_file: str, prescriptions_file: str, stock_file: str) -> None:
        self.stock = stock
        self.profiles = profiles
        self.pharmacist = pharmacist
        self.cart = Cart(stock=stock)
        # use the file instead of the object so that we can keep track
        self.records_file = records_file
        self.prescriptions_file = prescriptions_file
        self.stock_file = stock_file
        self.books = BookRecords.load(records_file)

    #TODO: Create all the necessary functions/method to create and manage the menu using the
    # available variables and all the attributes of the class

    # Make sure to dump the prescriptions, stock, and sale data after every sale.

    # Your menu should have two main options with suboptions. Such as
    """
    1. Order management
        1.1. Adding to a cart (you need to show the list of products and ask the user to select one with ID. Bonus: Can you display with numbers and ask user to choose a number instead?
                Also ask for quantity.)
        1.2. Remove from a cart (display the cart and ask the user to select the element to remove. Remove by ID or by index (bonus))
        1.3. Clear the cart (self explanatory)
        1.4. Checkout (displays the cart with the total and ask for a prescription element. Proceed to checkout and show a message is successful or not).
    2. Analytics
        2.1. Total income from purchases
        2.2. Prescription statistics
        2.3. Purchases for a user
        2.4. Sales by an agent
        2.5. Top sales

    * For each of the menu items, when necessary, display a success or error message to guide the user.
    """

    def show_main_menu(self):
        print("===== Main Menu =====")
        print("1. Order management")
        print("2. Analytics")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            self.order_management_menu()
        elif choice == "2":
            self.analytics_menu()
        elif choice == "3":
            return 'q'
        else:
            print(MSG_WRONG_INPUT)


    def order_management_menu(self):
        print("===== Order Management =====")
        print("1. Add to cart")
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
        else:
            print(MSG_WRONG_INPUT)
        self.order_management_menu()

    def analytics_menu(self):
        print("\n===== Analytics =====")
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
        else:
            print(MSG_WRONG_INPUT)
        self.analytics_menu()

    def add_to_cart(self):
        # Implement adding items to the cart
        try:
            product_id = input("Enter product ID: ")
            quantity = int(input("Enter quantity: "))
            self.cart.add(productCode=product_id, quantity=quantity)
        except ValueError:
            print(MSG_WRONG_INPUT)
            self.add_to_cart()

    def remove_from_cart(self):
        # Implement removing items from the cart
        self.cart.remove(input("Enter product ID: "))

    def clear_cart(self):
        # Implement clearing the cart
        self.cart.clear()

    def checkout(self):
        # cart: Cart, customerID: str, prescription: Prescription = None
        wrap = Wrapper(self.stock, self.pharmacist.username)
        customer_id = input("Enter customer ID: ")
        print("\nEnter 1 to enter prescription ID or any key to continue without prescription: ")
        choice = input("Enter your choice: ")
        try:
            prescription: Prescription = None
            if choice == '1':
                prescription_id = input("Enter Prescription ID: ")
                prescription_dict = Prescription.get(self.prescriptions_file, prescription_id)
                prescription = Prescription(DoctorName=prescription_dict['DoctorName'],
                                            PrescriptionID=prescription_dict['PrescriptionID'],
                                            Medications=prescription_dict['Medications'],
                                            CustomerID=prescription_dict['CustomerID']
                                            )
            wrap.checkout(cart=self.cart, customerID=customer_id, prescription=prescription)
            wrap.dump(self.records_file)
        except Exception as e:
            print(e)

    def total_income(self):
        total = self.books.totalTransactions()
        print(f"Total income: {total}")

    def prescription_statistics(self):
        print(self.books.reportOnPrescriptions())

    def purchases_for_user(self):
        print(self.books.purchasesByUser(input("Enter Username: ")))

    def sales_by_agent(self):
        print(self.books.purchasesByUser(self.pharmacist.username))

    def top_sales(self):
        print(self.books.topNSales())