"""
class MyFirstClass:
    pass

a = MyFirstClass()
b = MyFirstClass()
print(a)
print(b)
"""

# Añadir algunos atributos -> DATOS
"""
class Point:
    pass

p1 = Point()
p2 = Point()
print(p1,p2)

p1.x = 5
p1.y = 6

p2.x = 3
p2.y = 6

print(p1.x, p1.y, p2.x, p2.y)
"""
#<object>.<atritute> = <value>
"""
class Point:
    def reset(self):
        self.x = 0
        self.y = 0

p = Point()
p.reset()
print(p.x, p.y)
"""
"""
class Point:
    def reset(marta):
        marta.x = 0
        marta.y = 0

p = Point()
p.reset()
print(p.x, p.y)
"""
# class Point:
#     def reset(self):
#         self.x = 0
#         self.y = 0

# print(Point.reset())  # No funciona porque no esta instanciada

# class Point:
#     def reset(self):
#         self.x = 0
#         self.y = 0

# p = Point()
# print(Point.reset(p))
# print(p.x, p.y)
# import math
# class Point:
#     def move(self, x, y):
#         self.x = x
#         self.y = y

#     def reset(self):
#         self.x = 0
#         self.y = 0

#     def calculate_distance(self, other_point):
#         return math.sqrt(
#             (self.x -other_point.x)**2
#             + (self.y- other_point.y)**2
#         )
# p1 = Point()
# p2 = Point()
# p1.reset()
# p2.move(5,0)
# print(p2.x, p2.y)
# distance_between_p1_p2 = p1.calculate_distance(p2)
# print(int(distance_between_p1_p2), "Esta es la distancia entre mis puntos")
# try:
#     print(p2.z)
# except AttributeError:
#     print("haz algo")

# class Point:
#     """
#     Representa un punto en dos dimensiones
#     """
#     def __init__(self, x, y) -> None:
#         self.move(x,y)

#     def move(self,x,y):
#         """....."""
#         self.x = x
#         self.y = y

#     def reset(self):
#         """......."""
#         self.move(0,0)

# point = Point(3,4)
# print(point.x, point.y)

# QUIEN PUEDE ACCEDER A NUESTROS DATOS

# class SecretString:
#     def __init__(self, plain_string:str, pass_prhase:str) -> None:
#         self.__plain_string = plain_string
#         self.__pass_phrase = pass_prhase

#     def decrypt(self, pass_phrase:str) -> str:
#         if pass_phrase == self.pass_phrase:
#             return self.plain_string
#         else:
#             return ""
#     def __private(self):
#         pass

# secret_string = SecretString("ACME: Top Secret", "qwerty")
# # print(secret_string.decrypt("qwerty"))
# # print(secret_string.__plain_string)
# print(secret_string._SecretString__plain_string)