from product_reader import load_products
from typing import List, Dict


def recommendation() -> List[Dict]:

    products = load_products()
    recommendations: List[Dict] = []
    for p in products:
        try:
            price = float(p.get('price', 0))
            stock = int(p.get('stock', 0))
        except (TypeError, ValueError):
            # This just ignores if someone puts the price or stock wrong
            continue

        if price < 50.00 and stock > 0:
            recommendations.append(p)

    return recommendations


if __name__ == "__main__":
    recs = recommendation()
    if not recs:
        print("No recommendations found")
    else:
        print("Recommendations:")
        for prod in recs:
            print(
                f"- {prod['name']}: ${prod['price']} ({prod['stock']} in stock) - {prod['category']}")
