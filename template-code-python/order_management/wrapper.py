from .cart import Cart
from .stock import Stock
from .product import Product
from .prescription import Prescription
from time import time

import json
sales_file = "../data/sales.json"
## would need to create a new object for each new order
class Wrapper:
    """
    Main class used to manage orders and carts.

    Attributes:
        sales: A list of the sales done during the program's execution
        stock: The stock used in the execution
        agentID: the username of the pharmacist running the program
    """
    def __init__(self, stock: Stock, agentID: str) -> None:
        self.sales = []
        self.stock = stock
        self.agentID = agentID

    def checkout(self, cart: Cart, customerID: str, prescription: Prescription = None):
        """Handles the checkout procedure of the program.
        
        Args:
            cart: The cart to pay for
            prescription: the prescription that accompanies the order (default: None)
        """

        #TODO: First check that all the product that require a prescription have all the criteria met
        # (i.e., (1) there is a prescription that (2) matches the customer's ID, and (3) contains the medication
        # in the specified quantity).
        # Raise an exception if either of those conditions is unmet.

        for product_id in cart.products:
            product = cart.stock.getProductByID(product_id)
            if product.requires_prescription:
                if not prescription or not prescription.medecineInPrescription(product, cart.products[product_id]) or customerID != prescription.CustomerID:
                    raise Exception("Invalid prescription")
            sale = {
                "name": product.name,
                "quantity": cart.products[product_id],
                "price": product.price,
                "purchase_price": product.price * cart.products[product_id],
                "timestamp": time(),
                "customerID": customerID,
                "salesperson": self.agentID
            }
            self.sales.append(sale)
            prescription.markComplete(product)




        #TODO: Get the current datetime and save a Sale information for each product sold with the following schema
        # {"name": "<name>", "quantity": <quantity>, "price": <unit price>, "purchase_price": <total price>, "timestamp": <timestamp>,
        # "customerID": <customer username>, "salesperson": <pharmacist username>}

        #TODO: Append the list to the current sales

        #TODO: Make sure that the sold products are marked as complete in the prescriptions.


    def dump(self, outfile: str):
        """Dumps the current sales data to a file

        Args:
            outfile: the path to the output file
        """
        #TODO: Load the content, if any of the existing file

        #TODO: Update the content by appending the new entries to it, and save to the file

        with open(sales_file, 'r') as f:
            file_data = json.load(f)
            for item in self.sales:
                file_data.append(item)

        with open(outfile, 'w') as f:
            json.dump(file_data, f)
