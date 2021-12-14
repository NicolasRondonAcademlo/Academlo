from notebook import Notebook
import sys
class Menu:
    def __init__(self) -> None:
        self.notebook = Notebook()
        self.choices = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_notes,
            "4": self.modify_notes,
            "5": self.quit
        }

    def run(self):
        while True:
            self.display_menu()
            choice = input( "Ingresa una opcion")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{choice} esta no es una opcion valida")

    def display_menu(self):
        print(
            """
            Menu de libreta
            1. Mostrar todas las notas
            2. Buscar Notas
            3. Añadir Notas
            4. Modificar Notas
            5. Salir
            """
        )

    def show_notes(self, notes=None):
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print(f"{note.id} {note.memo} {note.tags}")
    
    def search_notes(self):
        filter = input("Buscar por: ")
        notes = self.notebook.search(filter)
        self.show_notes(notes)

    def add_notes(self):
        memo = input("Ingresa un recordatorio: ")
        self.notebook.new_note(memo)
        print("Tu nota fue añadida")
    
    def modify_notes(self):
        id = input("Ingresa el id de la nota: ")
        memo = input("Ingresa el recordatorio")
        tags = input("Ingresa las etiquetas")
        if memo:
            self.notebook.modify_memo(id, memo)
        if tags:
            self.notebook.modify_tags(id, tags)
    
    def quit(slef):
        print("gracias por usar tu libreta")
        sys.exit(0)

Menu().run()