#include "FileHandler.cpp"
#include <iomanip>

class SearchProduct
{
private:
    string filename;

public:
    string searchText;
    FileHandler fHandler;

    string to_lowercase(const string& text) {
        string lowercase_text;
        for (char c : text) {
            lowercase_text += tolower(c);
        }
        return lowercase_text;
    }

    vector<Product> searchByName(string name){
        //Add code to search by name. Searching is not case-sensitive it means
        //for input like: "name" products with names like "Name 1", "Product name" needs to included in the found results.
        cout << "Calling search by name" << endl;

        vector<Product> productsVector = fHandler.readJsonFile();

        cout << "Calling search by name again" << endl;
        vector<Product> searchVector;
        Product product;


        for(int i = 0; i< productsVector.size(); i++){
            product = productsVector.at(i);
            cout << "Product details : " << product.getName() << endl;
            if(to_lowercase(product.getName()).find(to_lowercase(name)) != std::string::npos){
                searchVector.push_back(product);
            }else{
                cout << "Not found" << endl;
            }
        }
        return searchVector;
    };

    vector<Product> searchByCategory(string category){
        //Add code to search by category. Searching is not case-sensitive it means
        //for input like: "categ" products with category like "category 1", "Product category" needs to included in the found results.
        vector<Product> productsVector = fHandler.readJsonFile();
        vector<Product> searchVector;
        Product product;

        for(int i = 0; i< productsVector.size(); i++){
            product = productsVector.at(i);
            if(to_lowercase(product.getCategory()).find(to_lowercase(category)) != std::string::npos){
                searchVector.push_back(product);
            }else{
                cout << "Not found" << endl;
            }
        }
        return searchVector;
    };

    vector<Product> searchByBrand(string brand){
        //Add code to search by brand. Searching is not case sensitive it means 
        //for input like: "br" products with names like "Brand 1", "brand name" needs to included in the found results.
        vector<Product> productsVector = fHandler.readJsonFile();
        vector<Product> searchVector;
        Product product;

        for(int i = 0; i< productsVector.size(); i++){
            product = productsVector.at(i);
            if(to_lowercase(product.getBrand()).find(to_lowercase(brand)) != std::string::npos){
                searchVector.push_back(product);
            }else{
                cout << "Not found" << endl;
            }
        }
        return searchVector;
    };

    void showSearchResult(vector<Product> plist, string sTxt)
    {
        //Add code to display Search results
        cout << "Displaying search results for " << sTxt << endl;
        cout<<"|Product Name |Brand   |Description   |Price   |Dosage    | Requires prescription   |Qty available  |"<<endl;
        cout<<"***********************"<<endl;
        for(Product p : plist){
            cout << "|" << sizeTextto10(p.getName());
            cout << "|" << sizeTextto10(p.getBrand());
            cout << "|" << sizeTextto10(p.getDescription());
            cout << "|" << sizeTextto10(p.getDosageInstruction());
            cout << "|" << sizeBoolto10(p.getRequiresPrescription());
            cout << "|" << sizeExpAmountTo9(p.getQuantity()) << "|" << endl;
        }

    }

    string sizeTextto10(string displayString) {
        return(displayString.append(10 - displayString.length(), ' '));
    }

    string sizeBoolto10(bool requiresPrescription) {
        string boolVal = "";
        if (requiresPrescription){
            boolVal = "Yes";
        }else{
            boolVal = "No";
        }
        return(boolVal.append(10 - boolVal.length(), ' '));
    }

    string sizeExpAmountTo9 (float floatStr)
    {
        std::stringstream stream;
        stream << std::fixed << std::setprecision(2) << floatStr;
        std::string str_formatted_expense = stream.str();
        return(str_formatted_expense.append(10 - str_formatted_expense.length(), ' '));
    }

};