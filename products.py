# type: ignore
class InventoryError(Exception):
    """Custom exception for inventory-related errors.

    Args:
        Exception (BaseException): The base exception class.
    """


class Product:
    """A class representing a product in the store."""

    def __init__(self, name: str, price: float, quantity: int):
        """Initialize a Product instance.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.
            quantity (int): The quantity of the product.

        Raises:
            ValueError: If any of the parameters are invalid.
        """
        if name == "":
            raise ValueError("Product name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be of negative value.")
        if quantity < 0:
            raise ValueError("Quantity cannot be of negative value.")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True


    def get_quantity(self) -> int:
        """Get the quantity of the product.
        Args:
            None
        Returns:
            int: The quantity of the product.
        """
        return self.quantity


    def set_quantity(self, quantity: int) -> None:
        """Set the quantity of the product.

        Args:
            quantity (int): The new quantity of the product.

        Returns:
            None

        Raises:
            ValueError: If the quantity is negative.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.active = False


    def is_active(self) -> bool:
        """Check if the product is active.

        Args:
            None

        Returns:
            bool: True if the product is active, False otherwise.
        """
        return self.active


    def activate(self) -> None:
        """Activate the product.

        Args:
            None

        Returns:
            None
        """
        self.active = True


    def deactivate(self) -> None:
        """Deactivate the product.
        Args:
            None

        Returns:
            None
        """
        self.active = False


    def show(self) -> None:
        """Display the product details.

        Args:
            None

        Returns:
            None
        """
        return f"{self.name}, Price($): {self.price}, Quantity: {self.quantity}"


    def buy(self, quantity: int) -> float:
        """Buy a quantity of the product.

        Args:
            quantity (int): The quantity of the product to buy.

        Raises:
            ValueError: If the quantity is not valid.
            InventoryError: If there is not enough inventory to fulfill the purchase.

        Returns:
            float: The total price of the purchase.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        if not self.is_active():
            raise InventoryError(f"The product {self.name} is not available for purchase.")

        if self.quantity < quantity:
            raise InventoryError(f"{quantity} items requested, but {self.quantity} "
                                 f"units of {self.name} are available for purchase.")
        price = quantity * self.price
        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()
        return price
