Esto ya empieza a acercarse mucho al problema del "Detective".

Supongamos:

```
Año       Temperatura
2019      20.1
2020      20.4
2021      20.5
2022      20.8
2023      21.0
```

Calculamos una pendiente:

```
°C por año
```

Pero queremos saber:

> ¿Qué tan incierta es esa pendiente?
> Podemos hacer bootstrap.

```
import numpy as np

x = np.array([2019, 2020, 2021, 2022, 2023])
y = np.array([20.1, 20.4, 20.5, 20.8, 21.0])

rng = np.random.default_rng(42)

pendientes = []

for _ in range(10000):

    indices = rng.choice(len(x), size=len(x), replace=True)

    x_boot = x[indices]
    y_boot = y[indices]

    pendiente = np.polyfit(x_boot, y_boot, 1)[0]

    pendientes.append(pendiente)

pendientes = np.array(pendientes)

ic = np.percentile(pendientes, [2.5, 97.5])

print("Pendiente original:",
      np.polyfit(x, y, 1)[0])

print("IC 95%:", ic)
```