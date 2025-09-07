import pandas as pd

def obtenerDatos(ruta_excel="resultado_laboratorio_suelo.xlsx"):

    tablaSuelo = pd.read_excel(ruta_excel)

    tablaSuelo.columns = tablaSuelo.columns.str.strip()

    def corregirValores(valor):
        if pd.isna(valor):
            return None

        if isinstance(valor, (int, float)):
            return valor

        valorStr = str(valor).strip()

        # Cambia tipo fecha a tipo número
        if "-" in valorStr or ":" in valorStr:
            fecha = pd.to_datetime(valorStr, errors="coerce")
            if pd.notna(fecha):
                return float(f"{fecha.day}.{fecha.month}")

        try:
            return float(valorStr.replace(",", "."))
        except:
            return valorStr

    tablaSuelo = tablaSuelo.applymap(corregirValores)

    def renombrarColumnas(tabla):
        return tabla.rename(columns={
            "pH agua:suelo 2,5:1,0": "pH",
            "Fósforo (P) Bray II mg/kg": "Fosforo",
            "Potasio (K) intercambiable cmol(+)/kg": "Potasio"
        })

    tablaSuelo = renombrarColumnas(tablaSuelo)

    tablaSuelo.to_excel(ruta_excel, index=False)

    columnaNecesarias = [
        "Departamento",
        "Municipio",
        "Cultivo",
        "Topografia",
        "pH",
        "Fosforo",
        "Potasio"
    ]

    return tablaSuelo[columnaNecesarias]
