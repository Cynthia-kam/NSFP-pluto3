from __future__ import annotations

import json
from datetime import datetime

from typing import List
from .sale import Sale
from datetime import datetime
from prettytable import PrettyTable


class BookRecords:
    """A record of all the sales made through the application.
    
    Attributes:
        transactions: a list of the transactions
    """

    def __init__(self, transactions: List[Sale]) -> None:
        self.transactions = transactions

    def __str__(self) -> str:
        """Returns a string representation of a record.
        
        Args:
        
        Returns: A string
        """
        headers = ["ID", "Date", "Customer", "Medication", "Quantity", "Purchase Price (RWF)", "Prescription"]
        rows = []
        table = PrettyTable(headers)
        for i in range(len(self.transactions)):
            rows.append([i + 1, datetime.fromtimestamp(self.transactions[i].timestamp), self.transactions[i].customerID,
                         self.transactions[i].name, self.transactions[i].quantity, self.transactions[i].purchase_price,
                         self.transactions[i].prescriptionID])
        table.add_rows(rows)
        return table.get_string()

        # TODO: In the format below, return a representation of the records
        # |      # | Date                | Customer   | Medication | Quantity | Purchase Price | Prescription |
        # |      1 | 2023-06-03 21:23:25 | doe        | Quinine    |        3 |       1400 RWF | PHA1         |

    def reportOnPrescriptions(self) -> str:
        """Reports on prescription sales.

        Args: 

        Returns: A string report of the prescriptions processed
        """
        # TODO: From the transactions data, retrieve for each prescription, the actual medications that were processed
        # and aggregate for each, the corresponding total price.
        header = ["Prescription ID", "Total Price"]
        rows = []
        table = PrettyTable(header)
        for transaction in self.transactions:
            if transaction.prescriptionID:
                rows.append([transaction.PrescriptionID, transaction.purchase_price])
        table.add_rows(rows)
        return table.get_string()

        # TODO: output in the following format, the results:
        # |    # | Prescription ID | Total Price |

    def purchasesByUser(self, customerID: str):
        """Reports on the sales performed by a customer.
        
        Args:
            customerID: Username of the customer.

        Returns: A string representation of the corresponding transactions
            
        """
        # TODO: Query the transactions to the `transactions` list below
        transactions = []
        for transaction in self.transactions:
            if transaction.customerID == customerID:
                transactions.append(transaction)

        return BookRecords(transactions).__str__()

    def salesByAgent(self, salesperson: str):
        """Reports on the sales performed by a pharmacist.
        
        Args:
            salesperson: Username of the pharmacist.

        Returns: A string representation of the corresponding transactions
            
        """
        # TODO: Query the transactions to the `transactions` list below
        transactions = []
        for transaction in self.transactions:
            if transaction.customerID == salesperson:
                transactions.append(transaction)

        # return the string representation
        return BookRecords(transactions).__str__()

    def topNSales(self, start: datetime = datetime.strptime('1970-01-02', '%Y-%m-%d'), end: datetime = datetime.now(),
                  n=10) -> str:
        """Return the top n sales ordered by the total price of purchases.

        Args:
            start: a datetime representing the start period to consider (datetime, default to 01 Jan 1970)
            end: a datetime representing the end period to consider (datetime, default to current timestamp)
            n: number of records to consider (int, default to 10)

        Returns:
        A string representation of the top n 
        """

        # TODO: Query the top transactions and save them to the variable `transactions` below
        transactions = []
        for transaction in self.transactions:
            if start.timestamp() <= transaction.timestamp <= end.timestamp():
                transactions.append(transaction)

        sorted_transactions = sorted(transactions, key=lambda x: x.purchase_price, reverse=True)
        return BookRecords(sorted_transactions[:n]).__str__()

    def totalTransactions(self) -> float:
        """Returns the total cost of the transactions considered.
        
        Args:
        
        Returns: A floating number representing the total price
        """
        return sum([transaction.purchase_price for transaction in self.transactions])

    @classmethod
    def load(cls, infile: str) -> BookRecords:
        """Loads a JSON file containing a number of sales object
        
        Args:
            infile: path to the file to be read
        Returns: A new object with the transactions in the file
        """
        # TODO: Implement the function. Make sure to handle the cases where
        # the file does not exist.
        transactions: List[Sale] = []
        try:
            with open(infile, 'r') as f:
                file_data = json.load(f)
                for item in file_data:
                    transactions.append(Sale(**item))

        except FileNotFoundError as e:
            print("Invalid File Path")

        finally:
            return BookRecords(transactions)
