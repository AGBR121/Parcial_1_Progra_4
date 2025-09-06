import pandas as pd

def cargar_datos(path_excel="resultado_laboratorio_suelo.xlsx"):
    df = pd.read_excel(path_excel)

    df.columns = df.columns.str.strip()

    col_ph = "pH agua:suelo 2,5:1,0"

    def corregir(val):
        if pd.isna(val):  
            return None

        if isinstance(val, (int, float)):
            return float(val)

        val_str = str(val).strip()
        
        if "-" in val_str:
            fecha = pd.to_datetime(val_str, errors="coerce")
            if pd.notna(fecha):
                return float(f"{fecha.day}.{fecha.month}")

        try:
            return float(val_str.replace(",", "."))
        except:
            return None

    if col_ph in df.columns:
        df[col_ph] = df[col_ph].apply(corregir)

        df.to_excel(path_excel, index=False)
        print(f"✅ Columna '{col_ph}' corregida y guardada en {path_excel}")
    else:
        print(f"⚠️ No encontré la columna '{col_ph}'. Columnas disponibles: {df.columns.tolist()}")

    return df
