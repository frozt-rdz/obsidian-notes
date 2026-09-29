La esperanza nos dice:

> "¿Cuál es el centro?"

Pero todavía queremos saber:

> "¿Qué tanto se dispersan los valores alrededor del centro?"

Para eso usamos la **varianza**.

Se representa:

$$Var(X)$$

o:

$$\sigma^2$$

La fórmula es:

$$Var(X)=E[(X-\mu)^2]$$

En palabras:

1. calculamos la diferencia respecto al promedio;
2. la elevamos al cuadrado;
3. promediamos esas diferencias.
# Ejemplo sencillo de varianza

Considera:

```
4, 5, 6
```

La media es:

$$\mu=5$$

Diferencias:

```
4 - 5 = -1
5 - 5 = 0
6 - 5 = 1
```

Elevamos al cuadrado:

```
1
0
1
```

Promediamos:

$$Var(X)=\frac{1+0+1}{3} $$
​​$$Var(X)=\frac23$$
# ¿Por qué elevamos al cuadrado?

Porque si simplemente sumáramos las diferencias:

$$-1+0+1=0$$

parecería que no existe variación.

El cuadrado elimina los signos negativos:

$$(-1)^2=1 $$
$$1^2=1$$

Así podemos medir cuánto se alejan los datos.