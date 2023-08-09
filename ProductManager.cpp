#include "SearchProduct.cpp"

class ProductManager
{
private:
    Product prod;
public:
    int getMenu(){
        int selected = -1;
        bool isChoiceValid = false;

        while(!isChoiceValid){
            cout<<"Menu:"<<endl;
            cout<<"1. Add product"<<endl;
            cout<<"2. Search Product By Name"<<endl;
            cout<<"3. Search Product By Category"<<endl;
            cout<<"4. Search Product By Brand"<<endl;
            cout<<"5. Update Product"<<endl;
            cout<<"6. Delete Product"<<endl;
            cout<<"7. Exit Application"<<endl;

            cout << "Enter your choice: " << endl;

            cin >> selected;

            if(selected < 1 || selected > 7 ||cin.fail()){
                cout << "Invalid selection" <<endl;
                cin.clear();
                cin.ignore(numeric_limits<streamsize>::max(), '\n');
            }else{
                isChoiceValid = true;
            }
        }
        return selected;
    }

    void addProduct(){
        // TODO add code to add product and 
            // store the product to products.json file by using Product class and FileHandler class
    }

    // TODO Add code for Updating a product

    // TODO Add code for deleting a product
    
};

int main()
{

    // ADD Code for displaying a welcome Menu
    // and handle all required logic to add, search, update, and delete product
    ProductManager productManager;
    SearchProduct searchProduct;
    vector<Product> resultsVector;
    string searchTerm;

    int choice = -1;

    while(choice!=7){
        choice = productManager.getMenu();
        if(choice == 1){
            cout << "Selected 1";
        }
        else if(choice == 2){
            cout << "Enter product name below:" << endl;

            cin.ignore();
            getline(cin, searchTerm);

            resultsVector = searchProduct.searchByName(searchTerm);
            searchProduct.showSearchResult(resultsVector, searchTerm);
        }
        else if(choice == 3){
            cout << "Enter product category below:" << endl;

            cin.ignore();
            getline(cin, searchTerm);

            resultsVector = searchProduct.searchByCategory(searchTerm);
            searchProduct.showSearchResult(resultsVector, searchTerm);
        }
        else if(choice == 4){
            cout << "Enter product brand below:" << endl;

            cin.ignore();
            getline(cin, searchTerm);

            resultsVector = searchProduct.searchByBrand(searchTerm);
            searchProduct.showSearchResult(resultsVector, searchTerm);
        }
        else if(choice == 5){
            cout << "Selected 5";
        }
        else if(choice == 6){
            cout << "Selected 6";
        }
        else if(choice == 7){
            cout << "Thank you for using E-Pharmacy" << endl;
            exit(EXIT_SUCCESS);
        }
        else{
            cout << "Please try again..." << endl;
        }
    }
    return 0;
}


