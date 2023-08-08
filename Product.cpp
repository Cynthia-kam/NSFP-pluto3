#include <iostream>
#include <string>
#include <chrono>
#include <random>
#include <cstring>

using namespace std;
using namespace std::chrono;

class Product{

    private:
    int quantity;
    string name;
    string brand;
    string description;
    string code;
    float price;
    string dosageInstruction;
    string category;
    bool requires_prescription;

    public:

    string getName(){
        return name;
    }

    string getBrand(){
        return brand;
    }

    string getDescription(){
        return description;
    }

    string getDosageInstruction(){
        return dosageInstruction;
    }

    string getCategory(){
        return category;
    }
    
    int getQuantity(){
        return quantity;
    }

    float getPrice(){
        return price;
    }

    bool getRequiresPrescription(){
        return requires_prescription;
    }


    string generateUniqueCode()
    {
        string characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";

        string uniqueCode = "";
        auto now = system_clock::now();
        auto millis = duration_cast<milliseconds>(now.time_since_epoch());
        mt19937 generator(millis.count());
        uniform_int_distribution<int> distribution(0, 100000);

        // generate 10 characters long unique string

        for (int i = 0; i <= 10; i++)
        {
            int random_index = distribution(generator) % characters.length();
            uniqueCode += characters[random_index];
        }

        return uniqueCode;
    };

    string promptTextField(string promptText){
        // method takes text to display e.g: "Enter Product Name:"
        // it prompts a user and return user input in form of text. Text can be made by multiple words.
        string textInput;
        cout << promptText <<endl;
        getline(cin, textInput);
        return textInput;
    }


    float promptNumberField(string promptText){
        // method takes text to display e.g: "Enter Product Name:"
        // it prompts a user and return user input in form of text. Text can be made by multiple words.
        string textInput;
        cout << promptText <<endl;
        getline(cin, textInput);
        return stof(textInput);
    }

    bool promptRequirePrescription()
    {
        // User can type 1 or 0. 
        // it prompts a user and return user input in form of boolean.
        string textInput;
        cout << "Does product require a prescription?" <<endl;
        getline(cin, textInput);
        return bool(stoi(textInput));
    }

    void createProduct()
    {
        Product product;
        string product_name = promptTextField("Enter product name:");
        product.name = product_name;
        string product_brand = promptTextField("Enter product brand:");
        product.brand = product_brand;
        string product_description = promptTextField("Enter product description:");
        product.description = product_description;
        string product_category = promptTextField("Enter product category:");
        product.category = product_category;
        string product_dosageInstruction = promptTextField("Enter product dosage instruction:");
        product.dosageInstruction = product_dosageInstruction;
        float product_quantity = promptNumberField("Enter product quantity:");
        product.quantity = product_quantity;
        float product_price = promptNumberField("Enter product price:");
        product.price = product_price;
        bool product_requiresPrescription = promptRequirePrescription();
        product.requires_prescription = product_requiresPrescription;
        // Add code to generate Unique code for product using generateUniqueCode method
        string unique_code = generateUniqueCode();
        product.code = unique_code;
    };

    string toJson()
    {

        string productInJson;
      // The Output should look like:
      //{"code":"tgtwdNbCnwx","name":"name 1","brand":"br 2","description":"df","dosage_instruction":"dfg","price":123.000000,"quantity":13,"category":"des","requires_prescription":1}

        Product product;
        productInJson = "{\"code\":\""+product.code+"\","
                        "\"name\":\""+product.name+"\","
                        "\"brand\":\""+product.brand+"\","
                        "\"description\":\""+product.description+"\","
                        "\"dosage_instruction\":\""+product.dosageInstruction+"\","
                        "\"price\":\""+to_string(product.price)+"\","
                        "\"quantity\":\""+to_string(product.quantity)+"\","
                        "\"category\":\""+product.category+"\","
                        "\"requires_prescription\":\""+ to_string(product.requires_prescription)+"\"}";
        return productInJson;
    };

    void productFromJson(string txt)
    {
        //TODO Add code to convert a json string product to product object
        // string is in the form below
        //{"code":"tgtwdNbCnwx","name":"name 1","brand":"br 2","description":"df","dosage_instruction":"dfg","price":123.000000,"quantity":13,
        // "category":"des","requires_prescription":1}
        // You need to extract value for each field and update private attributes declared above.
        int size = txt.size();
        if(txt[size-1] == ','){
            txt.erase(0,1);
            txt.erase(size-3, 2);
        }else{
            txt.erase(0,1);
            txt.erase(size-2, 1);
        }

        int i = 0;
        char* str = txt.data();
        char *token = strtok(str, ",");
        string keyValues[9];
        
        while (token != NULL)
        {
            keyValues[i] = token;
            token = strtok(NULL, ",");
            i++;
        }

        Product product;
        product.code = fetchValue(keyValues[0]);
    };

    //TODO Implement a way to strip the quotes and pick the value from the key-value pair
    string fetchValue(string keyValueStr) {
        for (auto character : keyValueStr)
        {
            if (character == '"')
            {
                keyValueStr = "";
            }
            else
            {
                keyValueStr = keyValueStr + character;
            }
            //Full string is printed at this point
            std::cout << keyValueStr << std::endl;
        }
        //Full string is cleared by this point
        std::cout << keyValueStr << std::endl;
        return keyValueStr;
    }
};
