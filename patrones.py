
# import abc

# class Product(metaclass=abc.ABCMeta):
#     @abc.abstractmethod
#     def operation(self):
#         pass


# class ProductA(Product):
#     def operation(self):
#         print("Producto A")
#         return "Producto A"
    

# class ProductB(Product):
#     def operation(self):
#         print("Product B")
#         return "Product B"

# def create_product(creator):
#     creator().operation()


# create_product(ProductA)

# create_product(ProductB)



import abc
class IBuilder(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def build_part_a(self):
        pass

    @abc.abstractmethod
    def build_part_b(self):
        pass
    
    @abc.abstractmethod
    def build_part_c(self):
        pass
    
    @abc.abstractmethod
    def get_result(self):
        pass
    

class Product():
    def __init__(self) -> None:
        self.parts = []

    
class Builder(IBuilder):
    def __init__(self) -> None:
        self.product = Product()

    def build_part_a(self):
        self.product.parts.append("techo")
        return self
    
    def build_part_b(self):
        self.product.parts.append("piscina")
        return self

    def build_part_c(self):
        self.product.parts.append("terraza")
        return self

    def get_result(self):
        return self.product


class Director:

    @staticmethod
    def construct():
        return Builder().build_part_c().build_part_b().get_result()


producto_final = Director.construct()
print(producto_final.parts)