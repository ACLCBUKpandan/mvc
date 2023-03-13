from model.Products import Product
from controller.ProductController import get_products

def display_products():
    products = get_products()

    for itx, i in products:
        print(f'{itx} {i.name} {i.price} x{i.stocks}')

