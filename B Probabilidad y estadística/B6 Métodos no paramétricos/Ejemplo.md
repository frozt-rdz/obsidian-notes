Supongamos que tienes datos de 10 años:

```
años = [2015, 2016, 2017, 2018, 2019,
        2020, 2021, 2022, 2023, 2024]

temperatura = [22.1, 22.3, 22.2, 22.5, 22.7,
               22.8, 23.0, 22.9, 23.2, 23.4]
```

Una pregunta podría ser:

> ¿La temperatura tiene una tendencia creciente con el tiempo?

Aquí:

```
Año ↔ Temperatura
```

Usaríamos Kendall.

# ¿Qué pasa si tenemos valores repetidos?

```
temperatura = [
    22.1, 22.3, 22.3, 22.5, 22.5,
    22.8, 22.8, 22.9, 23.2, 23.4
]
```

Tenemos:

```
22.3
22.3

22.5
22.5

22.8
22.8
```

Son **empates**.

No hay que entrar en pánico.

Kendall está diseñado para poder trabajar con empates.

```
tau, p = kendalltau(años, temperatura)

print(tau)
print(p)
```.