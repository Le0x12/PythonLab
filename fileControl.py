#Creamos un archivo para lectura y escritura
myFile = open("ilMioArchivo.txt", "w+")

#Escribimos en el archivo algun texto de una linea 
myFile.write("Python POWER ᕙ(`▽´)ᕗ \n\n")

#Escribimos un texto con multilineas
myFile.writelines(["Historial de lanzamientos de Python\n","Guido Van Rossum publicó la primera versión del código Python (versión 0.9.0) en 1991. Dicha versión ya incluía buenas características, como algunos tipos de datos y funciones para la gestión de errores.\n",
"Python 1.0 se lanzó en 1994 con nuevas funciones para procesar fácilmente una lista de datos, como la asignación, el filtrado y la reducción.\n","Python 2.0 se lanzó el 16 de octubre de 2000, con nuevas características útiles para los programadores, como la compatibilidad con los caracteres Unicode y una forma más corta de recorrer una lista.\n","El 3 de diciembre de 2008, se lanzó Python 3.0. Incluía características como la función de impresión y más soporte para la división de números y la gestión de errores. \n"])

#Cerramos el archivo
myFile.close()