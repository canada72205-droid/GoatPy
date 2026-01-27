# OOP
from product_reader import load_products
import csv


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
        
    
    def find_by_category(self, category):
        return [p for p in self.products if p.category == category]

    def display_products(self):
        for product in self.products:
            print(product.display_info())
    
    def add_product(product_dict, filename="products.csv"):
        import os
    
   
        file_exists = os.path.exists(filename) and os.path.getsize(filename) > 0
        
        with open(filename, "a", newline="") as file:
            fieldnames = ["name", "price", "category", "stock"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            
           
            if not file_exists:
                writer.writeheader()
            
            writer.writerow(product_dict)
        print(f"Added {product_dict['name']} to Store")
    
    def edit_product(products, filename="products.csv"):
   
        product_name = input("Enter the product name to edit: ")
    
        found = False
        for product in products:
            if product['name'].lower() == product_name.lower():
                found = True
                
                print(f"\nEditing: {product['name']}")
                print("(Press Enter to keep current value)")
                
                new_name = input(f"New name [{product['name']}]: ")
                new_price = input(f"New price [${product['price']}]: ")
                new_category = input(f"New category [{product['category']}]: ")
                new_stock = input(f"New stock [{product['stock']}]: ")
                
                if new_name:
                    product['name'] = new_name
                if new_price:
                    product['price'] = float(new_price)
                if new_category:
                    product['category'] = new_category
                if new_stock:
                    product['stock'] = int(new_stock)
                
                with open(filename, 'w', newline='') as file:
                    fieldnames = ['name', 'price', 'category', 'stock']
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(products)
                
                print("\nProduct updated successfully!")
                break
        
        if not found:
            print("Product not found")


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


class User():
    def __init__(self, name, preferred_category):
        self.name = name
        self.preferred_category = preferred_category
        
    def choose_product(self, product_manager, preferred_category):
        return product_manager.find_by_category(self.preferred_category)
        
    def add_to_cart(self, product_name, price):
        self.cart.append({
            'name': product_name,
            'price': price
        })
    def view_cart(self):
        if not self.cart:
            print("Your cart is empty")
            return
        
        print("\n--- Your Cart ---")
        total = 0
        for item in self.cart:
            print(f"{item['name']}: ${item['price']:.2f}")
            total += item['price']
        print(f"Total: ${total:.2f}")

    def remove_from_cart(self, product_name):
        if product_name in self.cart:
            del self.cart[product_name]
            print(f"{product_name} removed from cart")
        else:
            print("Item not in cart")
    