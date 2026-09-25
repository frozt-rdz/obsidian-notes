import numpy as np
import matplotlib.pyplot as plt
datos = np.array([10, 12, 15, 16, 20])

# Generador de números aleatorios -> 42 es la semilla, chiste chiste
rng = np.random.default_rng(42)

bootstrap_stats = []

for _ in range (10000):
    #Creamos las muestras, 5 datos (10, 12, 15, 16, 20)
    muestra = rng.choice(datos, size=len(datos), replace=True)
    mediana = np.median(muestra)
    bootstrap_stats.append(mediana)

#Conversion a arreglo
bootstrap_stats = np.array(bootstrap_stats)

media_bootstrap = np.mean(bootstrap_stats)
ic = np.percentile(bootstrap_stats, [2.5, 97.5])

print("Mediana original:", np.median(datos))
print("Media de las medianas de bootstrap:", media_bootstrap)
print("IC 95%", ic)

#VISUALIZACION
# Datos a anlizar a 20 intervalos (bins) en histograma(hist)
plt.hist(bootstrap_stats, bins=20)

plt.axvline(ic[0], linestyle="--")
plt.axvline(ic[1], linestyle="--")

plt.xlabel("Mediana bootstrap")
plt.ylabel("Frecuencia")
plt.title("Distribución Bootstrap de la mediana")

plt.show()