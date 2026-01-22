# OOP
from product_reader import load_products


class Product:
    def __init__(self, name, price, category, stock):
        self.name = name
        self.price = price
        self.category = category
        self.stock = stock

    def display_info(self):
        return f"Product Name: {self.name}, Price: ${self.price:.2f}, Category: {self.category}, Stock: {self.stock}"


# Product_Manager: responsible for loading product data from CSV , displaying products, searching and filtering
class Product_Manager:
    def __init__(self, ):
        raw_product = load_products()
        self.products = [Product(**prod) for prod in raw_product]
        
    #def load_products(self, csv_file = 'products.csv'):
        # Implementation for loading products from CSV
  #      with open(csv_file, 'r') as file:
    #        reader = csv.DictReader(file)
     #       for row in reader:
      #          product = Product(
       #             name=row['name'],
        #            price=float(row['price']),
         #           category=row['category'],
          #          stock=int(row['stock'])
            #    )
           #     self.products.append(product)
    
    def find_by_category(self, category):
        return [p for p in self.products if p.category == category]

    def display_products(self):
        for product in self.products:
            print(product.display_info())

# SortingAlgorithm: responsible for sorting products based on different criteria


class SortingAlgorithm:
    @staticmethod
    def sort_by_price(products, ascending=True):
        return sorted(products, key=lambda x: x.price, reverse=not ascending)

    @staticmethod
    def sort_by_name(products):
        return sorted(products, key=lambda x: x.name)

    @staticmethod
    def sort_by_stock(products, ascending=True):
        return sorted(products, key=lambda x: x.stock, reverse=not ascending)

# Add Product


def add_product(product_manager, name, price, category, stock):
    new_product = Product(name, price, category, stock)
    product_manager.products.append(new_product)

# Delete Product


def delete_product(product_manager, product_name):
    product_manager.products = [
        p for p in product_manager.products if p.name != product_name]

# Search Product by name


def search_product(product_manager, search_term):
    return [p for p in product_manager.products if search_term.lower() in p.name.lower()]

# Search Product by category


def filter_by_category(product_manager, category):
    return [p for p in product_manager.products if p.category.lower() == category.lower()]

# Search Product based on logical conditions


def search_with_conditions(product_manager, condition_func):
    return [p for p in product_manager.products if condition_func(p)]

class User():
    def __init__(self, name, preferred_category, SortingAlgorithm=False):
        self.name = name
        self.preferred_category = preferred_category
        self.SortingAlgorithm = SortingAlgorithm
    
    def choose_product(self, product_manager):
        return product_manager.find_by_category(self.preferred_category)
    

def main():
    item = Product_Manager()
    user = User("Alice", "Electronics")
    recommended_products = user.choose_product(item)
    print("Recommended Products for", user.name)
    for product in recommended_products:
        print(product.display_info())   
if __name__ == "__main__":
    main()