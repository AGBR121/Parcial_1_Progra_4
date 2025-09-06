def recibirDatos():
    print("Análisis de Laboratorio Suelos en Colombia\n")
    print("___________________________________________\n")

    # Pedir los datos al usuario
    departamento = input("1. Ingrese el Departamento: ")
    municipio = input("2. Ingrese el Municipio: ")
    cultivo = input("3. Ingrese el Cultivo: ")

    while True:
        try:
            numeroRegistros = int(input("4. Ingrese el número de registros a consultar: "))
            if numeroRegistros <= 0:
                print("El número debe ser mayor que 0.")
                continue
            break
        except ValueError:
            print("Debe ingresar un número válido.")
    
    return departamento, municipio, cultivo, numeroRegistros