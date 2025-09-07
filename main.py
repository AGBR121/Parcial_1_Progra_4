from api import Backend
from ui import Frontend

def main():
    datosRecibidos = Frontend.recibirDatos()
    medianas = Backend.filtrarDatos(datosRecibidos)
    Frontend.imprimirResultados(datosRecibidos, medianas)


if __name__ == "__main__":
    main()
