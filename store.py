import products

Product = products.Product

class Store:
    """A class representing a store that holds products."""

    def __init__(self, products_list: list):
        """Initialize the store with a list of products.
        Args:
            products (list): A list of Product objects.
        """
        self.list_of_products = list(products_list)


    def add_product(self, product: Product) -> None:
        """Add a product to the store.
        Args:
            product (Product): The product to be added.
        """
        self.list_of_products.append(product)


    def remove_product(self, product: Product) -> None:
        """Remove a product from the store.
        Args:
            product (Product): The product to be removed.
        Returns:
            None
        Raises:
            products.InventoryError: If the product is not found in the store."""
        if product in self.list_of_products:
            self.list_of_products.remove(product)
        else:
            raise products.InventoryError("The store does not hold this product.")


    def get_total_quantity(self) -> int:
        """Get the total quantity of all productsin the store.
        Returns:
            int: The total quantity of all products.
        Raises:
            products.InventoryError: If there are no products in the store.
        """
        if not self.list_of_products:
            raise products.InventoryError("No products available in the store.")
        return sum(product.get_quantity() for product in self.list_of_products)


    def get_all_products(self) -> list:
        """Get a list of all products in the store.
        Returns:
            list: A list of all active products.
        Raises:
            products.InventoryError: If there are no products in the store.
        """
        active_products = [product for product in self.list_of_products if product.is_active()]
        if not active_products:
            raise products.InventoryError("No active products available in the store.")
        return active_products


    @staticmethod
    def order(shopping_list: list[tuple[Product, int]]) -> float:
        """Process an order from the shopping list.
        Args:
            shopping_list (list): A list of tuples where each tuple
            contains a Product and the quantity to buy.
        Returns:
            float: The total price of the order.
        Raises:
            products.InventoryError: If a product is not available in sufficient quantity.
        """
        if not shopping_list:
            raise ValueError("Shopping list cannot be empty.")
        if not all(isinstance(item, tuple)
                   and len(item) == 2
                   and isinstance(item[0], Product)
                   and isinstance(item[1], int) for item in shopping_list):
            raise TypeError("Shopping list must contain tuples of (Product, quantity).")
        return sum(product.buy(quantity) for product, quantity in shopping_list)
