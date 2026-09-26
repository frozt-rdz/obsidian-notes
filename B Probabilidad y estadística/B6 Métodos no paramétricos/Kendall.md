Necesitamos SciPy:

```
pip install scipy
```

Código:

```
from scipy.stats import kendalltau

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

tau, p = kendalltau(x, y)

print("Tau:", tau)
print("p-value:", p)
```

Esperamos aproximadamente:

```
Tau: 1.0
p-value: muy pequeño
```

# ¿Qué significa el p-value?

Aquí aparece una idea fundamental de estadística.

Tenemos:

H0:no existe asociacioˊnH_0: \text{no existe asociación}

y

H1:existe asociacioˊnH_1: \text{existe asociación}

Si:

```
p < 0.05
```

podemos considerar que los datos proporcionan evidencia contra H0H_0, bajo el nivel de significancia elegido.

Por ejemplo:

```
tau = 0.82
p = 0.003
```

Podríamos escribir:

> Existe evidencia estadística de una asociación monotónica positiva entre X y Y.

Pero no debemos decir automáticamente:

> "X causa Y."

**Correlación ≠ causalidad.**

# Ejemplo más realista

Imagina que analizamos:

```
Año
2018
2019
2020
2021
2022
2023
2024

NDVI
0.45
0.47
0.46
0.50
0.51
0.53
0.54
```

Queremos saber:

> ¿Existe una tendencia creciente del NDVI con el tiempo?

Podemos utilizar Kendall.

```
from scipy.stats import kendalltau

años = [2018, 2019, 2020, 2021, 2022, 2023, 2024]

ndvi = [0.45, 0.47, 0.46, 0.50, 0.51, 0.53, 0.54]

tau, p = kendalltau(años, ndvi)

print(f"Tau = {tau:.3f}")
print(f"p-value = {p:.4f}")
```

Esto puede ser muy útil para un problema donde queremos detectar tendencias en datos ambientales.

# ¿Y los empates en Kendall?

Ahora imagina:

```
X = 1, 2, 3, 4, 5
Y = 10, 20, 20, 30, 40
```

Tenemos un empate:

```
20
20
```

Kendall tiene métodos para manejar estos empates.

Por eso **no necesitas eliminar automáticamente los valores repetidos**.

En Python:
```
from scipy.stats import kendalltau

x = [1, 2, 3, 4, 5]
y = [10, 20, 20, 30, 40]

tau, p = kendalltau(x, y)

print(tau)
print(p)
```

SciPy tiene en cuenta los empates al calcular Kendall tau.