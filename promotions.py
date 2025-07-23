from abc import ABC, abstractmethod

class PromotionError(Exception):
    """Raised when a promotion cannot be applied to a product or order."""
    pass

class Promotion(ABC):
    """An abstract class outlining promotion functionality"""

    @abstractmethod
    def apply_promotion(product, quantity) -> float:
       pass

class SecondHalfPrice(Promotion):
    """A class representing the second-half-price promotion"""

    def __init__(self, name: str):
        self.name = name

    
    def apply_promotion(product, quantity: int) -> float:
        """Applies promotion if eligible.

        Args:
            product: The product to apply the promotion on.
            quantity(int): The quantity of products.

        Returns:
            float: The total price after discount.
            
        Raises:
            PromotionError: If purchase is not eligible for promotion.
        """
        if quantity < 2:
            raise PromotionError("Cannot apply Promotion if quantity is less than two.")
        eligible_promotion_times = quantity // 2
        reminder_times = quantity % 2

        promoted_price = product.price * eligible_promotion_times * 1.5
        remainder_price = product.price * reminder_times
        
        total_price = promoted_price + remainder_price
        return total_price



class ThirdOneFree(Promotion):
    """A class representing the second-half-price promotion"""
    pass

class PrecentDiscount(Promotion):
    """A class representing the second-half-price promotion"""
    pass
