from api import Backend
from ui import Frontend

def main():
    datosRecibidos = Frontend.recibirDatos()
    resultados = Backend.filtrarDatos(datosRecibidos)
    Frontend.imprimirResultados(resultados)


if __name__ == "__main__":
    main()
