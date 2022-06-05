path =  "./20220305-DatosNormalizados-AsignaturaElectronicaCircuitos-Curso2021-GrupoE.xlsx"
solapa = "Datos"
tabla = "GrupoE_Fechas"
url = 'mysql+pymysql://excel_user:patata@127.0.0.1/EC' #credenciales(excel_user), contraseña(patata) y host(localhost)

 
try:
    import sys
    import pandas as pd
    from sqlalchemy import create_engine 
 
except Exception as e:
    print(" *** ERROR FATAL *** Error inicial al cargar librerias!! ")
    print(e)
    sys.exit(0)
 
def excel2mysql():
    try:
        try:
            x1 = pd.read_excel(path, sheet_name = "Datos", header = 4)
            #x1 = df.parse(solapa)
            x1.columns = map(str.lower, x1.columns)  # Columnas a lower
            engine = create_engine(url , echo = False, encoding='utf-8')
            with engine.connect() as conn, conn.begin():
                x1.to_sql(tabla, conn, if_exists='replace')
            print ("Migración terminada!")
 
        except Exception as f:
            print('Imposible conectar con Base de datos!! Revise datos de conexión!!' )
            print(f)
 
    except Exception as e:
        print('ERROR!! Imposible abrir fichero')
        print(e)
 
if __name__ == '__main__':
    excel2mysql()

# https://runebook.dev/es/docs/pandas/reference/api/pandas.read_excel