from dataclasses import dataclass

from model.Products import Product


@dataclass
class CartItem:
    product: Product


