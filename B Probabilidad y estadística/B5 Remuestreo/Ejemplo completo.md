Vamos a simular una serie con tendencia + autocorrelación.

```
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

n = 150

x = np.arange(n)

y = np.zeros(n)

for i in range(1, n):

    tendencia = 0.03 * x[i]

    ruido = rng.normal(0, 0.8)

    y[i] = (
        tendencia
        + 0.7 * y[i-1]
        + ruido
    )

plt.plot(x, y)

plt.xlabel("Tiempo")
plt.ylabel("Valor")
plt.title("Serie temporal con tendencia y autocorrelación")

plt.show()
```

Aquí estamos simulando algo que podría parecerse conceptualmente a:

```
Tiempo
 ↓

  /\      /\
 /  \__  /  \___
      \/         \__
         ↑
     tendencia general
```

# Calculamos la pendiente observada

```
pendiente = np.polyfit(x, y, 1)[0]

print("Pendiente:", pendiente)
```

# Bootstrap normal

```
rng = np.random.default_rng(42)

pendientes = []

for _ in range(10000):

    indices = rng.choice(
        n,
        size=n,
        replace=True
    )

    y_boot = y[indices]

    pendiente_boot = np.polyfit(
        x,
        y_boot,
        1
    )[0]

    pendientes.append(pendiente_boot)

pendientes = np.array(pendientes)

ic = np.percentile(
    pendientes,
    [2.5, 97.5]
)

print("IC bootstrap normal:", ic)
```

Pero recuerda:

> aquí ignoramos la dependencia temporal.

# Bootstrap por bloques de la pendiente

Vamos a cambiar la estrategia.

```
def block_bootstrap_slope(
    x,
    y,
    block_size,
    n_iter=10000
):

    rng = np.random.default_rng(42)

    n = len(y)

    pendientes = []

    for _ in range(n_iter):

        indices = []

        while len(indices) < n:

            inicio = rng.integers(0, n)

            bloque = (
                np.arange(inicio, inicio + block_size)
                % n
            )

            indices.extend(bloque)

        indices = np.array(indices[:n])

        y_boot = y[indices]

        pendiente = np.polyfit(
            x,
            y_boot,
            1
        )[0]

        pendientes.append(pendiente)

    return np.array(pendientes)
```

Ahora:

```
pendientes_bloques = block_bootstrap_slope(
    x,
    y,
    block_size=10,
    n_iter=10000
)

ic_bloques = np.percentile(
    pendientes_bloques,
    [2.5, 97.5]
)

print("IC bootstrap por bloques:", ic_bloques)
```

La diferencia conceptual es:

```
Bootstrap normal:

dato dato dato dato dato
 ↑    ↑    ↑    ↑    ↑
independientes


Bootstrap por bloques:

[ dato dato dato ]
[ dato dato dato ]
[ dato dato dato ]
       ↑
preservamos estructura local
```

# Una advertencia importante sobre las pruebas de permutación

Aquí hay una trampa que probablemente te interese mucho para el NASA Challenge.

Para datos independientes puedes hacer:

```
y_perm = rng.permutation(y)
```

Pero si `y` es una **serie temporal autocorrelacionada**, una permutación arbitraria:

```
1 2 3 4 5 6
```

→

```
5 1 6 2 4 3
```

destruye la estructura temporal.

Por eso:

> **No debes usar automáticamente una prueba de permutación ordinaria para una serie temporal solo porque Python la permite.**

Hay técnicas específicas para series temporales cuando quieres construir una prueba que respete la dependencia.

# Un mini mapa mental

```
                    REMUESTREO
                         │
          ┌──────────────┴──────────────┐
          │                             │
      BOOTSTRAP                    PERMUTACIÓN
          │                             │
          │                             │
   ¿Qué tan incierto?           ¿Qué tan raro?
          │                             │
          │                             │
   Con reemplazo                 Mezclar/reasignar
          │                             │
          │                             │
          └──────────────┬──────────────┘
                         │
                  SERIES TEMPORALES
                         │
                 autocorrelación
                         │
                         ↓
                BOOTSTRAP POR BLOQUES
```

# Las tres preguntas que debes recordar

Cuando veas un problema, piensa:

### Pregunta 1

> **Quiero un intervalo de confianza.**

Piensa:

```
BOOTSTRAP
```

---

### Pregunta 2

> **Quiero saber si mi resultado podría aparecer por azar.**

Piensa:

```
PERMUTACIÓN
```

---

### Pregunta 3

> **Mis datos son temporales y hay autocorrelación.**

Piensa:

```
BOOTSTRAP POR BLOQUES
```
**Regla de oro para B5:**

> **Bootstrap = incertidumbre.**  
> **Permutación = azar bajo una hipótesis nula.**  
> **Bloques = dependencia temporal.**