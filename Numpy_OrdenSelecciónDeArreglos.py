#Importacion de numpy
import numpy as np

arrayAleatoriosEnteros = np.random.randint(20, size=20)
array_CeroDiez = np.arange(10)
array_pares_reshaped = np.arange(0,20,2).reshape(2,5)

#ORDEN Y SELECCIÓN EN ARREGLOS--------------

#Ordenar arrays
#Ordenar de mayor a menor
print("Array aleatorio ordenado de mayor a menor:")
print(-np.sort(-arrayAleatoriosEnteros))

#Ordenar de menor a mayor
print("Array aleatorio ordenado de menor a mayor:")
print(np.sort(arrayAleatoriosEnteros))


#Obtener primer elemento
#Tener en cuenta la dimensión del array
print("Obtener primer elemento del array de cero a diez (Dimensión 1):")
print(array_CeroDiez)
print("Primer elemento:")
print(array_CeroDiez[0])

#Obtener ultimo elemento
#Tener en cuenta la dimensión del array
print("Obtener ultimo elemento del array de pares (Dimensión 2):")
print(array_pares_reshaped)
print("Ultimo elemento:")
print(array_pares_reshaped[1,4])

#Obtener cierta fila
print("Obtener la fila 2 del array de pares (Dimensión 2):")
print(array_pares_reshaped)
print("Fila 2:")
print(array_pares_reshaped[1,:])

#Obtener cierta columna
print("Obtener la columna 1 del array de pares (Dimensión 2):")
print(array_pares_reshaped)
print("Columna 1:")
print(array_pares_reshaped[:,1])

#Validar condicion 
#números menores a 20 de un array aleatorio
print("Validar cuales elementos de un array aleatorio son menores a 10:")
print(arrayAleatoriosEnteros)
print("Menores a 10:")
print(arrayAleatoriosEnteros<10)

#Obtener los valores que cumplen cierta condición
#Obtener números mayores a 10 de un array aleatorio
print("Obtener cuales elementos de un array aleatorio son mayores a 10:")
print(arrayAleatoriosEnteros)
print("Mayores a 10:")
print(arrayAleatoriosEnteros[arrayAleatoriosEnteros>10])
