class Livro():
    def __init__(self, titulo, paginas):
        self._titulo = titulo.capitalize()
        self._paginas = int(paginas)
        self._ppm = None
        self._tempo_pagina = None
