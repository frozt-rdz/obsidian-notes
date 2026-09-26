Podemos hacer una simulación de un dado.

```
import random

resultado = random.randint(1, 6)

print("Resultado:", resultado)
```

Cada vez que ejecutes el programa aparecerá algo como:

```
Resultado: 4
```

Pero una sola tirada no nos dice mucho.

Podemos lanzar el dado miles de veces.

```
import random

N = 100000
favorables = 0

for _ in range(N):
    dado = random.randint(1, 6)

    if dado > 4:
        favorables += 1

probabilidad = favorables / N

print("Probabilidad experimental:", probabilidad)
```

Deberías obtener algo parecido a:

```
Probabilidad experimental: 0.333
```

La probabilidad teórica era:

13=0.3333...\frac13=0.3333...

Cuantas más simulaciones hagamos, normalmente más se acercará el resultado experimental al teórico.

Esto es una idea importantísima en ciencia de datos:

> **Podemos utilizar datos observados para aproximar probabilidades.**