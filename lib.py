class Libro:
    codigo = ''
    titulo = ''
    autor = ''
    precio = 0
    pais = ''
    anio_publicacion = 2022
    categoria = ''
    especial = False
    listado_libros = []

    def __init__(self):
        self.especial = True
        self.codigo = 'AAC-123'
        self.titulo = 'Don Quijote de la Mancha'
        self.autor = 'Pepito'
        self.precio = 20000
        self.pais = 'S/P'
        self.anio_publicacion = 2022
        self.categoria = 'Ficcion'

    def setCodigo(self, codigo):
        if len(codigo) < 8 and codigo[0:3].isalpha() and codigo[3:4] == '-' and codigo[4:7].isdigit():
            self.codigo = codigo
            return True
        else:
            print("Formato de codigo incorrecto.")
            return False

    def setPrecio(self, precio):
        if 10000 <= precio <= 150000:
            self.precio = precio
            return True
        else:
            print("Formato de precio incorrecto (Entre 10k y 150k)")
            return False

    def setAnio_publicacion(self, anio_publicacion):
        if 1780 <= anio_publicacion <= 2023:
            self.anio_publicacion = anio_publicacion
            return True
        else:
            print("Formato año de publicacion no valido")
            return False
