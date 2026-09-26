Ahora viene uno de los métodos que probablemente te resulte más interesante para análisis de datos.

## ¿Qué pregunta responde?

Kendall's tau intenta responder:

> **¿Cuando X aumenta, Y también tiende a aumentar?**

Es una medida de **asociación entre dos variables ordinales o continuas basada en el orden de los datos**.

Por ejemplo:

|Año|Temperatura|
|---|---|
|2010|22|
|2011|23|
|2012|24|
|2013|26|
|2014|27|

Parece existir una tendencia creciente.

Kendall puede detectar esa relación.

# La intuición de Kendall

Supongamos:

```
X = 1, 2, 3, 4
Y = 10, 20, 30, 40
```

Cuando X aumenta:

```
1 → 2 → 3 → 4
```

Y también aumenta:

```
10 → 20 → 30 → 40
```

La relación es perfectamente creciente.

Entonces:

τ=1
## Relación perfectamente decreciente

```
X = 1, 2, 3, 4
Y = 40, 30, 20, 10
```

Cuando X aumenta, Y disminuye.

Entonces:

τ=−1\tau = -1

---

## Sin relación clara
Por ejemplo:

```
X = 1, 2, 3, 4, 5
Y = 20, 5, 40, 10, 25
```

No existe un patrón de orden evidente.

Tau estará cerca de:

```
0
```

# Interpretar Kendall tau

Una forma sencilla de pensarlo:

|τ|Interpretación intuitiva|
|---|---|
|+1|asociación creciente perfecta|
|+0.7|asociación creciente fuerte|
|+0.3|asociación creciente moderada/débil|
|0|sin asociación monotónica clara|
|-0.3|asociación decreciente moderada/débil|
|-0.7|asociación decreciente fuerte|
|-1|asociación decreciente perfecta|

Estos cortes son solamente orientativos. **No existe una tabla universal donde, por ejemplo, 0.7 siempre signifique exactamente "fuerte".**
