def recibirDatos():
    print("Analisis de Laboratorio Suelos en Colombia\n")

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

def imprimirResultados(resultados):

    if resultados is None:
        print("\nNo se encontraron resultados con los filtros ingresados.\n")
        return

    departamento, municipio, cultivo, topografias, medianaPh, medianaFosforo, medianaPotasio = resultados

    caracter_horizontal = "─"  
    caracter_vertical = "│" 
    caracter_esquina = "+"
    
    filasTabla = [
        ("Departamento", departamento),
        ("Municipio", municipio),
        ("Cultivo", cultivo),
        ("Topografía(s)", topografias),
        ("Mediana pH", f"{medianaPh:.2f}"),
        ("Mediana Fósforo", f"{medianaFosforo:.2f}"),
        ("Mediana Potasio", f"{medianaPotasio:.2f}"),
    ]

    # Calcular ancho de columnas
    ancho_columna_1 = max(len(fila[0]) for fila in filasTabla) + 2
    ancho_columna_2 = max(len(fila[1]) for fila in filasTabla) + 2

    linea_separadora = (
        caracter_esquina 
        + caracter_horizontal * ancho_columna_1 
        + caracter_esquina 
        + caracter_horizontal * ancho_columna_2 
        + caracter_esquina
    )

    print("\nResultados del análisis\n")
    print(linea_separadora)
    for etiqueta, valor in filasTabla:
        print(f"{caracter_vertical} {etiqueta.ljust(ancho_columna_1-1)}"
              f"{caracter_vertical} {valor.ljust(ancho_columna_2-1)}{caracter_vertical}")
        print(linea_separadora)




