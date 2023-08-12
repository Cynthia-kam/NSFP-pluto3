import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;

import org.json.simple.parser.ParseException;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;

import org.json.simple.parser.JSONParser;

public class PrescriptionManagement {
    static FileHandler fileHandler = new FileHandler();

    public static void main(String[] args) throws IOException, ParseException {


        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int choice, numMedications;
        Prescription prescription = new Prescription();


        while (true) {
            System.out.println("Menu");
            System.out.println("1. Add prescription");
            System.out.println("2. View prescriptions");
            System.out.println("3. Delete prescription");
            System.out.println("4. Exit");

            System.out.println("Enter your choice : ");
            try{
                choice = Integer.parseInt(reader.readLine());
                switch (choice) {
                    case 1 -> {
                        // Don't forget to add code to save these information in the prescription
                        String prescriptionID, customerID, doctorName;
                        System.out.println("Enter prescription ID");
                        prescriptionID = reader.readLine();
                        prescription.setPrescriptionID(prescriptionID);
                        System.out.println("Enter customer ID");
                        customerID = reader.readLine();
                        prescription.setCustomerID(customerID);
                        System.out.println("Enter doctor name");
                        doctorName = reader.readLine();
                        prescription.setDoctorName(doctorName);
                        prescription.setDate(LocalDate.now());
                        System.out.print("Enter the number of medications to add: ");
                        numMedications = Integer.parseInt(reader.readLine());
                        ArrayList<Medication> medications = new ArrayList<>();
                        String medName, medDetails, medDosage, medID;
                        int medQty;
                        String medicationsFilePath = "products.json";
                        displayMedications(medicationsFilePath);
                        for (int i = 1; i <= numMedications; i++) {

                            System.out.println("Enter details for Medication " + i + ":");

                            System.out.println("Enter medication ID");
                            medID = reader.readLine();
                            System.out.println("Enter medication name");
                            medName = reader.readLine();
                            System.out.println("Enter medication details");
                            medDetails = reader.readLine();
                            System.out.println("Enter medication dosage");
                            medDosage = reader.readLine();
                            System.out.println("Enter medication quantity");
                            medQty = Integer.parseInt(reader.readLine());
                            prescription.setDate(LocalDate.now());

                            if(isMedicationInStock(medID, medName,medQty)){
                                Medication medication = new Medication(medID, medName, medDetails, medDosage, medQty);
                                medications.add(medication);
                                prescription.setMedications(medications);
                                prescription.addPrescription(prescription);
                            }else{
                                System.out.println("Medication unavailable. Please check medication ID, name or quantity");
                                break;
                            }
                        }
                    }
                    case 2 -> {
                        // Prescriptions must be returned in the array
                        ArrayList<Prescription> prescriptions = prescription.viewPrescription();
                        if (prescriptions.size() == 0) {
                            System.out.println("No prescriptions available\n");
                        } else {
                            System.out.println("| PrescriptionID |  DoctorName   |    CustomerID | \tDate\t | ");
                            System.out.println("******************************************************************");

                            for (Prescription p : prescriptions) {
                                System.out.println("|\t  " + p.getPrescriptionID() + "\t\t" + p.getDoctorName() + "\t\t  " + p.getCustomerID() + "\t\t" + p.getDate());

                                System.out.println("| MedicationID |  \tName    | \t Quantity | ");

                                for (Medication med : p.getMedications()) {
                                    System.out.println("|\t  " + med.getID() + "\t\t" + med.getName() + "\t\t " + med.getQuantity());
                                }

                                System.out.print("\n");
                                System.out.println("*****************************************************************");
                            }

                            System.out.println("");
                        }
                    }
                    case 3 -> {
                        // Prescriptions must be returned in the array
                        ArrayList<Prescription> prescriptions = prescription.viewPrescription();
                        if (prescriptions.size() == 0) {
                            System.out.println("No prescriptions available\n");
                        } else {
                            System.out.println("| PrescriptionID |  DoctorName   |    CustomerID | \tDate\t | ");
                            System.out.println("******************************************************************");

                            for (Prescription p : prescriptions) {
                                System.out.println("|\t  " + p.getPrescriptionID() + "\t\t" + p.getDoctorName() + "\t\t  " + p.getCustomerID() + "\t\t" + p.getDate());

                                System.out.println("| MedicationID |  \tName    | \t Quantity | ");

                                for (Medication med : p.getMedications()) {
                                    System.out.println("|\t  " + med.getID() + "\t\t" + med.getName() + "\t\t " + med.getQuantity());
                                }

                                System.out.print("\n");
                                System.out.println("*****************************************************************");
                            }

                            System.out.println("");
                        }
                        String prescriptionID;
                        System.out.println("Enter ID of prescription to delete : ");
                        prescriptionID = reader.readLine();
                        prescription.deletePrescription(prescriptionID);
                    }
                    case 4 -> {
                        System.out.println("Exiting the Prescription Management section...");
                        System.exit(0);
                    }
                    default -> System.out.println("Invalid choice. Please try again.");
                }
            }catch (NumberFormatException e){
                System.out.println("Please enter a number");
            }

        }

    }

    public static boolean isMedicationInStock(String medicationID, String medicationName, int medicationQuantity) throws FileNotFoundException, IOException, ParseException {
        JSONParser parser = new JSONParser();
        boolean isMedicationInStock = false;
        int availableQuantity;
        String availableMedicationID, availableMedicationName;
        try (FileReader fileReader = new FileReader("products.json")) {
            if (fileReader.read() == -1) {
                return false;
            } else {
                fileReader.close();
                JSONArray jsonArray = (JSONArray) parser.parse(new FileReader("products.json"));
                for (Object obj : jsonArray) {
                    JSONObject jsonObject = (JSONObject) obj;
                    //Compare ID of available medication to passed medication
                    availableMedicationID = (String) jsonObject.get("code");
                    availableMedicationName = (String) jsonObject.get("name");
                    availableQuantity = Integer.parseInt((String) jsonObject.get("quantity"));
                    if(availableMedicationID.equals(medicationID) && availableMedicationName.equals(medicationName) && medicationQuantity<=availableQuantity && availableQuantity>0){
                        isMedicationInStock = true;
                        break;
                    }
                }
            }
            return isMedicationInStock;
        }
    }


        public static void displayMedications(String filePath) throws IOException, ParseException {
            String medicationID, medicationName, medicationPrice, medicationQuantity;
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

                        // medication ID, name, price and quantity should be casted to String
                        medicationID = (String) jsonObject.get("code");
                        medicationName = (String) jsonObject.get("name");
                        medicationPrice = (String) jsonObject.get("price");
                        medicationQuantity = (String) jsonObject.get("quantity");
                        System.out.println("|\t" + medicationID + "\t\t" + medicationName + "\t\t  " + medicationPrice + "\t\t\t  " + medicationQuantity + "\t\t");

                    }
                    System.out.println("---------------------------------------------------------------------------------------");


                }
            }

        }

    }
