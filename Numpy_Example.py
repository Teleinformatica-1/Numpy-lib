import numpy as np
import matplotlib.pyplot as plt

#Configuración de plt para ser tomado como escala de grises
plt.rcParams['image.cmap'] = 'gray'

#tamaño de las matrices 
tamano=(20,30)

#Una matriz de ceros representando el color negro 
negro = np.zeros(tamano)

#Una matriz de unos representando el color blanco
blanco = np.ones(tamano)

#Una matriz de 0.5 representando el color gris
gris = np.ones(tamano)*0.5

#Una matriz de calores aleatorios entre 0 y 1 
Aleatorio = np.random.rand(tamano[0],tamano[1]) 

#Agregar y mostrar matriz a plt
plt.imshow(negro,vmin=0,vmax=1)
plt.show()

#Agregar y mostrar matriz a plt
plt.imshow(blanco,vmin=0,vmax=1)
plt.show()

#Agregar y mostrar matriz a plt
plt.imshow(gris,vmin=0,vmax=1)
plt.show()

#Agregar y mostrar matriz a plt
plt.imshow(Aleatorio,vmin=0,vmax=1)
plt.show()