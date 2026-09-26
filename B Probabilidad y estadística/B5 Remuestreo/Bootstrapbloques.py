import numpy as np
import pandas as pd

def block_bootstrap(data, block_size, n_iter=10000):

    data = np.asarray(data)
    n = len(data)

    #Generador
    rng = np.random.default_rng(42)

    #Lista de estadisticas que se llenara n_iter
    estadisticas = []

    for _ in range(n_iter):
        #Rellenaremos la lista hasta tener la misma longitud de los datos originales
        muestra = []

        while len(muestra) < n:

            #Punto de partida del bloque al azar
            inicio = rng.integers(0, n)
            #Extraemos el fragmento de data que empieza en inicio que mide bloc_size
            bloque = data[inicio:inicio + block_size]

            #Si el bloque queda corto va al principio de los datos originales y tomas los elementos que le faltan
            if len(bloque) < block_size:
                bloque = np.concatenate([bloque, data[:block_size - len(bloque)]])

            muestra.extend(bloque)

        #Cortamos excedente n
        muestra = np.array(muestra[:n])
        #Promedio de la muestra sintetica
        estadisticas.append(np.mean(muestra))

    return np.array(estadisticas)


rng = np.random.default_rng(42)

n = 200

datos = np.zeros(n)

for i in range(1, n):

    datos[i] = (
        0.8 * datos[i-1]
        + rng.normal(0, 1)
    )

#Se compara cada dato con el inmediato anterior
serie = pd.Series(datos)
print(
    "Autocorrelación lag 1:",
    serie.autocorr(lag=1)
)

# Comparar Bootstrap normal vs Bootstrap por bloques
bootstrap_normal = []

for _ in range(10000):

    muestra = rng.choice(datos,size=len(datos),replace=True)

    bootstrap_normal.append(np.mean(muestra))

bootstrap_normal = np.array(bootstrap_normal)

ic_normal = np.percentile(bootstrap_normal,[2.5, 97.5])

print("Bootstrap normal:")
print(ic_normal)

bootstrap_bloques = block_bootstrap(datos,block_size=10,n_iter=10000)

ic_bloques = np.percentile(bootstrap_bloques,[2.5, 97.5])

print("Bootstrap por bloques:")
print(ic_bloques)
    
