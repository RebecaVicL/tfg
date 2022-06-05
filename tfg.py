# from click import open_file
# import openpyxl
# import pandas as pd
# import os
# from cgi import parse_header
# import xlrd 

hola = '\t\t\n\tHola Mundo\n'
print(hola)
hola_limpio = hola.replace(" ","_")
print(hola_limpio)

######################################################
#import pandas as pd
#from sqlalchemy import create_engine

#db = "EC"
#table = "GrupoE"
#path =  "./20220305-DatosNormalizados-AsignaturaElectronicaCircuitos-Curso2021-GrupoE.xlsx"

#url = 'mysql+pymysql://excel_user:patata@127.0.0.1/EC' #credenciales(excel_user), contraseña(patata) y host(localhost)

#engine = create_engine(url , echo = False)

#df = pd.read_excel(path, sheet_name = "Datos", header = 11)

#print("Hemos terminado de leer")

#df.to_sql(name = table, con = url, if_exists = "append", index = False) 
###########################################################
#Esta funcion lo que hace es volcar lo que ya leimos, primero el nombre de la tabla, despues el objeto de conexion, 
#ver que pasa en caso de que esa tabla ya exista, lo que dice es que agreges los archivos de excel.


# filePath = "./20220305-DatosNormalizados-AsignaturaElectronicaCircuitos-Curso2021-GrupoE.xlsx"

# openFile = xlrd.open_workbook(filePath)

# sheet = openFile.sheet_by_name("Datos")

# print("No de filas", sheet.nrows)

# """
# def main():
#     df = leer_archivos()


# def leer_archivos():
#     print("Leyendo archivos")
#     import os

#     path = "./"
#     filename = input("Ingresar el nombre del archivo que quieres trabajar que se tiene que encontrar en la carpeta donde se encuentra este programa ") + ".xlsx"
#     fullpath = os.path.join(path, filename)
#     input(fullpath)
#     df = pd.read_excel(fullpath, sheet_name = "Datos", header = 0)
    
# if __name__ == "__main__":
#     main()
#     input("LA FUNCION SE HA TERMINADO CON ÉXITO, presiona enter para salir")
# """

# """
# excel_document = openpyxl.load_workbook('20220305-DatosNormalizados-AsignaturaElectronicaCircuitos-Curso2021-GrupoE.xlsx')
# sheet = excel_document.get_sheet_by_name('Datos')


# multiple_cells = sheet['U12':'U24']
# for column in multiple_cells:
#     for cell in column:
#         print cell.value
# """
