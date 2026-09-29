Esto es importante porque suele confundirse.

Un p-value responde aproximadamente:

> **Suponiendo que la hipótesis nula es cierta, ¿qué tan raro sería observar un resultado tan extremo como el obtenido o más?**

Por ejemplo:

p=0.03p=0.03

significa que, bajo la hipótesis nula, un resultado tan extremo como el observado tendría una probabilidad de aproximadamente 3%.

No significa:

> "Hay 3% de probabilidad de que la hipótesis nula sea cierta."

Esa interpretación sería incorrecta.
# Ejemplo de Z y p-value con Python

Primero podemos usar `scipy`.

```
from scipy.stats import norm

z = 1.96

# Probabilidad de estar por encima de 1.96
cola_derecha = 1 - norm.cdf(z)

# Prueba de dos colas
p_value = 2 * cola_derecha

print("Cola derecha:", cola_derecha)
print("p-value:", p_value)
```

Obtendrás aproximadamente:

```
Cola derecha: 0.025
p-value: 0.05
```

Ahora prueba:

```
for z in [1, 1.5, 1.96, 2, 2.58, 3]:
    p = 2 * (1 - norm.cdf(z))
    print(f"Z = {z:.2f}, p = {p:.5f}")
```

Verás cómo, mientras Z se aleja de cero, el p-value disminuye.