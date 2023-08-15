from .product import Product
from .stock import Stock
import json
class Cart:
    """Represents a cart with a list of products and quantity

    Attributes:
        products: a dictionary with the key being the ID of the products, and the value being the quantity
        added
    """
    def __init__(self, stock: Stock) -> None:
        self.products = {}
        self.stock = stock
    def dump(self, outfile: str):
        """Saves the cart to a JSON file"""
        try:
            with open(outfile, 'w') as f:
                json.dump(self.products, f)
            print("Product added to cart saved successfully.")
        except IOError:
            print("Error adding product to cart file.")

    def add(self, productCode: str, quantity: int):
        """Adds a product to the cart with the specified quantity
        
        Args:
            productCode: the identifier of the product
            quantity: quantity to add

        Returns: None
        """
        #TODO: Make sure the quantity is valid (> 0 and <= to the quantity in the stock)
        #TODO: If the product was already in the cart, increment the quantity
        
        #TODO: After the checks, add the product to the dictionary

        if quantity<=0:
            print("quantity can't be less than 0")
            return
        if productCode in self.products:
            self.products[productCode]+=quantity
        else:
            self.products[productCode]=quantity
        


    def __str__(self) -> str:
        """String representation of the cart
        """
        #TODO: Return a string representation of a cart that shows the products, their quantity, unit price, total price. And also the total price of the cart
        # Feel free to format it the way you want to
        return NotImplemented

    def remove(self, code):
        """
        Removes a specific product from the cart """
        #TODO: Removes a product from the cart. safely fail if the product code is not found

    def clear(self):
        """Clears up the cart.
        """

    @property
    def cost(self):
        """Returns the total cost of the cart"""
        #TODO: implement the function

    