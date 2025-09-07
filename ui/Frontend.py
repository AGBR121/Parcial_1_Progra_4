def recibirDatos():
    print("Analisis de Laboratorio Suelos en Colombia\n")

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
    
    return departamento.upper(), municipio.upper(), cultivo.capitalize(), numeroRegistros

def imprimirResultados(datosRecibidos, medianas):
    departamento, municipio, cultivo, _ = datosRecibidos
    medianaPh, medianaFosforo, medianaPotasio = medianas

    h = "─"  
    v = "│" 
    esquina = "+"
    
    # Datos a mostrar
    filas = [
        ("Departamento", departamento),
        ("Municipio", municipio),
        ("Cultivo", cultivo),
        ("Mediana pH", f"{medianaPh:.2f}"),
        ("Mediana Fósforo", f"{medianaFosforo:.2f}"),
        ("Mediana Potasio", f"{medianaPotasio:.2f}"),
    ]

    # Calcular ancho de columnas dinámicamente
    col1_width = max(len(f[0]) for f in filas) + 2
    col2_width = max(len(f[1]) for f in filas) + 2

    linea = esquina + h * col1_width + esquina + h * col2_width + esquina

    print("\nResultados del análisis\n")
    print(linea)
    for nombre, valor in filas:
        print(f"{v} {nombre.ljust(col1_width-1)}{v} {valor.ljust(col2_width-1)}{v}")
        print(linea)


