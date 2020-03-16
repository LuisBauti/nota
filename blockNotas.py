# -*- Coding: UTF-8 -*-
# Programa: BAndeja de mensajes
# objetivo: Su funcion es recibir, notificar y revidsar los mensajes.
# Autor: Luis Enrique Consuegra
# Fecha: 12/3/2020

import sys
import plataform
from notebook import Notebook

class Menu:
    """
    Despliega un menú que responde a las elecciones del usuario.
    """
    def __init__(self):
        self.notebook = Notebook()
        self.options = {"1": self.show_notes,
                        "2": self.search_notes,
                        "3": self.add_note,
                        "4": self.modify_note,
                        "5": self.exit}

    def display_menu(self):
         """ Despliega el menú principal """
         print("""
                Menú principal

                1. Mostrar todas las notas
                2. Buscar nota
                3. Agregar una nota
                4. Modificar una nota
                5. Salir
                """)

    def show_notes(self, notes=None):
        """ Despliega una nota """
        if not notes:
            notes = self.notebook.notes

        for note in notes:
            print("Id: {0}\nEtiquetas: '{1}'\nContenido: {2}\nFecha: {3}"
                  .format(note.id, note.tags, note.memo, note.creation_date))

    def search_notes(self):
        """ Busca una nota mediante un filtro """
        filter = input("Ingresa el texto de búsqueda: ")
        note = self.notebook.search(filter)
        self.show_notes(note)

    def add_note(self):
        memo = input("Ingrese el contenido de la nota: ")
        tags = input("Etiquetas para la nota separadas por espacio: ")
        self.notebook.new_note(memo, tags)
        print("¡Nueva nota agregada!")

    def modify_note(self):
        pass

    def exit(self):
        """ Cierra la aplicación """
        print("Gracias por utilizar su libreta el día de hoy")
        sys.exit(0)

if __name__ == "__main__":
    menu = Menu()
    menu.run()
