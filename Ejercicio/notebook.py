import datetime

last_id = 0
class Note:
    def __init__(self, memo:str, tags:str="") -> None:
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.datetime.today()
        global last_id
        last_id +=1
        self.id = last_id

    def match(self, filter:str) -> bool:
        return filter in self.memo or filter in self.tags

class Notebook:
    def __init__(self) -> None:
        self.notes = []

    def new_note(self,memo, tags=""):
        self.notes.append(Note(memo, tags))

    def __find_note(self, note_id):
        for note in self.notes:
            if note_id == note.id:
                return note
            return None

    def modify_memo(self,note_id: int, memo:str):
        self.__find_note(note_id).memo = memo
    
    def modify_tags(self, note_id:int, tags:str):
        self.__find_note(note_id).tags = tags


    def search(self, filter:str) -> list:
        return [note for note in self.notes if note.match(filter)]



n = Notebook()
n.new_note("Nota prueba")
print(n.notes[0].memo)
n.modify_memo(1, " Texto que modifique")
print(n.notes[0].memo)