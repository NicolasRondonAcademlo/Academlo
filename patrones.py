
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



# import abc
# class IBuilder(metaclass=abc.ABCMeta):

#     @abc.abstractmethod
#     def build_part_a(self):
#         pass

#     @abc.abstractmethod
#     def build_part_b(self):
#         pass
    
#     @abc.abstractmethod
#     def build_part_c(self):
#         pass
    
#     @abc.abstractmethod
#     def get_result(self):
#         pass
    

# class Product():
#     def __init__(self) -> None:
#         self.parts = []

    

# class Builder(IBuilder):
#     def __init__(self) -> None:
#         self.product = Product()

#     def build_part_a(self):
#         self.product.parts.append("techo")
#         return self
    
#     def build_part_b(self):
#         self.product.parts.append("piscina")
#         return self

#     def build_part_c(self):
#         self.product.parts.append("terraza")
#         return self

#     def get_result(self):
#         return self.product


# class Director:

#     @staticmethod
#     def construct():
#         return Builder().build_part_c().build_part_b().get_result()


# producto_final = Director.construct()
# print(producto_final.parts)


# import abc
# import time
# import copy
# import datetime

# class Prototype(metaclass=abc.ABCMeta):

#     def __init__(self) -> None:
#         time.sleep(3)
#         self.heigt = None
#         self.age = None
#         self.defense = None
#         self.attack  = None

#     @abc.abstractmethod
#     def clone(self):
#         pass


# class ShopKeeper(Prototype):
#     def __init__(self, height, age, defense, attack) -> None:
#         super().__init__()
#         time.sleep(3)
#         self.heigt = height
#         self.age = age
#         self.defense = defense
#         self.attack = attack

#     def clone(self):
#         return copy.deepcopy(self)


# # print("Crear Tendero", datetime.datetime.now().time())
# # shopkeeper = ShopKeeper(1890,232,43,545)
# # print("Finalizo de crear el tendero", datetime.datetime.now().time())


# print("Ejercito de tenderos", datetime.datetime.now().time())
# shopkeeper = ShopKeeper(1890,232,43,545)

# for i in range(10):
#     shopkeeper_clone = shopkeeper.clone()
#     print("Finalizo clonacion del tendero", datetime.datetime.now().time())
# print("Terminamos de crear los tenderos", datetime.datetime.now().time())


# class SoyUnico:
#     __instance = None
#     nombre = None

#     def __str__(self) -> str:
#         return self.nombre

#     def __new__(cls):
#         if SoyUnico.__instance is None:
#             SoyUnico.__instance = object.__new__(cls)
#         return SoyUnico.__instance

# ricardo = SoyUnico()
# ricardo.nombre = "Ricardo Montoya"

# print(ricardo)

# ramon = SoyUnico()
# ramon.nombre = "Ramon Perez"
# print(ramon)
# print(ricardo)

# import abc


# class IA(metaclass=abc.ABCMeta):
#     @abc.abstractmethod
#     def method_a(self):
#          pass


# class A(IA):
#     def method_a(self):
#         print("El metodo a")



# class IB(metaclass=abc.ABCMeta):
#     @abc.abstractmethod
#     def method_b(self):
#          pass


# class B(IB):
#     def method_b(self):
#         print("El metodo b")


# class BAdapter(IA):
#     def __init__(self) -> None:
#         self.b = B()

#     def method_a(self):
#         self.b.method_b()


# item = A()
# item.method_a()

# item = BAdapter()
# item.method_a()


class Observer:
    def __init__(self, observable) -> None:
        observable.subscribe(self)
        

    def notify(self, observable, *args, **kwwargs):
        print("Obtuvo", args, kwwargs, "De", observable)


class Observable:
    def __init__(self) -> None:
        self.__observers = []
    
    def subscribe(self, observer):
        self.__observers.append(observer)
        pass


    def unsuscribe(self, observer):
        self.__observers.remove(observer)
        pass

    def notify_observers(self, *args, **kwargs):
        for obs in self.__observers:
            obs.notify(self, *args, **kwargs)



subject = Observable()

observer1 = Observer(subject)
observer2 = Observer(subject)

subject.notify_observers(
    "Primer cambio" , kw="Por el observador"
)

print("--------------")
subject.unsuscribe(observer2)
subject.notify_observers(
    "Segundo cambio", kw = "Por el observaodr"
)