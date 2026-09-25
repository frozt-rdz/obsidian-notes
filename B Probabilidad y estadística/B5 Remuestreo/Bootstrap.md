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