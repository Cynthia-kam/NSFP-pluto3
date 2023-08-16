import json
from typing import List
from .product import Product
from prettytable import PrettyTable

class Stock:
    """Represents the catalog of products
    
    Attributes:
        products: the list of products
    """

    def __init__(self, products: List[Product]) -> None:
        self.products = products

    def update(self, id: int, change: int):
        """Update the quantity of a product by adding or removing
        
        Args:
            id: identifier of the product
            change: the value by which the quantity should be update (+1 adds 1, -2 removes 2 for example)
        """
        # TODO: Make sure the product exists, and that by making the change, the value is still >= 0

        # TODO: Update the quantity
        product = self.getProductByID(id)
        if product:
            if product.quantity + change < 0:
                print("Sorry, you can only have a maximum of", product.quantity)
            else:
                product.quantity += change
        else:
            print("Product does not exist")

    def getProductByID(self, id: int) -> Product:
        """Gets a product by its ID

        Args:
            id: identifier of the product
        
        Returns: the product's object
        """
        products = self.products
        for product in products:
            if product.code == id:
                return product

    def dump(self, outfile: str):
        """Saves the stock to a JSON file"""
        # TODO: Implement the function
        with open(outfile, 'w') as f:
            json.dump([json.loads(product.to_json()) for product in self.products], f)

    @staticmethod
    def load(infile: str):
        """Loads the stock from an existing file
        
        Args: 
            infile: input file to the function
        """
        with open(infile, 'r') as f:
            file_data = json.load(f)
            products: List[Product] = []
            for item in file_data:
                product = Product(
                    item['code'],
                    item['name'],
                    item['brand'],
                    item['description'],
                    item['quantity'],
                    item['price'],
                    item['dosage_instruction'],
                    item['requires_prescription'],
                    item['category']
                )

                products.append(product)
            return Stock(products)

    def __str__(self) -> str:
        """Returns a string representation of the stock
        """
        # TODO: Return the description of the stock with a nice output showing the ID, Name, Brand, Description, Quantity, Price, and the requires_prescription field

        headers = ["ID","Name","Brand","Description","Quantity","Price","Requires Prescription"]
        rows = []
        for product in self.products:
            rows.append([product.code,product.name,product.brand,product.description,product.quantity,product.price,product.requires_prescription])

        table = PrettyTable(headers)
        table.add_rows(rows)
        return f"===== Items In Stock ===== \n{table.get_string()} \nTotal Number Of Items In Stock: {len(self.products)}"
