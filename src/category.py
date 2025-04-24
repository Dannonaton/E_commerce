from src.product import Product


class Category:
    """Категория товара"""
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)
        print(Category.product_count)

    def add_product(self, product: dict):
        """Метод добавления нового продукта в список"""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products(self) -> str:
        product_list = ""
        for product in self.__products:
            product_list += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт. \n "
        return product_list