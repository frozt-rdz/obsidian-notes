Ahora llegamos a un concepto especialmente importante para ciencia de datos.

La **covarianza** intenta responder:

> **¿Dos variables tienden a cambiar juntas?**

Supongamos:

|Horas estudiadas|Calificación|
|---|---|
|1|60|
|2|65|
|3|72|
|4|80|
|5|88|

Aquí parece que:

> cuando aumentan las horas de estudio, también aumenta la calificación.

Existe una covarianza positiva.

# Tipos de covarianza

### Covarianza positiva

Cuando una variable aumenta y la otra tiende a aumentar.

$$Cov(X,Y)>0$$
Ejemplo:

```
horas de estudio ↑
calificación ↑
```

---

### Covarianza negativa

Cuando una aumenta mientras la otra tiende a disminuir.

$$Cov(X,Y)<0$$

Ejemplo hipotético:

```
horas viendo televisión ↑
horas estudiando ↓
```

---

### Covarianza cercana a cero

No hay una relación lineal evidente.

$$Cov(X,Y) \approx 0$$
# Fórmula de covarianza

Para variables aleatorias:

$$Cov(X,Y)=E[(X-\mu_X)(Y-\mu_Y)]$$

Otra forma equivalente:

$$Cov(X,Y)=E[XY]-E[X]E[Y]$$

La idea intuitiva es muy importante:

> Medimos cómo se mueven X e Y con respecto a sus respectivas medias.

# Ejemplo visual

Imagina estos puntos:

```
y
|
|            *
|         *
|      *
|   *
| *
+---------------- x
```

Existe una tendencia ascendente.

Por tanto:

$$Cov(X,Y)>0$$

Ahora:

```
y
|
| *
|    *
|       *
|          *
|             *
+---------------- x
```

Existe una tendencia descendente.

Entonces:

$$Cov(X,Y)<0$$
# Python para covarianza

```
import numpy as np

horas = np.array([1, 2, 3, 4, 5])
calificaciones = np.array([60, 65, 72, 80, 88])

covarianza = np.mean(
    (horas - np.mean(horas)) *
    (calificaciones - np.mean(calificaciones))
)

print("Covarianza:", covarianza)
```

Obtendrás una covarianza positiva.

También existe:

```
np.cov(horas, calificaciones)
```

pero aquí hay una cuestión importante:

`np.cov()` utiliza por defecto **covarianza muestral**, mientras que nuestra fórmula anterior usa una división por nn, es decir, covarianza poblacional.

Para estudiar los conceptos primero, conviene entender la fórmula manual.

# ¿Cuál es el problema de la covarianza?

La magnitud de la covarianza depende de las unidades.

Por ejemplo:

```
peso = kilogramos
altura = metros
```

Si cambias:

```
metros → centímetros
```

la covarianza cambia de magnitud.

Eso dificulta comparar relaciones entre diferentes conjuntos de datos.

Aquí aparece la **correlación**.