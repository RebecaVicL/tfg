import sys
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

url = 'mysql+pymysql://root:patata@mariadb/Asignatura'

try:
    import sys
    import pandas as pd
    import numpy as np
    from sqlalchemy import create_engine
    from sqlalchemy_utils import database_exists, create_database

except Exception as e:
    print(" * ERROR FATAL * Error inicial al cargar librerias!! ")
    print(e)
    sys.exit(0)


def load_fechas(file):
    path = file
    tabla = "Fecha"

    # Leer todas las secciones necesarias en un solo DataFrame
    x1 = pd.read_excel(path, sheet_name="Datos", usecols="W:BN", skiprows=2, nrows=6, header=None, index_col=0).fillna(0).transpose()
    x2 = pd.read_excel(path, sheet_name="Datos", usecols="W:BN", skiprows=11, nrows=1, header=None, index_col=0).fillna(0).transpose()
    x3 = pd.read_excel(path, sheet_name="Datos", usecols="S,X:BN", skiprows=12, nrows=11, header=None, index_col=0).fillna(0).transpose()

    # Limpiar y ajustar nombres de columnas
    for df in [x1, x2, x3]:
        df.columns = [col.replace(" ", "_") if isinstance(col, str) else col for col in df.columns]

    # Concatenar DataFrames
    x4 = pd.concat([x1, x2, x3], axis=1)

    # Convertir la columna "Fecha" a formato de fecha con manejo de errores
    x4["Fecha"] = pd.to_datetime(x4["Fecha"], errors='coerce', format="%Y-%m-%d")

    # Crear la conexión a la base de datos
    engine = create_engine(url, echo=False, encoding='utf-8')

    # Verificar si la base de datos ya existe
    if not database_exists(engine.url):
        create_database(engine.url)

    # Almacenar el DataFrame en la base de datos
    with engine.connect() as conn, conn.begin():
        x4.to_sql(tabla, conn, if_exists='replace')

    print("Migración terminada!")

# Llama a la función con la ruta correcta al archivo Excel
# load_fechas("ruta_del_archivo_excel.xlsx")
