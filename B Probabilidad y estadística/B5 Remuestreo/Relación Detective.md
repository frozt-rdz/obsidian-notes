Supongamos que tienes:

```
Año
↓
NDVI
```

y descubres:

```
NDVI ↑
```

No deberías detenerte en:

> "Encontré una pendiente positiva."

Puedes hacer un análisis más robusto:

### Paso 1 — Calcular la tendencia

```
pendiente = 0.015
```

### Paso 2 — Bootstrap

Construyes un:

```
IC 95% de la pendiente
```
Pregunta:

> ¿Qué tan incierta es la pendiente?

### Paso 3 — Permutación

Destruyes la asociación:

```
Año ↔ NDVI
```

y preguntas:

> ¿Una pendiente de esta magnitud aparece fácilmente por azar?
> 
### Paso 4 — Comprobar autocorrelación

Si:

```
NDVI(t)
```

está relacionado con:

```
NDVI(t-1)
```

entonces el bootstrap ordinario puede ser inadecuado.

### Paso 5 — Bootstrap por bloques

Mantienes grupos consecutivos:

```
2018 2019 2020
```

en lugar de separar completamente las observaciones.