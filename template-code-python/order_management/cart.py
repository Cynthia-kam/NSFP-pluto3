from .product import Product
from .stock import Stock
from prettytable import PrettyTable
class Cart:
    """Represents a cart with a list of products and quantity

    Attributes:
        products: a dictionary with the key being the ID of the products, and the value being the quantity
        added
    """
    def __init__(self, stock: Stock) -> None:
        self.products = {}
        self.stock = stock

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
        product: Product = self.stock.getProductByID(productCode)
        if product:
            quantity_in_stock = product.quantity
            if quantity > quantity_in_stock:
                print("Sorry, we are out of stock")
            elif 0 < quantity <= quantity_in_stock:
                if productCode in self.products:
                    self.products[productCode] += quantity
                else:
                    self.products[productCode] = quantity
                print("Product added successfully")
            else:
                print("Enter valid quantity")
        else:
            print("Product does not exist")

    def __str__(self) -> str:
        """String representation of the cart
        """

        #TODO: Return a string representation of a cart that shows the products, their quantity, unit price, total price. And also the total price of the cart
        # Feel free to format it the way you want to
        headers = ["Product", "Quantity", "Unit Price", "Total Price"]
        rows = []

        for product in self.products:
            product_ = self.stock.getProductByID(product)
            rows.append([product_.name, self.products[product], product_.price, self.products[product] * product_.price])
        tab = PrettyTable(headers)
        tab.add_rows(rows)

        return f"===== Your Cart =====\n{tab.get_string()} \nTotal Cost: {self.cost}"


    def remove(self, code):
        """
        Removes a specific product from the cart """
        #TODO: Removes a product from the cart. safely fail if the product code is not found
        try:
           del self.products[code]
        except KeyError:
            pass

    def clear(self):
        """Clears up the cart.
        """
        self.products.clear()

    @property
    def cost(self):
        """Returns the total cost of the cart"""
        #TODO: implement the function
        total = 0
        for product in self.products:
            total += self.products[product] * self.stock.getProductByID(product).price
        return total

    