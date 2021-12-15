
# from typing import Match


# class Contact:
#     all_contact = []

#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#         self.all_contact.append(self)

# class Supplier(Contact):
#     def order(self, order):
#         print(f"la orden numero {order} fue enviada a {self.name}")

# # c = Contact("Jose", "jose@example.com")
# # print(c.name, c.email)
# # s = Supplier("Alejandra", "aleja@example.co")
# # print(s.name, s.email)

# # class ExtendList(list):
# #     def search(self):
# #         lista_buscar = []
# #         for i  in self:
# #             if i in self and i == 1:
# #                 lista_buscar.append(i)
# #         return lista_buscar

# # lista_prueba = ExtendList([1,2,3,4])
# # print(lista_prueba.search(), "lista prueba")

# class ContactList(list):
#     def search(self, name):
#         match_contacts = []
#         for contact in self:
#             if name in contact.name:
#                 match_contacts.append(contact)
#         return match_contacts


# class Contact:
#     all_contact = ContactList()

#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#         self.all_contact.append(self)

# c1 = Contact("pepito", "pepito@perez.co")
# c2 = Contact("Mariana", "mariana@gmail.co")

# contacts = [c.name for c in c2.all_contact.search("pepito")]
# print(contacts)

# dict
# Ejercicio, encontrar la llave mas larga del diccionario
# class LongNameDict(dict):
#     def longest_key(self):
#         longest = None
#         for key in self:
#             if not longest or len(key) > len(longest):
#                 longest = key
#         return longest

# long_keys = LongNameDict()
# long_keys["llave"] = 2
# long_keys["Llave larga"] = 54
# print(long_keys["llave"])
# print(long_keys.longest_key())

# if [] == list:
#     pass


# if isinstance({}, list):
#     print("Has lo quesea")
#     pass

# PEP8

class Contact:
    all_contact = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.all_contact.append(self)

class Friend(Contact):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.all_contact.append(self)
        self.phone = phone



class Friend(Contact):
    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.phone = phone

amigo = Friend("Victor", "email@email.co", "3208039305")
print(amigo.email, amigo.phone, amigo.name)

# MULTIHERENCIA
"""
Si crees que necesitas multiherencia probablemente te equivocas,
si sabes que lo necesitas entonces probablemente estes en lo correcto
"""
# Mixins 

class MailSender:
    def send_email(self):
        print("Enviar un email " + self.email)

class EmailableContact(Contact, MailSender):
    pass

contact_email = EmailableContact("jon", "jon@gmail.com")
contact_email.send_email()