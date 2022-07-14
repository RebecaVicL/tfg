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
    x1 = pd.read_excel(path, sheet_name = "Datos", usecols="S,W:BN", skiprows=11, nrows=12, header=0, index_col=None)
    #ID = pd.read_excel(path, sheet_name = "Datos", usecols="S", skiprows=11, header=0, index_col=0)


    x1 = x1.fillna(0)
    
    for i in range(x1.shape[1]):
        x1.columns.values[i] = x1.columns.values[i].replace(" ", "_")
    print(x1)
    engine = create_engine(url , echo = False, encoding='utf-8')
    with engine.connect() as conn, conn.begin():
        x1.to_sql(tabla, conn, if_exists='replace')
    print ("Migración terminada!")
 
 
if __name__ == '__main__':
    excel2mysql()

#  https://www.manejandodatos.es/2019/04/migracion-de-excel-a-mysql/
