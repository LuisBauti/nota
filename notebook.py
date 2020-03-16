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
