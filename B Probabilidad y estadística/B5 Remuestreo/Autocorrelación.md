# ¿Qué es autocorrelación?

En términos sencillos:

> **El valor de hoy tiene relación con el valor de ayer.**

Por ejemplo:

```
Temperatura

20
21
21.2
21.5
22
22.1
```

No son observaciones completamente independientes.

El valor de:

```
22
```

probablemente tiene información relacionada con:

```
22.1
```

porque ocurren cerca en el tiempo.
# Imagínalo como una cadena

Supongamos:

```
A → B → C → D → E
```

Los datos no son independientes.

Más bien:

```
A influye en B
B influye en C
C influye en D
D influye en E
```
# ¿Por qué el bootstrap normal falla aquí?

El bootstrap tradicional hace:

```
A B C D E F G H
```

y puede generar:

```
A D B H C C F A
```

El problema:

```
C → D
```

estaba relacionado temporalmente.

Pero ahora están separados.

Acabamos de destruir parte de la estructura temporal.

# La solución: Bootstrap por bloques

En lugar de seleccionar observaciones individuales:

```
A
B
C
D
E
```

seleccionamos grupos consecutivos:

```
[A B C]
[D E F]
[G H I]
```

Por ejemplo:

```
Bloque 1 = [A B C]
Bloque 2 = [D E F]
Bloque 3 = [G H I]
```

Podemos seleccionar:

```
[D E F]
[A B C]
[A B C]
```

Resultado:

```
D E F A B C A B C
```

De esta forma preservamos parte de la relación entre valores consecutivos.

# ¿Por qué funciona?

Porque dentro del bloque:

```
A B C
```

mantenemos:

```
A está cerca de B
B está cerca de C
```

Eso conserva parte de la dependencia temporal.

En cambio, hacer bootstrap individual podría producir:

```
A F C H B D
```

y destruirla.