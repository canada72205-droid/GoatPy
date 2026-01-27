from product_reader import load_products


def binary_search(sequence, item):
    low = 0
    high = len(sequence) - 1

    while low <= high:
        mid = (low + high) // 2
        midpoint_value = sequence[mid]

        if midpoint_value == item:
            return mid
        if midpoint_value > item:
            high = mid - 1
        else:
            low = mid + 1

    return None


def main() -> int:
    # Load products
    products = load_products()
    # The prices from the products
    data = sorted([p['price'] for p in products])

    try:
        wanted_price = input("Enter a price to search (e.g. 19.99): ")
        target = float(wanted_price)
    except ValueError:
        print("Invalid input: please enter a numeric price (for example: 19.99)")
        return 1

    result = binary_search(data, target)
    if result is not None:
        print(f"Price {target} found at index: {result}")
    else:
        print(f"Price {target} not found")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
