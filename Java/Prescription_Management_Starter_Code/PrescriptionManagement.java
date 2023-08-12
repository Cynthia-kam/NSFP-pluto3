import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.UUID;

import com.sun.org.apache.xpath.internal.operations.Bool;
import org.json.simple.parser.ParseException;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;

import org.json.simple.parser.JSONParser;

public class PrescriptionManagement {
    private static String medicationID=null;
    private static String medicationName=null;
    private static String medicationPrice=null;
    private static Prescription[] prescriptions;
    private static String medicationQuantity;

    public static void main(String[] args) throws IOException, ParseException {
       UUID uuid= UUID.randomUUID();
	   BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
       int choice , numMedications;

       String prescriptionID=null;
       String customerID=null;
       String doctorName=null;
       LocalDate dateToPrint=null;
       ArrayList<Medication> medications = new ArrayList<>();
       Prescription prescription = new Prescription(prescriptionID, customerID, doctorName, dateToPrint, medications);
      while(true) {

            // TODO: Add code to display the menu and get the number(choice) a user selected
             System.out.println("1.Add prescription");
             System.out.println("2.View prescription");
             System.out.println("3.Delete prescription");
             System.out.println("4.Process prescription");
             System.out.println("Enter your choice: ");
             choice = Integer.parseInt(reader.readLine());
            switch (choice) {
               case 1:
            	   
                    // TODO: Add code to get Prescription ID, Customer ID,  Doctor's Name
                    // Don't forget to add code to save these information in the prescription
                   prescriptionID = String.valueOf(uuid);
                   prescription.setPrescriptionID(prescriptionID);
                   customerID=String.valueOf(uuid);
                   prescription.setCustomerID(customerID);
                   System.out.print("Enter doctor's name: ");
                   doctorName=reader.readLine();
                   prescription.setDoctorName(doctorName);
                   prescription.setDate(LocalDate.now());
                   // TODO: Add code to display available products/medications before adding them on the prescription
                   String medicationsFilePath = "products.json";
                   System.out.print("Enter the number of medications to add: ");
                   numMedications = Integer.parseInt(reader.readLine());
                   for (int i = 1; i <= numMedications; i++) {

                       System.out.println("Enter details for Medication " + i + ":");

                       // TODO: Add code to get Medication ID, Name, Details, Dosage and Quantity
                       String medicationName, medicationDetails, dosage, medicationID;
                       int quantity;

                       System.out.print("Enter medication name: ");
                       medicationName= reader.readLine();

                       System.out.print("Enter medication details: ");
                       medicationDetails=reader.readLine();

                       System.out.print("Enter dosage: ");
                       dosage= reader.readLine();

                       medicationID=String.valueOf(uuid);

                       System.out.println("Enter medication quantity: ");
                       quantity= Integer.parseInt(reader.readLine());

                       prescription.setDate(LocalDate.now());

                       Medication medication = new Medication(medicationID, medicationName, medicationDetails, dosage, quantity);
                       medication.setProcessedStatus(false);
                       medication.getProcessedStatus();
                       medications.add(medication);
                   }

                    // TODO: Add code to save all medications inserted by the user on the prescription
                   prescription.setMedication(medications);
                   prescription.addPrescription();
                   
                   break;
               case 2:
                    // TODO: Add code to retrieve all prescriptions in the file
                    // Prescriptions must be returned in the array

                   if(prescriptions.length==0) {
                       System.out.println("No prescriptions available\n");
                   }
                   else {
                       System.out.println("| PrescriptionID |  DoctorName   |    CustomerID | \tDate\t | ");
                       System.out.println("******************************************************************");

                       for(Prescription p: prescriptions)
                       {
                           System.out.println("|\t  "+ p.getPrescriptionID()+"\t\t"+ p.getDoctorName()+ "\t\t  " + p.getCustomerID()+"\t\t" + p.getDate());

                           System.out.println("");
                           System.out.println("| MedicationID |  \tName    | \t Quantity | ");
                           for(Medication med : p.getMedications())
                           {
                               System.out.println("|\t  "+ med.getID()+"\t\t"+ med.getName()+ "\t\t " + med.getQuantity() );
                           }

                           System.out.print("\n");
                           System.out.println("*****************************************************************");
                       }

                       System.out.println("");
                   }

            	   break;
               case 3:
                    // TODO: Add code to get the ID of the prescription you want to delete


                   Object prescrID = null;
                   prescription.deletePrescription(prescrID);
                  break;
               case 4:
                   System.out.println("Exiting the Prescription Management section...");
                   System.exit(0);
               default:
                  System.out.println("Invalid choice. Please try again.");
            }
            
            

         
         
      }
   }
   
   
   
   public static void displayMedications(String filePath) throws FileNotFoundException, IOException, ParseException {
	   
	      JSONParser parser = new JSONParser();
	      try(FileReader fileReader = new FileReader(filePath)){
	          if (fileReader.read() == -1) {
	              return;
	          } 
	          else {
	              fileReader.close();
	              JSONArray jsonArray = (JSONArray) parser.parse(new FileReader(filePath));
	              
                  System.out.println("---------------------------------------------------------------------------------------");
                  System.out.println("|\t"  + "\t\t  "  + "\t\t\t\t");
                  System.out.println("|\t" + "\t\t"  +  "Available Medications" + "\t\t");
                  System.out.println("|\t"  + "\t\t  "  + "\t\t\t\t");
                  System.out.println("---------------------------------------------------------------------------------------");
                  System.out.println("| Medication ID |  Medication Name   |    Medication Price ||    Medication Quantity |");
                  System.out.println("---------------------------------------------------------------------------------------");
                  
	              for (Object obj: jsonArray) {
	                  JSONObject jsonObject = (JSONObject) obj;
	                  
                    // TODO: Add code to get medication ID (it's named as code from medications/products file), name, price and quantity
                    // medication ID, name, price and quantity should be casted to String

                      
                      System.out.println("|\t" + medicationID + "\t\t" + medicationName + "\t\t  " + medicationPrice + "\t\t\t  " + medicationQuantity + "\t\t");
	                  
	              }
                  System.out.println("---------------------------------------------------------------------------------------");

	              
	          }  
	      }
	   
   } 


}
