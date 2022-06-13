path =  "./20220305-DatosNormalizados-AsignaturaElectronicaCircuitos-Curso2021-GrupoE.xlsx"
#path = "./EC_2021_GrupoA.xlsx"
solapa = "Datos"
tabla = "GrupoE"
#tabla = "GrupoA"
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
            # x1 = pd.read_excel(path, sheet_name = "Datos", header=11)
            # x1 = pd.read_excel(path, sheet_name = "Datos", index_col=22, nrows=2, usecols="A,C,E:F")
            # x1 = pd.read_excel(path, sheet_name = "Datos", usecols="W:BN", skiprows=2, nrows=6, converters={ "NaN": 0})
            x1 = pd.read_excel(path, sheet_name = "Datos", usecols="W:BN", skiprows=2, nrows=6, header=0, index_col=0)
            
            x1 = x1.fillna(0)
            print(x1)
            x1 = x1.transpose()
            #print(x1.keys())
            # print(x1.items)
            print(list(x1)[0].replace(" ","_"))
            print(x1)
            for i in range(5):
                  list(x1)[i] = list(x1)[i].replace(" ","_")
                  print(list(x1)[i])
            #     x1[i][22] = x1[i][22].replace(" ","_")
            print(x1)


            #x1 = df.parse(solapa)
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

#  https://www.manejandodatos.es/2019/04/migracion-de-excel-a-mysql/
