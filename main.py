from funciones.biblioteca import *

class MenuUsuario:

    def __init__(self):
        self.biblioteca_altabix = Biblioteca()

    def agregar_libro(self):
        self.codigo = input("Introduce el código del libro: ")
        self.isbn = input("Introduce el ISBN del libro: ")
        self.nombre = input("Introduce el nombre del libro: ")
        self.autor = input("Introduce el nombre del autor del libro: ")
        self.paginas = int(input("Introduce la cantidad de paginas que tiene el libro: "))
        self.genero = input("Introduce el genero del libro: ")

        self.biblioteca_altabix.agregar_libro(Libro(self.codigo, self.isbn, self.nombre, self.autor, datetime(2020, 10, 25), self.paginas, self.genero))

    def mostrar_libros(self):
        self.biblioteca_altabix.mostrar_libros()

    def buscar_libro(self):
        criterio = input("Introduce el criterio de búsqueda (titulo, autor, isbn, genero): ")
        valor = input("Introduce el valor a buscar: ")
        print(self.biblioteca_altabix.buscar_libro(criterio, valor))
    
    def prestar_libro(self):
        ellibro = self.biblioteca_altabix.obtener_libro(input('Introduce el titulo del libro a prestar: '))
        print(self.biblioteca_altabix.prestar(ellibro, input('Introduce el nombre del lector: ')))

    def devolver_libro(self):
        ellibro = self.biblioteca_altabix.obtener_libro(input('Introduce el titulo del libro a devolver: '))
        print(self.biblioteca_altabix.devolver(ellibro))

    def mostrar_historial_prestamos(self):
        datos_historial = self.biblioteca_altabix.historial_prestamos()
        for dato in datos_historial:
            print(f'Titulo: {dato[0]}\nLector: {dato[1]}\nFecha Prestamo: {dato[2].strftime("%d/%m/%Y %H:%M:%S:%f")}\nFecha Devolución: {dato[3].strftime("%d/%m/%Y %H:%M:%S:%f")}\n')

    def mostrar_menu(self, opcion=""):
        while opcion != '7':
            print("\n--- Menú de Usuario ---\n1. Agregar libro\n2. Mostrar libros\n3. Buscar libro\n4. Prestar libro\n5. Devolver libro\n6. Mostrar historial de préstamos\n7. Salir")
            
            match input("Ingrese una opción: "):
                case '1':
                    self.agregar_libro()
                case '2':
                    self.mostrar_libros()
                case '3':
                    self.buscar_libro()
                case '4':
                    self.prestar_libro()
                case '5':
                    self.devolver_libro()
                case '6':
                    self.mostrar_historial_prestamos()
                case '7':
                    print("Saliendo del menú de usuario...")
                case _:
                    print("Seleccione una opción válida.")

MenuUsuario().mostrar_menu()