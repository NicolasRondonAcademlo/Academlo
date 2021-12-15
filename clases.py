import abc
class ConnectionDatabase(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def insert(self, data):
        pass
    
    @abc.abstractmethod
    def delete(self):
        pass
    
    @abc.abstractmethod
    def update(self):
        pass

    @abc.abstractmethod
    def select(self):
        pass

class FirestoreDatabse(ConnectionDatabase):
    def insert(self, data):
        print("inserta")
        return
    
    def select(self):
        print("Selecciona")
        return

    def update(self):
        print("Actualiza")
        return

    def delete(self):
        print("borrar")

class MysqlDatabase(ConnectionDatabase):
    def insert(self, data):
        print("inserta")
        return
    
    def select(self):
        print("Selecciona")
        return

    def update(self):
        print("Actualiza")
        return

    def delete(self):
        print("borrar")

class DynamoDatabase(ConnectionDatabase):
    def insert(self, data):
        print("inserta")
        return
    
    def select(self):
        print("Selecciona")
        return

    def update(self):
        print("Actualiza")
        return

    def delete(self):
        print("borrar")

class User:
    def __init__(self) -> None:
        db = DynamoDatabase()
    def insert_user(self,user):
        self.db.insert(user, data)