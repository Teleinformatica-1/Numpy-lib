#Importacion de numpy
import numpy as np

arrayUnos = np.ones(10)
array_CeroDiez = np.arange(10)
array_pares = np.arange(0,20,2)
array_impares = np.arange(1,21,2)

#OPERACIONES ENTRE ARREGLOS-----------------

#Sumar, restar, multiplicar y dividir cada elemento de un array
print("Array de pares + 1:")
print(array_pares+1)

print("Array de impares -1:")
print(array_impares-1)

print("Array de cero a diez /10:")
print(array_CeroDiez/10)

print("Array de unos *10:")
print(arrayUnos*10)

#Sumar, restar, multiplicar y dividir arrays entre arrays
print("Array de pares - array de pares:")
print(array_pares + array_pares)

print("Array de impares - array de impares:")
print(array_impares - array_impares)

print("Array de cero a diez * array de cero a diez:")
print(array_CeroDiez * array_CeroDiez)

print("Array de unos / array de unos:")
print(arrayUnos/arrayUnos)

#Métodos estadísticos dentro un array
#Suma de los valores dentro del array
print("Suma de los valores del array de cero a diez:")
print(array_CeroDiez.sum())

#Promedio de los valores dentro del array
print("Promedio de los valores dentro del array de pares:")
print(array_pares.mean())

#Varianza de los valores dentro del array
print("Varianza de los valores dentro del array de impares:")
print(array_impares.var())
