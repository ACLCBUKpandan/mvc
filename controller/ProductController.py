from model.Products import Product


def create_product():
    pass 

def get_products() -> list[Product] :

    return [
        Product(name="Hello", price=12, stocks=10),
        Product(name="Hello", price=12, stocks=10),
        Product(name="Hello", price=12, stocks=10),
    ]

def edit_product(product: Product):
    pass

def delete_product(product: Product):
    pass

