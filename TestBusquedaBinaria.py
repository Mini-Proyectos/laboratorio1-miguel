#Se importan las funciones que se usaran
from Busquedas import LecturaDeDatos
from Busquedas import BusquedaBinaria
from Busquedas import Ordenan

arreglo=LecturaDeDatos(input("Ingrese el nombre del archivo: ")) #Se carga el arreglo desde el archivo que ingrese el usuario
e = int(input("Ingrese el elemento a buscar: "))				#Se pide que ingrese el elemento a localizar

if Ordenan(arreglo):											#Se hace una revision para saber si el arreglo esta ordenado
	encontrado = BusquedaBinaria(arreglo, e)					#En caso de que si este ordenado, se llama a la funcion BusquedaBinaria
	if encontrado != None:
		print("Está en la posición: " + str(encontrado))
	else: 
		print("No encontrado")

else:
	print("El arreglo no está ordenado, no se puede buscar") #En caso de que no haya estado ordenado, se le notifica al usuario