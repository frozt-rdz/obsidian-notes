Este es el concepto fundamental para entender todo lo demás.

## Ejemplo

Tenemos:

```
12, 5, 20, 8
```

Ordenamos:

```
5, 8, 12, 20
```

Asignamos rangos:

| Valor | Rango |
| ----- | ----- |
| 5     | 1     |
| 8     | 2     |
| 12    | 3     |
| 20    | 4     |
Entonces:

```
12 → 3
5  → 1
20 → 4
8  → 2
```

# ¿Qué ocurre cuando hay valores repetidos?

Aquí aparece uno de los puntos importantes de B6:

## Empates

Supongamos:

```
5, 8, 8, 12
```

Ordenamos:

```
5, 8, 8, 12
```

Sin empates tendríamos:

```
1, 2, 3, 4
```

Pero los dos `8` ocupan las posiciones 2 y 3.

Por tanto, utilizamos el promedio:

$$\frac{2+3}{2}=2.5$$

Los rangos quedan:

|Valor|Rango|
|---|---|
|5|1|
|8|2.5|
|8|2.5|
|12|4|

Esto es muy importante.

### Regla sencilla

Si varios valores empatan:

> **Todos reciben el promedio de los rangos que ocuparían.**
# Python: calcular rangos

Podemos hacerlo con SciPy.

```
from scipy.stats import rankdata

datos = [12, 5, 20, 8]

rangos = rankdata(datos)

print(rangos)
```

Resultado:

```
[3. 1. 4. 2.]
```

Ahora con empate:

```
datos = [5, 8, 8, 12]

rangos = rankdata(datos)

print(rangos)
```

Resultado:

```
[1.  2.5 2.5 4. ]
```

# ¿Por qué usar rangos?

Imagina dos conjuntos:

```
A = 10, 20, 30, 40, 50
B = 10, 20, 30, 40, 5000
```

El último valor de B es enorme.

Pero sus rangos son:

```
A:
1, 2, 3, 4, 5

B:
1, 2, 3, 4, 5
```

Desde el punto de vista del orden, son iguales.

Esto explica intuitivamente por qué las pruebas basadas en rangos suelen ser menos sensibles a la magnitud de un valor extremo.

# Ejemplo visual de rangos

Prueba este código:

```
from scipy.stats import rankdata

datos = [15, 12, 18, 12, 20]

rangos = rankdata(datos)

for dato, rango in zip(datos, rangos):
    print(f"{dato} → rango {rango}")
```

Obtendrás algo equivalente a:

```
15 → rango 3
12 → rango 1.5
18 → rango 4
12 → rango 1.5
20 → rango 5
```

¿Por qué `12` tiene rango `1.5`?

Porque ocupa:

```
rango 1
rango 2
```

y:

$$\frac{1+2}{2}=1.5$$
