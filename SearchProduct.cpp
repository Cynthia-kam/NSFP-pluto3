#include "FileHandler.cpp"

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
        //Add code to search by name. Searching is not case sensitive it means
        //for input like: "name" products with names like "Name 1", "Product name" needs to included in the found results.
        vector<Product> productsVector = fHandler.readJsonFile();
        vector<Product> searchVector;
        Product product;

        for(int i = 0; i< productsVector.size(); i++){
            product = productsVector.at(i);
            //cout << product.toJson();
            if(to_lowercase(product.getName()).find(to_lowercase(name)) != std::string::npos){
                searchVector.push_back(product);
            }else{
                //cout << "Not found" << endl;
            }
        }
        return searchVector;
    };

    vector<Product> searchByCategory(string category){
        //Add code to search by category. Searching is not case sensitive it means 
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
        // TODO
        //Add code to display Search results

    }
};