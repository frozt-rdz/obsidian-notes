## ¿Qué significa "no paramétrico"?

Supongamos que tenemos las temperaturas:

```
20, 21, 22, 23, 24, 25
```

Un método paramétrico podría asumir que los datos siguen aproximadamente una **distribución normal**.

Pero ahora imagina:

```
20, 21, 22, 23, 24, 80
```

Ese `80` es un valor extremadamente grande respecto a los demás.

Un método que dependa mucho de la **media** puede verse bastante afectado.

Los métodos no paramétricos muchas veces hacen algo diferente:

```
20 → rango 1
21 → rango 2
22 → rango 3
23 → rango 4
24 → rango 5
80 → rango 6
```

Ya no importa tanto que 80 esté muy lejos de 24. Para el método, lo importante es que:

> **80 es el valor más grande.**

Por eso los métodos basados en rangos pueden ser menos sensibles a valores extremos.
# Las dos ideas que debes recordar

Para este tema basta con recordar:

### Métodos paramétricos

Trabajan principalmente con:

```
valores → medias → varianzas → distribuciones
```

### Métodos no paramétricos

Trabajan mucho con:

```
valores → orden → rangos
```

Por ejemplo:

```
Datos:
8   3   10   5

Ordenados:
3   5   8   10

Rangos:
1   2   3   4
```

# ¿Cuándo usar métodos no paramétricos?

Son especialmente útiles cuando:

- los datos no parecen normales;
- hay pocos datos;
- tenemos valores ordinales;
- existen valores atípicos;
- no estamos seguros de que los supuestos de una prueba paramétrica se cumplan.

Pero cuidado:

> **"No paramétrico" no significa "no tiene supuestos".**

Cada prueba sigue teniendo condiciones que debemos considerar.