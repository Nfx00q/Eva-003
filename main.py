from lib import *
import time
listado_libros: list[any] = []
import random as rn

ciclo = True
isesp = ''
def grabarLibro(listado_libros):

    lib = Libro()

    c = False
    while c == False:
        c = lib.setCodigo(input("Ingrese codigo del libro (AAA-000) -> "))

    lib.titulo = input("Ingrese el titulo del libro -> ")
    lib.autor = input("Ingrese el autor del libro -> ")
    lib.pais = input("Ingrese el país del autor -> ")
    lib.categoria = input("Ingrese la categoria del libro -> ")

    c = False
    while c == False:
        c = lib.setAnio_publicacion(int(input("Ingrese el año de publicación del libro -> ")))

    c = False
    while c == False:
        c = lib.setPrecio(int(input("Ingrese el precio del libro -> ")))

    esp = input("¿Es especial el libro? S/N -> ")
    if esp == 'S' or esp == 's':
        lib.especial = True
    else:
        lib.especial = False

    listado_libros.append(lib)
    print("Libro agregado correctamente...")
    time.sleep(2)


def buscarLibro(listado_libros):
    cod = input("Inserte el codigo del libro a buscar -> ")
    for lib in listado_libros:
        if lib.codigo == cod:
            if lib.especial == True:
                print(f"Nombre libro: {lib.titulo} \t\t Autor: {lib.autor} \t Precio: ${lib.precio}\t Edición especial.")
            else:
                print(f"Nombre libro: {lib.titulo} \t\t Autor: {lib.autor} \t Precio: ${lib.precio}\t Edición común.")


def listaPais_categoria(listado_libros):
    pais = input("Ingrese pais del libro a buscar -> ")
    cat = input("Ingrese categoria del libro a buscar -> ")

    for lib in listado_libros:
        ran = rn.randint(1500, 5000)
        if lib.pais == pais and lib.categoria == cat:
            print(f"List Code: N°{ran} --- Mostrando resultados (Pais: {pais}\t Categoria: {cat})")
            print(f"Titulo obra: {lib.titulo}\t Autor: {lib.autor}\t Pais: {lib.pais}\t Categoria: {lib.categoria}\t Precio: ${lib.precio}")

        else:
            print("Categoria o País no registrado..")
            time.sleep(2)


def salir():
    print("Cerrando entorno... By Jhon Wick (V2.0)")
    time.sleep(2)
    ciclo = False


while ciclo:
    print("1) Grabar nuevo libro")
    print("2) Buscar libro")
    print("3) Listado por país y categoria")
    print("4) Salir")
    try:
        op = int(input("Ingrese una opción (1-4) -> "))
        match op:
            case 1:
                print("--- Grabado de nuevo libro ---")
                grabarLibro(listado_libros)
            case 2:
                print("--- Buscar libro ---")
                buscarLibro(listado_libros)
            case 3:
                print("--- Listado por país y categoria ---")
                listaPais_categoria(listado_libros)
            case 4:
                print("--- Salir ---")
                salir()
            case _:
                print("Opcion ingresada incorrecta..")
                time.sleep(2)
    except BaseException as error:
        print(f"Error code -> {error}")



