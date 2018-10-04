#Se importan las funciones que se van a usar
from Busquedas import OrdenaInsercion
from Busquedas import LecturaDeDatos

arreglo=LecturaDeDatos(input("Ingrese el nombre del archivo: ")) #Se carga el arreglo desde el archivo que ingrese el usuario

print(OrdenaInsercion(arreglo,0,len(arreglo))) 					#Se muestra el arreglo ordenado por Insercion
