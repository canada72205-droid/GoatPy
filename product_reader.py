import csv

def load_products(csv_file = 'products.csv'):
        products = [] 
        # Implementation for loading products from CSV
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                products.append(
                    {
                        'name': row['name'],
                        'price': float(row['price']),
                        'category': row['category'],
                        'stock': int(row['stock'])
                    }
                )             
        return products
products = load_products()