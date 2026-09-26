Esto ya empieza a acercarse mucho al problema del "Detective".

Supongamos:

```
Año       Temperatura
2019      20.1
2020      20.4
2021      20.5
2022      20.8
2023      21.0
```

Calculamos una pendiente:

```
°C por año
```

Pero queremos saber:

> ¿Qué tan incierta es esa pendiente?
> Podemos hacer bootstrap.

```
import numpy as np

x = np.array([2019, 2020, 2021, 2022, 2023])
y = np.array([20.1, 20.4, 20.5, 20.8, 21.0])

rng = np.random.default_rng(42)

pendientes = []

for _ in range(10000):

    indices = rng.choice(len(x), size=len(x), replace=True)

    x_boot = x[indices]
    y_boot = y[indices]

    pendiente = np.polyfit(x_boot, y_boot, 1)[0]

    pendientes.append(pendiente)

pendientes = np.array(pendientes)

ic = np.percentile(pendientes, [2.5, 97.5])

print("Pendiente original:",
      np.polyfit(x, y, 1)[0])

print("IC 95%:", ic)
```

# Interpretando ese intervalo

Supongamos que obtenemos:

```
Pendiente = 0.22

IC 95% = [0.10, 0.34]
```

Una forma descriptiva de interpretarlo sería:

> La estimación de la pendiente es de aproximadamente 0.22 unidades por año, y el intervalo bootstrap del 95 % va aproximadamente de 0.10 a 0.34.

Observa que:

```
0
|
|--- IC ---|
```

El intervalo **no contiene 0**.

Eso es compatible con una pendiente positiva bajo este procedimiento.

Pero todavía falta responder otra pregunta:

> **¿Una pendiente así podría aparecer simplemente por azar?**

Ahí entra la prueba de permutación.
# Prueba de permutación

La idea es diferente.

## Bootstrap pregunta:

> "¿Qué tan variable podría ser mi estimación?"

## Permutación pregunta:

> "Si realmente no hubiera relación, ¿qué tan fácil sería obtener un resultado como el mío?"

Esta diferencia es importantísima.

# Una situación sencilla

Supongamos dos grupos:

```
Grupo A
10 11 12 13 14

Grupo B
20 21 22 23 24
```

Claramente las medias son diferentes.

Tenemos:

```
media A = 12
media B = 22
```

Diferencia:

```
22 - 12 = 10
```

Ahora preguntamos:

> ¿Qué probabilidad existe de observar una diferencia tan grande simplemente por azar?

# La prueba de permutación

Juntamos todos:

```
10 11 12 13 14 20 21 22 23 24
```

Y mezclamos las etiquetas.

Por ejemplo:

```
Grupo A:
20 11 23 13 10

Grupo B:
12 22 21 14 24
```

Calculamos nuevamente:

```
media A
media B
diferencia
```

Repetimos miles de veces.

Así obtenemos la distribución de diferencias que esperaríamos **si las etiquetas de grupo fueran intercambiables**.
# Python: prueba de permutación

```
import numpy as np

grupo_A = np.array([10, 11, 12, 13, 14])
grupo_B = np.array([20, 21, 22, 23, 24])

observada = np.mean(grupo_B) - np.mean(grupo_A)

todos = np.concatenate([grupo_A, grupo_B])

rng = np.random.default_rng(42)

permutaciones = []

for _ in range(10000):

    mezclados = rng.permutation(todos)

    A_perm = mezclados[:len(grupo_A)]
    B_perm = mezclados[len(grupo_A):]

    diferencia = np.mean(B_perm) - np.mean(A_perm)

    permutaciones.append(diferencia)

permutaciones = np.array(permutaciones)

p_valor = np.mean(
    np.abs(permutaciones) >= abs(observada)
)

print("Diferencia observada:", observada)
print("p-valor:", p_valor)
```
# ¿Qué está haciendo `permutation()`?

Esta instrucción:

```
rng.permutation(todos)
```

mezcla aleatoriamente los valores.

Ejemplo:

```
Original:

[10, 11, 12, 20, 21]

Permutado:

[21, 12, 10, 20, 11]
```
# El p-valor explicado de forma sencilla

Supongamos que obtenemos:

```
p = 0.001
```

Significa aproximadamente:

> En las permutaciones realizadas bajo la hipótesis de no diferencia, alrededor del 0.1 % produjo un resultado tan extremo como el observado.

En términos intuitivos:

```
Resultados por azar

        ███████████████████
       █████████████████████
      ███████████████████████
     █████████████████████████
                           X
                           ↑
                      resultado observado
```

Si el resultado observado cae muy lejos de lo que produce el azar, eso es evidencia contra la hipótesis nula.

# Permutación para detectar una tendencia

Aquí aparece algo particularmente importante para tu preparación del NASA Space Apps.

Supongamos:

```
Año     NDVI
2015    0.42
2016    0.43
2017    0.41
2018    0.45
2019    0.47
2020    0.48
```

Calculamos una pendiente.

```
import numpy as np

x = np.arange(2015, 2021)

y = np.array([
    0.42,
    0.43,
    0.41,
    0.45,
    0.47,
    0.48
])

pendiente_observada = np.polyfit(x, y, 1)[0]

print("Pendiente:", pendiente_observada)
```

Ahora hacemos la pregunta:

> "¿Y si estos valores de NDVI estuvieran simplemente asociados a los años por azar?"


# Permutar la tendencia

Mantienes los años:

```
2015
2016
2017
...
```

pero mezclas los valores de `y`.

Por ejemplo:

```
Original:

2015 → 0.42
2016 → 0.43
2017 → 0.41
2018 → 0.45
2019 → 0.47
2020 → 0.48
```

Una permutación:

```
2015 → 0.47
2016 → 0.41
2017 → 0.48
2018 → 0.42
2019 → 0.43
2020 → 0.45
```

Calculamos la pendiente nuevamente.

Después repetimos miles de veces.

```
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(2015, 2021)

y = np.array([
    0.42,
    0.43,
    0.41,
    0.45,
    0.47,
    0.48
])

pendiente_observada = np.polyfit(x, y, 1)[0]

rng = np.random.default_rng(42)

pendientes_perm = []

for _ in range(10000):

    y_perm = rng.permutation(y)

    pendiente = np.polyfit(x, y_perm, 1)[0]

    pendientes_perm.append(pendiente)

pendientes_perm = np.array(pendientes_perm)

p_valor = np.mean(
    np.abs(pendientes_perm) >= abs(pendiente_observada)
)

print("Pendiente observada:", pendiente_observada)
print("p-valor:", p_valor)

plt.hist(pendientes_perm, bins=40)

plt.axvline(
    pendiente_observada,
    linestyle="--",
    linewidth=2
)

plt.xlabel("Pendiente")
plt.ylabel("Frecuencia")
plt.title("Prueba de permutación de la tendencia")

plt.show()
```

# Una forma de visualizar mentalmente la prueba

Imagina que obtienes:

```
                         ↑
                         |
                resultado observado
                         |
              ███████████|
          ███████████████|
       ███████████████████
    █████████████████████████
------------------------------------
               0
```

La distribución representa:

> "Qué pendientes aparecen cuando rompemos deliberadamente la relación temporal."

La pendiente real:

```
↑
```

es comparada contra ese mundo hipotético.
# Pero aparece un problema enorme: series temporales

Hasta aquí todo parece perfecto.

Pero ahora imagina temperatura diaria:

```
Lunes      20°
Martes     21°
Miércoles  21.5°
Jueves     22°
Viernes    22.1°
```

Los valores cercanos en el tiempo suelen parecerse.

Esto se llama:

# Autocorrelación