#path =  "./20220305-DatosNormalizados-AsignaturaElectronicaCircuitos-Curso2021-GrupoE.xlsx"
tabla = "GrupoE"
#tabla = "GrupoA"
url = 'mysql+pymysql://root:patata@127.0.0.1/EC' #credenciales(excel_user), contraseña(patata) y host(localhost)

import os
import sys
import pandas as pd
from sqlalchemy import create_engine 
from sqlalchemy_utils import database_exists, create_database
 
def selfichero():
    ficheros_dir = './'
    with os.scandir(ficheros_dir) as ficheros:
        ficheros = [fichero.name for fichero in ficheros if fichero.is_file() and fichero.name.endswith('.xlsx')]
    print("Estos son los ficheros que hay en esta carpeta:")
    for n in ficheros:
        print(f"[{ficheros.index(n)}]" + n)     
    excel_seleccionado=ficheros[int(input("-Selecciona el fichero que quieres analizar-->"))]
    print("./" + excel_seleccionado)
    return "./" + excel_seleccionado


def excel2mysql():
    path = selfichero()
    x1 = pd.read_excel(path, sheet_name = "Datos", usecols="S,X:AY,BL:BN", skiprows=11, nrows=12, header=0, index_col=None)
    #ID = pd.read_excel(path, sheet_name = "Datos", usecols="S", skiprows=11, header=0, index_col=0)


    x1 = x1.fillna(0)
    
    for i in range(x1.shape[1]):
        x1.columns.values[i] = x1.columns.values[i].replace(" ", "_")
    engine = create_engine(url , echo = False, encoding='utf-8')
    if not database_exists(engine.url):
        create_database(engine.url)
    with engine.connect() as conn, conn.begin():
        x1.to_sql(tabla, conn, if_exists='replace')
    print ("Migración terminada!")
 
 
if __name__ == '__main__':
    excel2mysql()

#  https://www.manejandodatos.es/2019/04/migracion-de-excel-a-mysql/