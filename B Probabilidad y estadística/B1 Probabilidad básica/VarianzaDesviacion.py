import numpy as np

datos = np.array([49, 50, 51])

media = np.mean(datos)
varianza = np.var(datos)
desviacion = np.std(datos)

print("Media:", media)
print("Varianza:", varianza)
print("Desviación estándar:", desviacion)

#Ahora cambiamos los datos
#Datos mas lejanos de la media, para ver como cambia la varianza y desviacion
datos = np.array([10, 50, 90])

print("Media:", np.mean(datos))
print("Varianza:", np.var(datos))
print("Desviación estándar:", np.std(datos))

