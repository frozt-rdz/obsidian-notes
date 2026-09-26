Esta distinción debes aprenderla muy bien.

### Kendall

Pregunta:

> **¿X y Y tienden a aumentar o disminuir juntas?**

Ejemplo:

```
Año ↔ temperatura
```

o:

```
precipitación ↔ vegetación
```

---

### Wilcoxon

Pregunta:

> **¿Hay un cambio sistemático entre dos mediciones relacionadas?**

Ejemplo:

```
antes ↔ después
```
# Una forma de memorizarlo

Piensa:

```
KENDALL
   ↓
RELACIÓN
   ↓
X ↔ Y
```

Mientras que:

```
WILCOXON
   ↓
CAMBIO
   ↓
ANTES ↔ DESPUÉS
```

# Comparación rápida

|Método|¿Qué analiza?|Tipo de datos|
|---|---|---|
|Rangos|Orden de los valores|Numéricos/ordinales|
|Kendall tau|Asociación monotónica|Dos variables|
|Wilcoxon|Cambio entre pares|Dos muestras relacionadas|
# Una mini guía de decisión

Cuando recibas datos, piensa así:

```
                ¿Qué quiero saber?
                       │
          ┌────────────┴────────────┐
          │                         │
     ¿Relación?                ¿Cambio?
          │                         │
          ↓                         ↓
    Kendall tau                Wilcoxon
          │                         │
       X ↔ Y                    Antes ↔ Después
```

Y antes de eso:

```
¿Los datos cumplen bien los supuestos
de los métodos paramétricos?

          │
      ┌───┴───┐
      │       │
     Sí      No / dudoso
      │       │
  Paramétrico No paramétrico
```

# Tu mapa mental de B6

```
                 MÉTODOS NO PARAMÉTRICOS
                          │
             ┌────────────┴────────────┐
             │                         │
          RANGOS                  PRUEBAS
             │                         │
       ┌─────┴─────┐             ┌─────┴──────┐
       │           │             │            │
   ordenar      empates       Kendall      Wilcoxon
       │           │             │            │
       │      promedio de       X ↔ Y      Antes ↔ Después
       │        rangos           │            │
       └───────────┴─────────────┴────────────┘
```

Y la frase que te recomiendo recordar es:

> **Los métodos no paramétricos reducen la dependencia de supuestos de distribución y muchos trabajan con rangos en lugar de hacerlo directamente con la magnitud de los datos.**