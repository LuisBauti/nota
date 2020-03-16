# -*- coding: utf8 -*-
from nota import Note

class Notebook:
    """
    Representa una colección de notas que pueden ser
    etiquetadas, modificadas y buscadas.
    """

    def __init__(self):
        """ Inicializa una libreta vacía """
        self.notes = list()

    def new_note(self, memo, tags=""):
        """ Crea una nueva nota y la agrega a la libreta """
        self.notes.append(Note(memo, tags))

    def _search_note(self, note_id):
        """
        Busca una nota con el id enviado.
        Esta función es privada (empieza con _).
        https://docs.python.org/2/tutorial/classes.html
        """
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note

        return None
