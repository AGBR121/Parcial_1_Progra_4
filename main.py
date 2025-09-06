from api import Backend

def main():
    df = Backend.cargar_datos()

    col_ph = "pH agua:suelo 2,5:1,0"

    print("\n✅ Valores corregidos de pH:")
    print(df[[col_ph]].head(50))

if __name__ == "__main__":
    main()
