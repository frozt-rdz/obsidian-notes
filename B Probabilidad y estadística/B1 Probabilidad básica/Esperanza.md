
La **esperanza** es básicamente el valor promedio que esperaríamos obtener si repitiéramos el experimento muchísimas veces.
Para una variable aleatoria discreta X con [función de probabilidad](https://es.wikipedia.org/wiki/Funci%C3%B3n_de_probabilidad "Función de probabilidad") ${\displaystyle \operatorname {P} [X=x_{i}]}$ con $i=1,2,…,n$ la esperanza se define como
![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==)$${\displaystyle \operatorname {E} [X]=\sum _{i=1}^{n}x_{i}\operatorname {P} [X=x_{i}]}$$
Se representa:

$$E[X]$$

o también:

$$\mu$$

---

## Ejemplo del dado

Tenemos:

|X|Probabilidad|
|---|---|
|1|1/6|
|2|1/6|
|3|1/6|
|4|1/6|
|5|1/6|
|6|1/6|

La esperanza es:

$$E[X] = 1\frac16+ 2\frac16+ 3\frac16+ 4\frac16+ 5\frac16+ 6\frac16$$

Factorizamos:

$$E[X] = \frac{1+2+3+4+5+6}{6} $$
$$E[X]=\frac{21}{6} $$
$$\boxed{E[X]=3.5}
$$
Esto **no significa** que puedas lanzar el dado y obtener 3.5.

Significa que si haces muchas tiradas, el promedio tenderá hacia aproximadamente:

$$3.5$$

# Python para la esperanza

```
import numpy as np

valores = np.array([1, 2, 3, 4, 5, 6])
probabilidades = np.array([
    1/6, 1/6, 1/6, 1/6, 1/6, 1/6
])

esperanza = np.sum(valores * probabilidades)

print("Esperanza:", esperanza)
```

Resultado:

```
Esperanza: 3.5
```