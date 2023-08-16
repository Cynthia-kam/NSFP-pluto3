#include <iostream>
#include <string>
#include <chrono>
#include <random>
#include <vector>
#include <sstream>
#include <string.h>

using namespace std;
using namespace std::chrono;

class Product
{

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
    string getCode()
    {
        return code;
    }

    string getName()
    {
        return name;
    }

    string getBrand()
    {
        return brand;
    }

    string getDescription()
    {
        return description;
    }

    string getDosageInstruction()
    {
        return dosageInstruction;
    }

    string getCategory()
    {
        return category;
    }

    int getQuantity()
    {
        return quantity;
    }

    float getPrice()
    {
        return price;
    }

    bool getRequiresPrescription()
    {
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

    string promptTextField(string promptText)
    {
        // method takes text to display e.g: "Enter Product Name:"
        // it prompts a user and return user input in form of text. Text can be made by multiple words.
        string textInput;
        cout << promptText << endl;
        getline(cin, textInput);
        return textInput;
    }

    float promptNumberField(string promptText)
    {
        // method takes text to display e.g: "Enter Product Name:"
        // it prompts a user and return user input in form of text. Text can be made by multiple words.
        string textInput;
        cout << promptText << endl;
        getline(cin, textInput);
        return stof(textInput);
    }

    bool promptRequirePrescription()
    {
        // User can type 1 or 0.
        // it prompts a user and return user input in form of boolean.
        string textInput;
        cout << "Does product require a prescription?" << endl;
        getline(cin, textInput);
        return bool(stoi(textInput));
    }

    void createProduct()
    {
        cin.ignore();
        string product_name = promptTextField("Enter product name:");
        name = product_name;
        cout << "Saving name as " << product_name << endl;
        string product_brand = promptTextField("Enter product brand:");
        brand = product_brand;
        cout << "Saving brand as " << product_brand << endl;
        string product_description = promptTextField("Enter product description:");
        description = product_description;
        string product_category = promptTextField("Enter product category:");
        category = product_category;
        string product_dosageInstruction = promptTextField("Enter product dosage instruction:");
        dosageInstruction = product_dosageInstruction;
        float product_quantity = promptNumberField("Enter product quantity:");
        quantity = product_quantity;
        float product_price = promptNumberField("Enter product price:");
        price = product_price;
        bool product_requiresPrescription = promptRequirePrescription();
        requires_prescription = product_requiresPrescription;
        // Add code to generate Unique code for product using generateUniqueCode method
        string unique_code = generateUniqueCode();
        code = unique_code;
    };

    string toJson()
    {

        string productInJson;
        // The Output should look like:
        //{"code":"tgtwdNbCnwx","name":"name 1","brand":"br 2","description":"df","dosage_instruction":"dfg","price":123.000000,"quantity":13,"category":"des","requires_prescription":1}
        productInJson += "{\"code\":\"" + code + "\","
                                                 "\"name\":\"" +
                         name + "\","
                                "\"brand\":\"" +
                         brand + "\","
                                 "\"description\":\"" +
                         description + "\","
                                       "\"dosage_instruction\":\"" +
                         dosageInstruction + "\","
                                             "\"price\":\"" +
                         to_string(price) + "\","
                                            "\"quantity\":\"" +
                         to_string(quantity) + "\","
                                               "\"category\":\"" +
                         category + "\","
                                    "\"requires_prescription\":\"" +
                         to_string(requires_prescription) + "\"}";
        return productInJson;
    };

    Product productFromJson(string txt)
    {
        int size = txt.size();
        if (txt[size - 1] == ',')
        {
            txt.erase(0, 1);
            txt.erase(size - 3, 2);
        }
        else
        {
            txt.erase(0, 1);
            txt.erase(size - 2, 1);
        }

        char *mutableStr = new char[txt.size() + 1];
        strcpy(mutableStr, txt.c_str());

        int i = 0;
        char *token = strtok(mutableStr, ",");
        string keyValues[9];

        while (token != NULL)
        {
            keyValues[i] = token;
            token = strtok(NULL, ",");
            i++;
        }
        Product product;
        product.code = fetchStrValue(keyValues[0]);
        product.name = fetchStrValue(keyValues[1]);
        product.brand = fetchStrValue(keyValues[2]);
        product.description = fetchStrValue(keyValues[3]);
        product.dosageInstruction = fetchStrValue(keyValues[4]);
        product.price = fetchFloatValue(keyValues[5]);
        product.quantity = fetchFloatValue(keyValues[6]);
        product.category = fetchStrValue(keyValues[7]);
        product.requires_prescription = fetchBoolValue(keyValues[8]);

        delete[] mutableStr; // Free the dynamically allocated memory

        return product;
    }

    string fetchStrValue(string keyValueStr)
    {
        // Input sample "code":"ThisCode"
        string keyValue;
        vector<string> values;
        int m = 0;
        int colonPosition = keyValueStr.find(':');
        string str = keyValueStr.substr(colonPosition + 1);

        for (auto character : str)
        {
            if (character == '"')
            {
                values.push_back(keyValue);
                keyValue = "";
            }
            else
            {
                keyValue = keyValue + character;
            }
        }

        return values[1];
    }

    float fetchFloatValue(string keyValueStr)
    {
        // Input sample "price":13.900000
        string keyValue;
        int colonPosition = keyValueStr.find(':');
        string str = keyValueStr.substr(colonPosition + 1);
        stringstream ss(str);
        float val;
        ss >> val;
        return val;
    }

    bool fetchBoolValue(string keyValueStr)
    {
        // Input sample "requires_prescription":1
        string keyValue;
        int colonPosition = keyValueStr.find(':');
        string str = keyValueStr.substr(colonPosition + 1);
        stringstream ss(str);
        bool val;
        ss >> val;
        return val;
    }
};
