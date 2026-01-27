from Goat import User, Product_Manager, Product
import os

from product_reader import products

def clear_screen():
    
    os.system('cls' if os.name == 'nt' else 'clear')

def print_menu():
    while True:
        clear_screen()
        print("=" * 60)
        print("GOATPY Presents: E-Commerce Product Management")
        print("             and Recommendation System")
        print("=" * 60)
        print()
        print("1. I'm a buyer")
        print("2. I'm a manager")
        print("3. Exit")
        print()
        
        answer = input("Enter choice: ")
        
        if answer == "1":
            name = input("What is your name?: ")
            preferred_category = input("What is your preferred Category?: ")
            current_user = User(name, preferred_category)
            buyer_menu(current_user)
        elif answer == "2":
            manager_menu()
        elif answer == "3":
            print("\nThank you for using GOATPY!")
            break
        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.")
            input("Press Enter to continue...")

def buyer_menu(current_user):
    while True:
        clear_screen()
        print("=== BUYER MENU ===\n")
        print("1. Browse products")
        print("2. Search products")
        print("3. View recommendations")
        print("4. View cart")
        print("5. Purchase Product")
        print("6. Remove from cart")
        print("0. Back to main menu")
        print()
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            for product_dict in products:
               product = Product(
                   product_dict["name"],
                   product_dict["price"],
                   product_dict["category"],
                   product_dict["stock"]
               ) 
               print(product.display_info())
        elif choice == "2":
            search_term = input("what would you like to search for?: ")
            found = False
            for product_dict in products:
                if product_dict["name"].lower() == search_term.lower():
                    product = Product(
                        product_dict['name'],
                        product_dict['price'],
                        product_dict['category'],
                        product_dict['stock']
                    )
                    print(product.display_info())
                    found = True
                    break
            if not found:
                    print("this item was not found")

        elif choice == "3":
            pref = current_user.preferred_category
            found = False
            for product_dict in products:
                if pref == product_dict['category']:
                    product = Product(
                            product_dict['name'],
                            product_dict['price'],
                            product_dict['category'],
                            product_dict['stock']
                        )
                    print(product.display_info())
                    found = True
            if not found:
                print(f"no produts were found under {pref}")
        elif choice == "4":
            current_user.view_cart()
        elif choice == "5":
            item = input("What would you like to purchase?: ")
            found = False
            for product_dict in products:
                if item ==  product_dict['name']:
                    current_user.add_to_cart(
                        product_dict['name'],
                        product_dict['price']
                    )
                    print(f"Added {item} to your cart!")
                    found = True
                    break
            if not found:
                print("Product not found")
        elif choice == "6":
            item = input("which item would you like to discard?: ") 
            current_user.remove_from_cart(item)   
        elif choice == "0":
            break
        else:
            print("\nInvalid choice.")
            input("Press Enter to continue...")

def manager_menu():
    while True:
        clear_screen()
        print("=== MANAGER MENU ===\n")
        print("1. Add product")
        print("2. Update product")
        print("3. Delete product")
        print("4. View all products")
        print("5. View analytics")
        print("0. Back to main menu")
        print()
        
        choice = input("Enter choice: ")
        
        if choice == "1":
           manager = Product_Manager()
           name = input("product name: ")
           price = float(input("price: "))
           category = input("category: ")
           stock = int(input("stock qunatity: "))

           new_product = {
                'name': name,
                'price': price,
                'category': category,
                'stock': stock
            }
           products.append(new_product)
           manager.add_product(new_product)
           print("Product added succesfully")
        elif choice == "2":
            manager = Product_Manager()
            manager.edit_product(products)
            input("\nPress Enter to continue...")
        elif choice == "3":
            manager = Product_Manager()
            manager.delete_product()
        elif choice == "4":
            view_all_products()
        elif choice == "5":
            view_analytics()
        elif choice == "0":
            break
        else:
            print("\nInvalid choice.")
            input("Press Enter to continue...")