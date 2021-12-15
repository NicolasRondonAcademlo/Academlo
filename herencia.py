
from typing import Match


class Contact:
    all_contact = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.all_contact.append(self)

class Supplier(Contact):
    def order(self, order):
        print(f"la orden numero {order} fue enviada a {self.name}")

# c = Contact("Jose", "jose@example.com")
# print(c.name, c.email)
# s = Supplier("Alejandra", "aleja@example.co")
# print(s.name, s.email)

class ContactList(list):
    def search(self, name):
        match_contacts = []
        for contact in self:
            if name in contact.name:
                match_contacts.append(contact)
        return match_contacts


class Contact:
    all_contact = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.all_contact.append(self)

c1 = Contact("pepito", "pepito@perez.co")
c2 = Contact("Mariana", "mariana@gmail.co")

contacts = [c.name for c in c2.all_contact.search("pepito")]
print(contacts)