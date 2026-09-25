## ¿Qué problema intenta resolver?

Imagina que calculas:

> "La mediana de mis datos es 22."

Pero tienes pocos datos.

La pregunta es:

> **¿Qué tan confiable es ese 22?**

El bootstrap intenta estimar la **incertidumbre de una estadística** sin necesitar asumir que los datos siguen una distribución normal.

# La idea del Bootstrap

Tenemos:

```
Datos originales
10 12 15 16 20
```

El bootstrap hace algo curioso:

### Selecciona datos CON reemplazo

Eso significa que un dato puede aparecer varias veces.

Una muestra bootstrap podría ser:

```
12 12 20 10 16
```

Otra:

```
15 15 15 10 20
```

Otra:

```
16 20 10 10 12
```

Todas tienen 5 elementos, igual que la muestra original.

Después calculamos nuestra estadística en cada muestra.

Por ejemplo, si nos interesa la mediana:

```
Muestra 1 → mediana = 12
Muestra 2 → mediana = 15
Muestra 3 → mediana = 12
...
```

Después de miles de repeticiones tenemos una distribución de posibles medianas.

# ¿Qué significa "con reemplazo"?

Esta parte es fundamental.

Supón:

```
Original:

[10, 20, 30, 40, 50]
```

En bootstrap puedes sacar:

```
30
```

y **volver a meterlo** antes de sacar otro.

Entonces podrías obtener:

```
30, 10, 30, 50, 20
```

El `30` aparece dos veces.

Eso es "con reemplazo".

# Intervalo de confianza mediante Bootstrap

Supongamos que tenemos:

```
datos = [10, 12, 15, 16, 20]
```

Queremos un intervalo de confianza del 95 % para la **mediana**.
Podemos hacer:

```
import numpy as np

datos = np.array([10, 12, 15, 16, 20])

rng = np.random.default_rng(42)

bootstrap_stats = []

for _ in range(10000):
    muestra = rng.choice(datos, size=len(datos), replace=True)
    mediana = np.median(muestra)
    bootstrap_stats.append(mediana)

bootstrap_stats = np.array(bootstrap_stats)

media_bootstrap = np.mean(bootstrap_stats)
ic = np.percentile(bootstrap_stats, [2.5, 97.5])

print("Mediana original:", np.median(datos))
print("Media de las medianas bootstrap:", media_bootstrap)
print("IC 95%:", ic)
```

### ¿Qué hace `rng.choice()`?

Esta línea:

```
muestra = rng.choice(datos, size=len(datos), replace=True)
```

significa:

> "Selecciona 5 elementos de `datos`, permitiendo repetirlos."

# ¿Por qué `2.5` y `97.5`?

Queremos el 95 % central de los resultados.

Visualmente:

```
 |----------- 95% -----------|
2.5%                         97.5%
 |                              |
 ↓                              ↓
----------------------------------
```

Los extremos representan aproximadamente el 5 % que queda fuera:

```
2.5% + 95% + 2.5% = 100%
```

Por eso usamos:

```
np.percentile(bootstrap_stats, [2.5, 97.5])
```

Este método suele llamarse **percentile bootstrap**.

# Visualicemos el Bootstrap

Esto ayuda muchísimo para entenderlo.

```
import matplotlib.pyplot as plt

plt.hist(bootstrap_stats, bins=20)

plt.axvline(ic[0], linestyle="--")
plt.axvline(ic[1], linestyle="--")

plt.xlabel("Mediana bootstrap")
plt.ylabel("Frecuencia")
plt.title("Distribución Bootstrap de la mediana")

plt.show()
```

Verás algo parecido a:

```
             ███
             █████
         ███████████
       ███████████████
    ███████████████████
██████████████████████████
----|-------------------|----
   2.5%                97.5%
```

La idea importante es:

> **El bootstrap convierte una sola estimación en una distribución de estimaciones posibles.**

# Bootstrap NO significa "hacer datos nuevos"

Esto es muy importante.

No estamos afirmando:

> "Estos datos son datos reales nuevos."

Estamos diciendo:

> "Voy a utilizar mi muestra como aproximación de la población y simular qué podría pasar si volviera a tomar muestras."

Es una especie de **experimento estadístico por computadora**.
# ¿Por qué es útil si no suponemos normalidad?

Muchos métodos estadísticos clásicos empiezan suponiendo:

```
Los datos siguen una distribución normal
```

Pero el bootstrap puede trabajar con distribuciones bastante diferentes.

Por ejemplo:

```
5, 6, 7, 8, 9, 100
```

Claramente hay un valor extremo.

No necesitamos asumir automáticamente:

```
Campana de Gauss
```

para construir una aproximación empírica de la incertidumbre.

### Pero cuidado

Bootstrap **no significa que no haya ninguna suposición**.

El bootstrap ordinario necesita, en términos generales, que las observaciones sean suficientemente independientes e intercambiables.

Eso se vuelve problemático en **series temporales**, y justamente por eso existe el bootstrap por bloques.