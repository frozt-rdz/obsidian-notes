
La varianza tiene unidades elevadas al cuadrado.

Por eso muchas veces es más fácil interpretar la:

$$\boxed{\text{desviación estándar}}$$

que se obtiene mediante:

$$\sigma=\sqrt{Var(X)}$$

En nuestro ejemplo:

$$\sigma=\sqrt{\frac23}$$
$$\sigma \approx 0.816$$

# Una intuición muy importante

Piensa en dos grupos:

### Grupo A

```
49, 50, 51
```

### Grupo B

```
10, 50, 90
```

Ambos tienen media:

$$50$$

Pero claramente el grupo B está mucho más disperso.

Por tanto:

$$Var(B)>Var(A)$$

y:

$$SD(B)>SD(A)$$

Esto es fundamental:

> **La media nos dice dónde está el centro. La desviación estándar nos dice qué tan dispersos están los datos.**

# Python: varianza y desviación estándar

```
import numpy as np

datos = np.array([49, 50, 51])

media = np.mean(datos)
varianza = np.var(datos)
desviacion = np.std(datos)

print("Media:", media)
print("Varianza:", varianza)
print("Desviación estándar:", desviacion)
```

Ahora:

```
datos = np.array([10, 50, 90])

print("Media:", np.mean(datos))
print("Varianza:", np.var(datos))
print("Desviación estándar:", np.std(datos))
```

La media seguirá siendo:

```
50
```

pero la variabilidad será muchísimo mayor.