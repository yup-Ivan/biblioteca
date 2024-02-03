from datetime import datetime

class Libro:

    def __init__(self, codigo : str, isbn : str, titulo : str, autor : str, anyo_publicacion : datetime, num_paginas : int, genero : str):
        self.codigo = codigo
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.anyo_publicacion = anyo_publicacion
        self.num_paginas = num_paginas
        self.genero = genero

class Biblioteca:
    
    def __init__(self):
        self.libros = []
        self.historial = []

    def agregar_libro(self, libro):
        self.libros.append({"Libro": libro, "prestado" : False})

    def obtener_libro(self, titulo):
        for libro in self.libros:
            if 'Libro' in libro and libro['Libro'].titulo == titulo:
                return libro['Libro']
        return None

    def buscar_libro(self, criterio, valor):
        def tu_libro(dict_libro):
            fecha = dict_libro['anyo_publicacion'].strftime('%d/%m/%Y')
            return f"\nCodigo: {dict_libro['codigo']}\nISBN: {dict_libro['isbn']}\nTITULO: {dict_libro['titulo']}\nAUTOR: {dict_libro['autor']}\nAÑO DE PUBLICACIÓN: {fecha}\nNUM_PAGINAS: {dict_libro['num_paginas']}\nGENERO: {dict_libro['genero']}"

        for libro in self.libros:
            dict_libro = vars(libro['Libro'])
            if criterio in dict_libro:
                if (dict_libro[criterio]) == valor:
                    return (f"\nSe ha encontrado el libro (Criterio: {criterio}, Valor: {valor}): {tu_libro(dict_libro)}\n")
            else:
                return ("Has introducido un criterio incorrecto, usa uno de los siguientes: 'titulo', 'autor', 'genero'.")
            
        return f"No se ha encontrado el libro con el criterio: {criterio}: {valor}."

    def mostrar_libros(self):
        print("\nLibros disponibles:")
        for libro in self.libros:
            if 'Libro' in libro:
                print(f"Código: {libro['Libro'].codigo}, Título: {libro['Libro'].titulo}")
            

    def prestar(self, libro_solicitado, lector):
        for libro in self.libros:
            if libro['Libro'] == libro_solicitado:
                if libro['prestado'] == True:
                    return "El libro solicitado ya ha sido prestado."

                libro['prestado'] = True
                self.historial.append((libro_solicitado.titulo, lector, datetime.now(), None))
                return f'Se ha prestado el libro {libro_solicitado.titulo} a {lector}.'

        return "El libro no está disponible en la biblioteca."

    def devolver(self, libro_solicitado):
        for libro in self.libros:
            if libro['Libro'] == libro_solicitado:
                if libro['prestado'] == False:
                    return "El libro no está prestado."

                libro['prestado'] = False
                for index, prestamo in enumerate(self.historial):
                    if prestamo[0] == libro_solicitado.titulo and prestamo[3] is None:
                        self.historial[index] = (prestamo[0], prestamo[1], prestamo[2], datetime.now())
                        return f'Se ha devuelto el libro {libro_solicitado.titulo}.'

        return "No se pudo realizar la devolución."

    def historial_prestamos(self):
        return self.historial

    def baja_libro(self, libro_baja):
        for index, libro in enumerate(self.libros):
            if libro['Libro'] == libro_baja:
                del self.libros[index]
                return f'El libro {libro_baja.titulo} se ha dado de baja.'
        return 'El libro no existe.'