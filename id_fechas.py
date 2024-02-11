# path =  "./20220305-DatosNormalizados-AsignaturaElectronicaCircuitos-Curso2021-GrupoE.xlsx"
# tabla = "GrupoE_fechas"
url = 'mysql+pymysql://root:patata@mariadb/Asignatura' #credenciales(excel_user), contraseña(patata) y host(localhost)

 
try:
    import sys
    import pandas as pd
    from sqlalchemy import create_engine 
    from sqlalchemy_utils import database_exists, create_database
 
except Exception as e:
    print(" *** ERROR FATAL *** Error inicial al cargar librerias!! ")
    print(e)
    sys.exit(0)
 
def load_fechas(file):
    path = file
    tabla = "Fecha"
    x1 = pd.read_excel(path, sheet_name = "Datos", usecols="W:BN", skiprows=2, nrows=6, header=None, index_col=0)

    x2 = pd.read_excel(path, sheet_name = "Datos", usecols="W:BN", skiprows=11, nrows=1, header=None, index_col=0)
       
    x3 = pd.read_excel(path, sheet_name = "Datos", usecols="S,X:BN", skiprows=12, nrows=11, header=None, index_col=0)

    x1 = x1.fillna(0)
    x3 = x3.fillna(0)
    x1 = x1.transpose()
    x2 = x2.transpose()
    x3 = x3.transpose()

    for i in range(x1.shape[1]):
        x1.columns.values[i] = x1.columns.values[i].replace(" ", "_")
    for i in range(x2.shape[1]):
        x2.columns.values[i] = x2.columns.values[i].replace(" ", "_")
    for i in range(x3.shape[1]):
        x3.columns.values[i] = x3.columns.values[i].replace(" ", "_")

    x4 = pd.concat([x1,x2,x3],axis=1)
    x4["Fecha"] =  pd.to_datetime(x4["Fecha"], format="%Y-%m-%d")

    engine = create_engine(url , echo = False, encoding='utf-8')
    if not database_exists(engine.url):
        create_database(engine.url)
    with engine.connect() as conn, conn.begin():
        x4.to_sql(tabla, conn, if_exists='replace')
    print ("Migración terminada!")

#  https://www.manejandodatos.es/2019/04/migracion-de-excel-a-mysql/
