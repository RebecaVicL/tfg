#path =  "./20220305-DatosNormalizados-AsignaturaElectronicaCircuitos-Curso2021-GrupoE.xlsx"
# tabla = "GrupoE"
# tabla = "GrupoA"
url = 'mysql+pymysql://root:patata@mariadb/Asignatura' #credenciales(excel_user), contraseña(patata) y host(localhost)

import os
import sys
import pandas as pd
from sqlalchemy import create_engine 
from sqlalchemy_utils import database_exists, create_database
from flask import Flask, render_template

def excel2mysql(file):
    path = file
    tabla = "Clase"
    x1 = pd.read_excel(path, sheet_name = "Datos", usecols="S,X:AY,BL:BN", skiprows=11, nrows=12, header=0, index_col=None)

    x1 = x1.fillna(0)
    
    for i in range(x1.shape[1]):
        x1.columns.values[i] = x1.columns.values[i].replace(" ", "_")
    engine = create_engine(url , echo = False, encoding='utf-8')
    if not database_exists(engine.url):
        create_database(engine.url)
    with engine.connect() as conn, conn.begin():
        x1.to_sql(tabla, conn, if_exists='replace')
    print ("Migración terminada!")
    return render_template('finish.html')
 
if __name__ == '__main__':
    excel2mysql()
