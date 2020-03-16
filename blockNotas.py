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