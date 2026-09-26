# Ejemplo con datos de temperatura

Supongamos:

```
Día

1   20
2   21
3   21
4   22
5   22
6   23
7   23
8   24
9   23
10  25
```

Si usamos bloques de 3:

```
Bloque 1 → [20, 21, 21]
Bloque 2 → [22, 22, 23]
Bloque 3 → [23, 24, 23]
Bloque 4 → [25]
```

Podemos seleccionar bloques completos.

# Bootstrap por bloques en Python

Vamos a construir una función sencilla.

```
import numpy as np

def block_bootstrap(data, block_size, n_iter=10000):

    data = np.asarray(data)
    n = len(data)

    rng = np.random.default_rng(42)

    estadisticas = []

    for _ in range(n_iter):

        muestra = []

        while len(muestra) < n:

            inicio = rng.integers(0, n)

            bloque = data[
                inicio:inicio + block_size
            ]

            if len(bloque) < block_size:
                bloque = np.concatenate([
                    bloque,
                    data[:block_size - len(bloque)]
                ])

            muestra.extend(bloque)

        muestra = np.array(muestra[:n])

        estadisticas.append(np.mean(muestra))

    return np.array(estadisticas)
```

# Probémoslo

Vamos a crear una serie temporal con autocorrelación.

```
import numpy as np

rng = np.random.default_rng(42)

n = 200

datos = np.zeros(n)

for i in range(1, n):

    datos[i] = (
        0.8 * datos[i-1]
        + rng.normal(0, 1)
    )
```

La parte:

```
0.8 * datos[i-1]
```

hace que el valor actual dependa bastante del anterior.

# Podemos comprobar la autocorrelación

Con pandas:

```
import pandas as pd

serie = pd.Series(datos)

print(
    "Autocorrelación lag 1:",
    serie.autocorr(lag=1)
)
```

Probablemente obtendrás un valor relativamente alto, porque construimos deliberadamente una serie con dependencia temporal.

# Comparar Bootstrap normal vs Bootstrap por bloques

Primero el bootstrap tradicional:

```
import numpy as np

rng = np.random.default_rng(42)

bootstrap_normal = []

for _ in range(10000):

    muestra = rng.choice(
        datos,
        size=len(datos),
        replace=True
    )

    bootstrap_normal.append(
        np.mean(muestra)
    )

bootstrap_normal = np.array(bootstrap_normal)

ic_normal = np.percentile(
    bootstrap_normal,
    [2.5, 97.5]
)

print("Bootstrap normal:")
print(ic_normal)
```

Ahora bootstrap por bloques:

```
bootstrap_bloques = block_bootstrap(
    datos,
    block_size=10,
    n_iter=10000
)

ic_bloques = np.percentile(
    bootstrap_bloques,
    [2.5, 97.5]
)

print("Bootstrap por bloques:")
print(ic_bloques)
```

Muchas veces el intervalo por bloques resultará diferente y puede ser más amplio, porque reconoce que las observaciones no proporcionan tanta información independiente como parecería a primera vista.

# El tamaño del bloque es importante

Esto:

```
block_size = 2
```

y esto:

```
block_size = 30
```

no producen exactamente el mismo resultado.

La lógica es:

```
Bloque pequeño
   ↓
preserva poca dependencia

Bloque grande
   ↓
preserva más dependencia
```

Pero tampoco quieres un bloque gigantesco.

La elección del tamaño del bloque depende de la estructura temporal y del problema.

# Bootstrap normal vs Bootstrap por bloques

| Método                | ¿Qué remuestrea?           | ¿Preserva tiempo?                      |
| --------------------- | -------------------------- | -------------------------------------- |
| Bootstrap tradicional | Observaciones individuales | No                                     |
| Bootstrap por bloques | Grupos consecutivos        | No                                     |
| Permutación           | Reordena/asigna datos      | Generalmente para dependencia temporal |
Una regla mental muy útil:

```
Datos independientes
       ↓
Bootstrap normal
```

pero:

```
Serie temporal
       ↓
¿Hay autocorrelación?
       ↓
Sí
       ↓
considerar bootstrap por bloques
```

# Diferencia fundamental entre Bootstrap y Permutación

Esta tabla merece memorizarse:

# Diferencia fundamental entre Bootstrap y Permutación

Esta tabla merece memorizarse:

|            | Bootstrap<br>                       | Permutación                              |
| ---------- | ----------------------------------- | ---------------------------------------- |
| Pregunta   | ¿Qué tan incierta es mi estimación? | ¿Qué tan raro es mi resultado bajo H₀?   |
| Muestreo   | Con reemplazo                       | Reordenamiento                           |
| Uso típico | Intervalos de confianza             | Pruebas de hipótesis                     |
| Ejemplo    | IC de la pendiente                  | ¿La pendiente es compatible con el azar? |
# Una analogía sencilla

Imagina que estás investigando huellas.

### Bootstrap

Preguntas:

> "Si repitiera muchas veces mi investigación usando los datos disponibles, ¿qué tan diferente sería mi estimación?"

### Permutación

Preguntas:

> "¿Podría encontrar una huella tan marcada simplemente por azar?"

### Bootstrap por bloques

Preguntas:

> "¿Y si las huellas vienen en grupos relacionados? No puedo tratarlas como completamente independientes."