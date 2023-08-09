#include "SearchProduct.cpp"

class ProductManager
{
private:
    Product prod;
public:
    int getMenu(){
        int selected = -1;

        cout<<"Menu:"<<endl;
        cout<<"1. Add product"<<endl;
        cout<<"2. Search Product By Name"<<endl;
        cout<<"3. Search Product By Category"<<endl;
        cout<<"4. Product By Brand"<<endl;
        cout<<"5. Update Product"<<endl;
        cout<<"6. Delete Product"<<endl;
        cout<<"7. Exit Application"<<endl;

        cout << "Enter your choice: " << endl;

        cin >> selected;

        if(selected < 0 || selected > 8){
            cout << "Invalid selection";
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

    int choice = -1;
    string searchTerm;
    searchProduct.searchByName("name");

    /*while(choice!=7){
        choice = productManager.getMenu();
        if(choice == 1){
            cout << "Selected 1";
        }
        else if(choice == 2){
            cout << "Enter product name below:" << endl;

            cin >> searchTerm;

            resultsVector = searchProduct.searchByName(searchTerm);
            searchProduct.showSearchResult(resultsVector, searchTerm);
        }
        else if(choice == 3){
            cout << "Selected 3";
        }
        else if(choice == 4){
            cout << "Selected 4";
        }
        else if(choice == 5){
            cout << "Selected 5";
        }
        else if(choice == 6){
            cout << "Selected 6";
        }
        else if(choice == 7){
            cout << "Selected 7";
        }
        else{
            cout << "Selected invalid";
        }
    }
*/
    //cout << "Exiting...";
    //return 0;
}


