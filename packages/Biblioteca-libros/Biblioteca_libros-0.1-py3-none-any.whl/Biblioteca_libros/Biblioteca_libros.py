#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Libro:
    def __init__(self, titulo, autor, año_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion
    
    def mostrar_info(self):
        return f"'{self.titulo}' de {self.autor}, publicado en {self.año_publicacion}"

class Autor:
    def __init__(self, nombre, fecha_nacimiento):
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.libros = []
    
    def agregar_libro(self, libro):
        self.libros.append(libro)
    
    def mostrar_libros(self):
        return [libro.mostrar_info() for libro in self.libros]

def mostrar_libros(libros):
    for libro in libros:
        print(libro.mostrar_info())

def mostrar_autores(autores):
    for autor in autores:
        print(f"Autor: {autor.nombre}, Nacido en: {autor.fecha_nacimiento}")
        print("Libros:")
        for libro in autor.mostrar_libros():
            print(f" - {libro}")


# In[ ]:




