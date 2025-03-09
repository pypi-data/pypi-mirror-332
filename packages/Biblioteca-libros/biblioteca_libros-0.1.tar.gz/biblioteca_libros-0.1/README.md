# Biblioteca Libros

Una biblioteca simple en Python para gestionar **libros** y **autores**. Permite agregar libros a autores, mostrar información de los libros y autores, y más.

## Instalación

Puedes instalar la biblioteca usando **pip**:

pip install Biblioteca_libros

## Uso

Una vez que la biblioteca está instalada, puedes usarla en tu código de la siguiente manera:

## Ejemplo de uso:

from biblioteca_libros import Libro, Autor, mostrar_libros, mostrar_autores

### Crear autores
autor = Autor("Isabel Allende", "1942")
autor2 = Autor("Gabriel García Márquez", "1927")

### Crear libros
libro1 = Libro("La casa de los espíritus", autor.nombre, 1982)
libro2 = Libro("Cien años de soledad", autor2.nombre, 1967)

### Agregar libros a autores
autor.agregar_libro(libro1)
autor2.agregar_libro(libro2)

### Mostrar libros y autores
print("\n📚 Libros:")
mostrar_libros([libro1, libro2])

print("\n👩‍🏫 Autores:")
mostrar_autores([autor, autor2])

## Salida esperada:

📚 Libros:
'La casa de los espíritus' de Isabel Allende, publicado en 1982
'Cien años de soledad' de Gabriel García Márquez, publicado en 1967

👩‍🏫 Autores:
Autor: Isabel Allende, Nacido en: 1942
Libros:
 - 'La casa de los espíritus' de Isabel Allende, publicado en 1982

Autor: Gabriel García Márquez, Nacido en: 1927
Libros:
 - 'Cien años de soledad' de Gabriel García Márquez, publicado en 1967

## Licencia

Este proyecto está bajo la MIT License. Consulta el archivo LICENSE para más detalles.
