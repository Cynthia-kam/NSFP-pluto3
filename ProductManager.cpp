#include "SearchProduct.cpp"

class ProductManager
{
private:
    Product prod;
public:
    int getMenu(){
        cout<<"Menu:"<<endl;
        cout<<"1. Add product"<<endl;
        cout<<"2. Search Product By Name"<<endl;
        cout<<"3. Search Product By Category"<<endl;
        cout<<"4. Product By Brand"<<endl;
        cout<<"5. Update Product"<<endl;
        cout<<"6. Delete Product"<<endl;
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
    SearchProduct searchProduct;
    searchProduct.searchByName("name");
}


