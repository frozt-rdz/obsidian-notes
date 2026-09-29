La correlación mide:

> **qué tan fuerte es la relación lineal entre dos variables y en qué dirección.**

La correlación de Pearson suele representarse mediante:

$$r$$

y está siempre entre:

$$−1≤r≤1$$
# Interpretación de la correlación

### $r=1$

Relación lineal positiva perfecta.

```
y
|          *
|       *
|    *
| *
+-------------- x
```

---

### $r=-1$

Relación lineal negativa perfecta.

```
y
| *
|    *
|       *
|          *
+-------------- x
```

---

### $r\approx0$

No existe una relación lineal clara.
# Ejemplos

Podemos pensar de forma aproximada:

|Correlación|Interpretación|
|---|---|
|1.00|positiva perfecta|
|0.90|positiva muy fuerte|
|0.70|positiva considerable|
|0.40|positiva moderada|
|0.10|positiva muy débil|
|0|sin relación lineal|
|-0.40|negativa moderada|
|-0.90|negativa muy fuerte|
|-1.00|negativa perfecta|

**Importante:** estos rangos son una guía práctica, no una ley universal. El significado depende del contexto.
# Covarianza vs correlación

Esta distinción es fundamental.

### Covarianza

Te dice:

> “¿Se mueven juntas?”

Pero su valor depende de las unidades.

### Correlación

Te dice:

> “¿Qué tan fuerte es su relación lineal?”

Y está normalizada entre:

$$1 \text{ y } 1$$

Por eso la correlación suele ser mucho más fácil de interpretar.
# Fórmula de correlación

La relación entre ambas es:
$$\rho_{XY} = \frac{Cov(X,Y)} {\sigma_X\sigma_Y}$$

Es decir:

$$\boxed{ \text{correlación} = \frac{\text{covarianza}} {\text{desviación X}\times\text{desviación Y}} }$$
# ¡Cuidado! Correlación no significa causalidad

Este punto es **importantísimo en ciencia de datos**.

Supongamos que encontramos:

r=0.95r=0.95

entre:

```
ventas de helado
```

y:

```
personas que usan protector solar
```

Eso no significa necesariamente:

> “Comprar helado provoca usar protector solar”.

Puede existir una tercera variable:

```
temperatura
```

Cuando hace calor:

```
temperatura ↑
      ↓
ventas de helado ↑

temperatura ↑
      ↓
uso de protector solar ↑
```

Las dos variables están relacionadas, pero una no necesariamente provoca la otra.
# Un ejemplo muy útil para tu preparación de ciencia de datos

Supón que tienes sensores de una estación meteorológica:

|Temperatura|Humedad|
|---|---|
|20|80|
|22|75|
|24|70|
|26|63|
|28|58|

Probablemente encontraríamos:

r<0r<0

porque:

```
temperatura ↑
humedad ↓
```

Esto te permite detectar patrones rápidamente.