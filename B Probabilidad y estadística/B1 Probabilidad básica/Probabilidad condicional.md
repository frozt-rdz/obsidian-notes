Este es uno de los conceptos más importantes.

Supongamos que lanzas un dado.

Pregunta:

> ¿Cuál es la probabilidad de obtener un 6?

Es:

$$P(6)=\frac16$$

Ahora cambiamos la pregunta:

> Si sabemos que salió un número par, ¿cuál es la probabilidad de que haya sido 6?

Ahora ya no consideramos todos los resultados.

Sabemos que:

$$B=\{2,4,6\}$$

Por lo tanto, únicamente quedan:

$$2,4,6$$
De esos tres, uno es 6.

Por tanto:

$$P(6\mid\text{par})=\frac13$$
# Fórmula de probabilidad condicional

La fórmula es:

$$P(A\mid B)= \frac{P(A\cap B)}{P(B)}$$

Se lee:

> “Probabilidad de A dado B”.

El símbolo:

$$\mid$$

significa **“dado que”**.

---

## Ejemplo

Tenemos:

$$A=\text{número mayor que 3} $$$$B=\text{número par}$$

Entonces:

$$A=\{4,5,6\}$$$$
B=\{2,4,6\}$$

La intersección es:

$$A\cap B=\{4,6\}$$

Por tanto:

$$P(A\cap B)=\frac26=\frac13$$

Mientras que:

$$P(B)=\frac36=\frac12$$

Entonces:

$$P(A\mid B) = \frac{1/3}{1/2} = \frac23$$

Por lo tanto:

$$P(A\mid B)=\frac32​$$​# Python para probabilidad condicional

Podemos comprobarlo mediante simulación:

```
import random

N = 100000

casos_par = 0
casos_mayor3_y_par = 0

for _ in range(N):
    dado = random.randint(1, 6)

    if dado % 2 == 0:
        casos_par += 1

        if dado > 3:
            casos_mayor3_y_par += 1

probabilidad_condicional = casos_mayor3_y_par / casos_par

print(probabilidad_condicional)
```

Resultado aproximado:

```
0.666
```

que se acerca a:

$$\frac23$$​