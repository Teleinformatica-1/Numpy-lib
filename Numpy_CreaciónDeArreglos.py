#Importacion de numpy
import numpy as np

#CREACIÓN DE ARREGLOS----------------------

#Array de números aleatorios desde cero
arrayAleatorios = np.random.rand(20)
print("Array de 20 números aleatorios:")
print(arrayAleatorios)

#Array de números aleatorios enteros desde cero
arrayAleatoriosEnteros = np.random.randint(20, size=20)
print("Array de 20 enteros aleatorios:")
print(arrayAleatoriosEnteros)

#Array Vacio
arrayVacio = np.empty((2,10))
print("Arreglo vacio:")
print(arrayVacio)

#Array lleno de 0  
arrayCeros = np.zeros(10)
print("Arreglo de ceros:")
print(arrayCeros)

#Array lleno de 1
arrayUnos = np.ones(10)
print("Arreglo de unos:")
print(arrayUnos)


#Array de una sucesión de números

#Inicia por defecto en 0 y con incremento en 1
#siendo 10 el valor final
array_CeroDiez = np.arange(10)
print("Arreglo de cero a diez:")
print(array_CeroDiez)

#Inicia en 0, hasta 20, con incremento en 2
array_pares = np.arange(0,20,2)
print("Arreglo de números pares:")
print(array_pares)

#Inicia en 1, hasta 21, con incremento en 2
array_impares = np.arange(1,21,2)
print("Arreglo de números impares:")
print(array_impares)

#Cambiar la dimension de arreglos ya creados
#Cantidad de filas 2, Cantidad de columnas 5
array_pares_reshaped = array_pares.reshape(2,5)
print("Arreglo bidimencional del arreglo anterior de números pares:")
print(array_pares_reshaped)