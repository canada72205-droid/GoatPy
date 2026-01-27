# OOP
from product_reader import load_products
import csv
from abc import ABC, abstractmethod


class Product:
    def __init__(self, name, price, category, stock):
        self.name = name
        self.price = price
        self.category = category
        self.stock = stock
        # logical variables
        self.is_out_of_stock = (self.stock <= 0)
        self.is_high_demand = self.category.lower() in ["electronics", "fashion"]
        self.is_budget_item = self.price < 10.0
        self.should_feature = self.is_high_demand and not self.is_budget_item
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
    
    def add_product(self, product_dict, filename="products.csv"):
        import os
        file_exists = os.path.exists(filename) and os.path.getsize(filename) > 0
        
        if file_exists:
            with open(filename, 'rb+') as f:
                f.seek(-1, os.SEEK_END)
                if f.read(1) != b'\n':
                    f.write(b'\n')

        with open(filename, "a", newline="") as file:
            fieldnames = ["name", "price", "category", "stock"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            
           
            if not file_exists:
                writer.writeheader()
            
            writer.writerow(product_dict)
        print(f"Added {product_dict['name']} to Store")
    
    def edit_product(self, products, filename="products.csv"):
   
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


    def delete_product(self, target_name):
        rows = []
        found = False
        target = target_name.strip().lower()
        with open('products.csv', 'r', newline='') as f:
            reader = csv.DictReader(f)
            fieldnames = reader.fieldnames
            for row in reader:
                
                if row['name'].strip().lower() != target:
                    rows.append(row)
                else:
                    found = True

        if found:
            with open('products.csv', 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(rows)
                
        return found




class SortingAlgorithm(ABC):
    @abstractmethod
    def sort(self, products, key="price"):
        pass

class BubbleSort(SortingAlgorithm):
    def sort(self, products, key='price'):       
        arr = products.copy()        
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                a = getattr(arr[j], key)                
                b = getattr(arr[j+1], key)
                if a > b:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr
    
class SelectionSort(SortingAlgorithm):
    def sort(self, products, key='price'):        
        arr = products.copy()        
        n = len(arr)
        for i in range(n):            
            min_idx = i
            for j in range(i+1, n):                
                a = getattr(arr[j], key)                
                b = getattr(arr[min_idx], key)
                if a < b:                    
                    min_idx = j
                    arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr


class User():
    def __init__(self, name, preferred_category, cart):
        self.name = name
        self.preferred_category = preferred_category
        self.cart = {}
        
    def choose_product(self, product_manager, preferred_category):
        return product_manager.find_by_category(self.preferred_category)
        
    def add_to_cart(self, product_name, price):
        self.cart[product_name] = price
    def view_cart(self):
        if not self.cart:
            print("Your cart is empty")
            return
        
        print("\n--- Your Cart ---")
        total = 0
        for name, price in self.cart.items():
            print(f"{name}: ${price:.2f}")
        total += price
        print(f"Total: ${total:.2f}")

    def remove_from_cart(self, product_name):
        if product_name in self.cart:
            del self.cart[product_name]
            print(f"{product_name} removed from cart")
        else:
            print("Item not in cart")
    