
# TestBusquedas.py
# Este es un archivo de prueba muy sencillo, debe ser modificado 
# de acuerdo con el enunciado del laboratorio.

from Busquedas import LecturaDeDatos
from Busquedas import BusquedaLineal

arreglo=LecturaDeDatos(input("Ingrese el nombre del archivo: "))
e = int(input("Ingrese el elemento a buscar: "))

encontrado = BusquedaLineal(arreglo, e)
if encontrado != None:
	print("Está en la posición: " + str(encontrado))
else: 
	print("No encontrado") 

