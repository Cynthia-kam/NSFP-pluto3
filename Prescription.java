import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.time.LocalDate;
import java.util.ArrayList;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;

import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;


public class Prescription {
	   private String prescriptionID;
	   private String customerID;
	   private String doctorName;
	   private ArrayList<Medication> medications;
	   private LocalDate date;
	   private JSONArray prescriptionList;
	   private final FileHandler fileHandler = new FileHandler();
	   

	   public Prescription() { 
		   prescriptionList = new JSONArray();
	   }
	   
	   public Prescription(String _prescriptionID, String _customerID, String _doctorName, ArrayList<Medication> _medication)
	   {
	       prescriptionID = _prescriptionID;
	       customerID = _customerID;
	       doctorName = _doctorName;
	       medications = _medication;
	       date = LocalDate.now();
	   }

	public Prescription(String _prescriptionID, String _customerID, String _doctorName, LocalDate _date, ArrayList<Medication> _medications) {
		prescriptionID = _prescriptionID;
		customerID = _customerID;
		doctorName = _doctorName;
		medications = _medications;
		date = _date;
	}

	public String getPrescriptionID() {
		return prescriptionID;
	}

	public void setPrescriptionID(String prescriptionID) {
		this.prescriptionID = prescriptionID;
	}

	public String getCustomerID() {
		return customerID;
	}

	public void setCustomerID(String customerID) {
		this.customerID = customerID;
	}

	public String getDoctorName() {
		return doctorName;
	}

	public void setDoctorName(String doctorName) {
		this.doctorName = doctorName;
	}

	public ArrayList<Medication> getMedications() {
		return medications;
	}

	public void setMedications(ArrayList<Medication> medications) {
		this.medications = medications;
	}

	public LocalDate getDate() {
		return date;
	}

	public void setDate(LocalDate date) {
		this.date = date;
	}

	public JSONArray getPrescriptionList() {
		return prescriptionList;
	}

	public void setPrescriptionList(JSONArray prescriptionList) {
		this.prescriptionList  = prescriptionList;
	}
		// While adding the prescription in the file, please follow the format shown below
		// Format for the prescription: {"DoctorName":"Yves","PrescriptionID":"TA3","Medications":[{"quantity":2,"processedStatus":false,"name":"IBUPROFEN","id":"IB7"}],"CustomerID":"GR","Date":"2023-08-07"}

	public void addPrescription(Prescription prescription) throws IOException, ParseException {
	        JSONArray existingPrescriptions = fileHandler.readJSONArrayFromFile();
			JSONObject prescriptionObject = new JSONObject();

			JSONArray medArray = getMedicationsOnPrescription(prescription);

			prescriptionObject.put("DoctorName",prescription.getDoctorName());
			prescriptionObject.put("PrescriptionID",prescription.getPrescriptionID());
			prescriptionObject.put("CustomerID",prescription.getCustomerID());
			prescriptionObject.put("Date",String.valueOf(prescription.getDate()));

			prescriptionObject.put("Medications",medArray);

	        existingPrescriptions.add(prescriptionObject);

	        fileHandler.writeJSONArrayToFile(existingPrescriptions);
	    }

		 //Convert ArrayList of medications to JSONArray of Medications with key-value pairs
	     //This can then be written to prescriptions.json file
		 JSONArray getMedicationsOnPrescription(Prescription prescription) {
			ArrayList<Medication> medicationsList = prescription.getMedications();
			JSONArray medicationArray = new JSONArray();

			for (Medication m : medicationsList) {
				JSONObject medicationObject = new JSONObject();
				medicationObject.put("quantity", m.getQuantity());
				medicationObject.put("processedStatus", m.getProcessedStatus());
				medicationObject.put("name", m.getName());
				medicationObject.put("id", m.getID());
				medicationArray.add(medicationObject);
			}
			return medicationArray;
		}

	   	public ArrayList<Prescription> viewPrescription() throws IOException, ParseException {

	        JSONArray jsonArray = fileHandler.readJSONArrayFromFile();
			ArrayList<Prescription> prescriptions = new ArrayList<>();
	        for (Object obj : jsonArray) {
	            JSONObject jsonObject = (JSONObject) obj;
                
                String doctorName = (String) jsonObject.get("DoctorName");
                String prescriptionID = (String) jsonObject.get("PrescriptionID");
                String customerID = (String) jsonObject.get("CustomerID");
                String date = (String) jsonObject.get("Date");
                LocalDate dateToPrint = LocalDate.parse(date);
                ArrayList<Medication> medications = new ArrayList<>();
                JSONArray medicationsArray = (JSONArray) jsonObject.get("Medications");

                for (Object medObj : medicationsArray) {
					// medication quantity should be casted to int
                    // also medication ID and name should be casted to String
					String medicationID, medicationName;
					int quantity;
					JSONObject mJsonObject = (JSONObject)medObj;
					medicationID = (String)mJsonObject.get("id");
					medicationName = (String)mJsonObject.get("name");
					quantity = Integer.parseInt(mJsonObject.get("quantity").toString());
					//Add new medication object to medications ArrayList
                    medications.add(new Medication(medicationID, medicationName, quantity));
                }
				//Add prescription object to prescriptions ArrayList with medications ArrayList to prescriptions object
                prescriptions.add(new Prescription(prescriptionID,customerID, doctorName, dateToPrint, medications));
                
            }
			return prescriptions;
	    }

		public void deletePrescription(String prescriptionID) throws IOException, ParseException {
			JSONArray existingPrescriptions = fileHandler.readJSONArrayFromFile();
			int indexToDelete = -1;
			for (int i = 0; i < existingPrescriptions.size(); i++) {
				JSONObject jsonObject = (JSONObject) existingPrescriptions.get(i);
				String existingPrescriptionID = (String) jsonObject.get("PrescriptionID");

				if (prescriptionID.equals(existingPrescriptionID)) {
					indexToDelete = i;
				}
			}
			if (indexToDelete == -1) {
				System.out.println("Item "+prescriptionID+" not found");
			}else{
				existingPrescriptions.remove(indexToDelete);
				fileHandler.writeJSONArrayToFile(existingPrescriptions);
			}
		}

}

