print('Anderson Emilio Blanco Rivera Carné: 1566323')
import os

mi_ubicacion = os.getcwd()
if os.path.exists("modulos"):
    print("La carpeta ya existe")
else:
    os.mkdir(mi_ubicacion + "\\modulos")
    archivo = open('./modulos/prueba.txt', 'w')
    archivo.write('Hola mundo')
    archivo.close()

    archivo = open(".gitignore")
    archivo.close()
