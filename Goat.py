# OOP
import csv
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
    def __init__(self, file):
        self.file = file
        self.inventory = load_products(file)
        self.products = [Product(**prod) for prod in self.inventory]

    def display_products(self):
        if not self.products:
            print("No products available.")
            return
        for product in self.products:
            print(product.display_info())

    def save_products(self):
        with open(self.file, 'w') as file:
            fieldnames = ['name', 'price', 'category', 'stock']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for product in self.products:
                writer.writerow({
                    'name': product.name,
                    'price': product.price,
                    'category': product.category,
                    'stock': product.stock
                })

    def add_product(self, name, price, category, stock):
        new_product = Product(name, price, category, stock)
        self.products.append(new_product)
        self.save_products()

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
    def __init__(self, name, preferred_category, SortingAlgorithm=False):
        self.name = name
        self.preferred_category = preferred_category
        self.SortingAlgorithm = SortingAlgorithm

    def choose_product(self, product_manager):
        return product_manager.filter_by_category(self.preferred_category)


def main():
    item = Product_Manager("products.csv")
    user = User("Alice", "Electronics")
    recommended_products = user.choose_product(item)
    print("Recommended Products for", user.name)
    for product in recommended_products:
        print(product.display_info())


if __name__ == "__main__":
    main()
