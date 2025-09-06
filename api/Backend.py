import pandas as pd

def obtenerDatos(ruta_excel="resultado_laboratorio_suelo.xlsx"):

    tabla_suelo = pd.read_excel(ruta_excel)

    tabla_suelo.columns = tabla_suelo.columns.str.strip()

    def corregirValores(valor):
        if pd.isna(valor):
            return None

        if isinstance(valor, (int, float)):
            return valor

        valor_str = str(valor).strip()

        # Cambia tipo fecha a tipo número
        if "-" in valor_str or ":" in valor_str:
            fecha = pd.to_datetime(valor_str, errors="coerce")
            if pd.notna(fecha):
                return float(f"{fecha.day}.{fecha.month}")

        try:
            return float(valor_str.replace(",", "."))
        except:
            return valor_str

    tabla_suelo = tabla_suelo.applymap(corregirValores)

    tabla_suelo.to_excel(ruta_excel, index=False)

    return tabla_suelo

