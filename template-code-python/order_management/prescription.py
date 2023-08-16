import json

from typing import List, Dict, Union
from .product import Product

prescription_file = "../data/prescriptions.json"
class Prescription:
    """Represents a prescription object

    Attributes:
        DoctorName: the name of the doctor who gave the prescription
        PrescriptionID: ID of the prescription
        Medications: list of the medications, this is the quantity, the ID, the name, and whether it was processed or not
        # see format in prescriptions.json
        CustomerID: ID of the customer
    """

    def __init__(self, DoctorName: str, PrescriptionID: str, Medications: List[Dict[str, Union[int, str, bool]]],
                 CustomerID: str, Date: str) -> None:
        self.DoctorName = DoctorName
        self.PrescriptionID = PrescriptionID
        self.Medications = Medications
        self.CustomerID = CustomerID

    def medecineInPrescription(self, product: Product, quantity: int) -> bool:
        """Verifies if a medecine with the specified quantity is included in a prescription

        Args:
            product: the product to verify
            quantity: the quantity to be added

        Returns: A boolean denoting whether the value was found
        """
        # TODO: Implement the function
        with open(prescription_file, 'r') as f:
            file_data = json.load(f)
            for item in file_data:
                if item['PrescriptionID'] == self.PrescriptionID:
                    for med in item['Medications']:
                        if med['id'] == product.code and med['quantity'] == quantity:
                            return True
                        else:
                            return False


    def markComplete(self, product: Product):
        """Mark a product's sale complete in the prescriptions file

        Args:
            product: the product sold

        Returns: None
        """
        # TODO: Change the value "ProcessedStatus" of the relevant product to True
        # with open(prescription_file, 'r') as f:
        #     file_data = json.load(f)
        #     for item in file_data:
        #         if item['PrescriptionID'] == self.PrescriptionID:
        #             for med in item['Medications']:
        #                 if med['id'] == product.code:
        #                     med['ProcessedStatus'] = True

        for medication in self.Medications:
            if medication['id'] == product.code:
                medication['ProcessedStatus'] = True


    def dump(self, outfile: str):
        """Dumps the updated prescription to the specified file
        
        Args: 
            outfile: path to the file where the output should be written

        Returns: None
        """
        # TODO: Read the output file (safely).

        with open(prescription_file, 'r') as f:
            file_data = json.load(f)

        # TODO: Update the prescription that is being edited in the loaded data
            for item in file_data:
                if item['PrescriptionID'] == self.PrescriptionID:
                    item['Medications'] = self.Medications

        # TODO: Save the updated object
        with open(outfile, 'w') as out_file:
            json.dump(file_data, out_file)
            print("Successfully saved the prescription")


    @classmethod
    def get(cls, infile: str, id: str):
        """Retrieves a specific prescription from a file
        
        Args:
            infile: path to the input file
            id: identifier of the prescription to add

        Returns: A prescription object as a dictionary
        """
        # TODO: Load the file and find the object with the relevant ID
        # TODO: Return the relevant prescription
        with open(infile, 'r') as f:
            file_data = json.load(f)
            for item in file_data:
                if item['PrescriptionID'] == id:
                    # return Prescription(item['DoctorName'], item['PrescriptionID'], item['Medications'], item['CustomerID'])
                    return {
                        'DoctorName': item['DoctorName'],
                        'PrescriptionID': item['PrescriptionID'],
                        'Medications': item['Medications'],
                        'CustomerID': item['CustomerID'],
                    }
