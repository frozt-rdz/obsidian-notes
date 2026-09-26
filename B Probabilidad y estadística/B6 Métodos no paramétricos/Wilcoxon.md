Ahora pasamos a otro concepto.

Wilcoxon se utiliza para comparar datos cuando una prueba t tradicional puede no ser apropiada.

Hay dos situaciones que conviene distinguir.

### Wilcoxon signed-rank

Se utiliza típicamente con:

> **datos pareados o relacionados.**

Por ejemplo:

```
Antes      Después
70         75
65         70
80         78
72         77
```

Tenemos a las **mismas personas antes y después**.

La pregunta es:

> ¿El cambio entre antes y después es sistemáticamente diferente de cero?

---

# 16. Ejemplo sencillo de Wilcoxon

Supongamos:

```
Antes:
10, 12, 11, 15, 13

Después:
12, 14, 13, 16, 15
```

Calculamos las diferencias:

```
Después - Antes

2
2
2
1
2
```

Todas son positivas.

Eso sugiere que después tenemos valores mayores.

Wilcoxon analiza los **rangos de las diferencias**, en lugar de depender directamente de la media de esas diferencias como hace una prueba t pareada.

# Wilcoxon en Python

```
from scipy.stats import wilcoxon

antes = [10, 12, 11, 15, 13]
despues = [12, 14, 13, 16, 15]

estadistico, p = wilcoxon(antes, despues)

print("Estadístico:", estadistico)
print("p-value:", p)
```

Podríamos plantear:

$$H_0: \text{no existe un cambio sistemático}$$
$$H_1: \text{sí existe un cambio sistemático}$$

Una interpretación sería:

```
Si p < 0.05:
hay evidencia de un cambio estadísticamente significativo.
```

# ¿Por qué Wilcoxon utiliza rangos?

Imagina que calculamos:

```
Diferencias:

1
2
2
10
100
```

El `100` es enorme.

En una prueba que dependa directamente de los valores puede tener mucha influencia.

Wilcoxon utiliza el orden de las magnitudes:

```
1   → rango 1
2   → rango 2.5
2   → rango 2.5
10  → rango 4
100 → rango 5
```

Por eso los valores extremos pueden tener una influencia relativamente menor.

# ¡Pero cuidado con una cosa!

Es común escuchar:

> "Los métodos no paramétricos no son afectados por valores atípicos."

Eso es demasiado fuerte.

Es mejor decir:

> **Los métodos basados en rangos suelen ser menos sensibles a la magnitud de los valores extremos que métodos basados directamente en los valores.**

Pero un atípico todavía puede afectar:

- los rangos;
- el resultado;
- la interpretación;
- especialmente cuando tenemos pocos datos.
# ¿Qué pasa con los empates en Wilcoxon?

Esto también es importante.

Supongamos:

```
Diferencias:

2
2
2
3
5
```

Tenemos varios valores repetidos.

Wilcoxon también debe manejar esos empates.

SciPy realiza el manejo correspondiente dependiendo de la configuración utilizada.

Por ejemplo:

```
from scipy.stats import wilcoxon

antes = [10, 10, 10, 10, 10]
despues = [12, 12, 12, 13, 15]

resultado = wilcoxon(antes, despues)

print(resultado)
```