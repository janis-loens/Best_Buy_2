
import sys
from products import Product, InventoryError
import store


def pause() -> None:
    """Pause the program to give the user time to read.

    Args:
        None

    Returns:
        None
    """
    input("\nPress Enter to continue.\n")


def print_products(products: list) -> None:
    """Print the details of each product in the list.

    Args:
        products (list): A list of Product objects.

    Returns:
        None
    """
    for index, product in enumerate(products):
        print(f"{index+1}. {product.show()}")

def handle_order(store_instance, products: list) -> None:
    """Handle the order process for the store.
    Args:
        store_instance (store.Store): The store instance to process the order.
        products (list): A list of available products in the store.
    """
    total_price = 0.0
    while True:
        product_choice = input("Select the product number of the item that you want (0 if none): ")
        if product_choice.isdigit():
            product_choice = int(product_choice)
            if product_choice == 0:
                break
            if 1 <= product_choice <= len(products):
                selected_product: Product = products[product_choice - 1]
                quantity_input = input("Enter the quantity: ")
                try:
                    quantity = int(quantity_input)
                    if quantity <= 0:
                        print("Please enter a quantity greater than zero.")
                        continue
                except ValueError:
                    print("Please enter a valid number for quantity.")
                    continue

                try:
                    price = store_instance.order([(selected_product, quantity)])
                    print(f"{quantity} units of {selected_product.name} added to list.")
                    print()
                    total_price += price
                except InventoryError as inventory_error:
                    print(inventory_error)
                    pause()
            else:
                print("\nThe selected product number is invalid.\n")

        else:
            print("Please enter a valid product number.")
    if total_price > 0:
        print(f"\nOrder made! The total payment is: ${total_price:.2f}")


def start(store_instance: store.Store) -> None:
    """Start the Best Buy store application.
    Providing a menu for the user to interact with the store.

    Args:
        store (store.Store): The store instance to run the application on.

    Returns:
        None
    """
    while True:
        try:
            products = store_instance.get_all_products()
        except InventoryError as inventory_error:
            print()
            print(f"{inventory_error}")
            print("Exiting the application.")
            break
        store_menu = input("""
        Store Menu
    ----------
    1. List all products in store
    2. Show total amount in store
    3. Make an order
    4. Quit
                           
    Please choose a number: """)
        print()
        if store_menu == "1":
            print()
            print_products(products)
            pause()
        elif store_menu == "2":
            print()
            print(f"There is a total of {store_instance.get_total_quantity()} "
                  f"products in the store.")
            pause()
        elif store_menu == "3":
            print()
            print_products(products)
            print()
            handle_order(store_instance, products)
            pause()

        elif store_menu == "4":
            if input("Are you sure you want to quit? (y/n): ").lower() == "y":
                print("Thank you for visiting Best Buy!")
                print("Goodbye!")
                sys.exit()
        else:
            print("Invalid choice. Please try again.")
            pause()

if __name__ == "__main__":
    # Initialize the store with some products
    product_list = [ Product("MacBook Air M2", price=1450, quantity=100),
                 Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 Product("Google Pixel 7", price=500, quantity=250)
               ]
    best_buy = store.Store(product_list)

    start(best_buy)
