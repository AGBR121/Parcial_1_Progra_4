from api import Backend
from ui import Frontend

def main():
    datosRecibidos = Frontend.imprimirMenu()
    datosTabla = Backend.obtenerDatos()

    print("\nDatos corregidos:")
    print(datosTabla)  

if __name__ == "__main__":
    main()
