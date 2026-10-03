---
tipo: ciencia-tierra
estado: borrador
dificultad: 1
fecha: {{date:YYYY-MM-DD}}
prerequisitos: []
reto:
fuentes: []
tags:
  - space-apps
  - ciencia-tierra
  - flashcards
---

# {{title}}

> [!abstract] Idea clave
> ‹Qué es el fenómeno o proceso, en una frase.›

> [!question] ¿Qué pregunta responde?
> ‹¿Por qué ocurre, cómo cambia, qué provoca?›

> [!quote]- En 30 segundos (versión hablada)
> ‹Explicación oral para cualquier público.›

## Intuición

‹Analogía cotidiana del proceso.›

## Sistema: causas, proceso y efectos

```mermaid
flowchart LR
    subgraph CAUSAS["Forzantes"]
        F1["‹forzante 1›"]
        F2["‹forzante 2›"]
    end
    subgraph PROCESO["Proceso"]
        P["{{title}}"]
    end
    subgraph EFECTOS["Efectos"]
        E1["‹efecto 1›"]
        E2["‹efecto 2›"]
    end
    F1 -- "aumenta" --> P
    F2 -- "reduce" --> P
    P -- "provoca" --> E1
    P -- "modifica" --> E2
    E2 -. "retroalimentación" .-> F1
    classDef core fill:#1f6feb,stroke:#0b3d91,color:#ffffff
    class P core
```

## Descripción cuantitativa

$$
\text{‹ecuación o ley›}
$$

| Símbolo | Significa | Unidades |
|:-:|---|:-:|
| $‹a›$ | ‹…› | ‹…› |
| $‹b›$ | ‹…› | ‹…› |

> [!info] En palabras
> ‹Qué relación física expresa y qué pasa si una variable cambia.›

## Escalas

| Escala | Valor típico | Comentario |
|---|---|---|
| Espacial | ‹m, km, global› | ‹…› |
| Temporal | ‹horas, estaciones, décadas› | ‹…› |
| Magnitud | ‹orden de magnitud› | ‹…› |

## Ejemplo numérico

**Situación:** ‹caso concreto con números›

$$
\begin{aligned}
\text{‹cantidad›} &= \text{‹sustitución con unidades›} \\
&= \text{‹resultado con unidades›}
\end{aligned}
$$

> [!success] ¿Tiene sentido?
> ‹Compara el orden de magnitud con valores reales.›

## Cálculo en Python

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 200)      # ‹unidad›
y = ...                          # ecuación del proceso
plt.plot(t, y)
plt.xlabel("‹variable› (‹unidad›)"); plt.ylabel("‹variable› (‹unidad›)")
plt.title("‹título›"); plt.grid(True); plt.show()
```

## Cómo se observa desde el espacio

| Variable | Misión o producto | Qué detecta |
|---|---|---|
| ‹…› | ‹…› | ‹…› |
| ‹…› | ‹…› | ‹…› |

## Incertidumbre y factores de confusión

> [!warning] Cuidado
> ‹Otro proceso que produce la misma señal, ciclo natural que se confunde con tendencia, límite de la medición.›

- [ ] Variabilidad natural vs tendencia
- [ ] Ciclo estacional o anual
- [ ] Efectos locales vs globales
- [ ] Sesgos del instrumento

## Impacto y relevancia

‹Por qué importa: clima, agua, agricultura, salud, riesgos.›

## Aplicación en Space Apps

**Reto:** ‹nombre› · **Pregunta:** ¿‹…›?

```mermaid
flowchart LR
    Q["Pregunta del reto"] --> V["Variable observable"]
    V --> D["Producto NASA"]
    D --> A["Análisis de tendencia o anomalía"]
    A --> I{"¿Coincide con la física esperada?"}
    I -- "sí" --> C["Comunicar impacto"]
    I -- "no" --> V
```

## Conexiones

```mermaid
flowchart LR
    A["‹Proceso previo›"] -- "alimenta" --> C(("{{title}}"))
    C -- "influye en" --> B["‹Proceso siguiente›"]
    C -- "se mide con" --> S["‹Sensor o producto›"]
    C -. "se confunde con" .-> X["‹Fenómeno parecido›"]
    classDef core fill:#1f6feb,stroke:#0b3d91,color:#ffffff
    class C core
```

Enlaces: [[‹Proceso previo›]] → **{{title}}** → [[‹Proceso siguiente›]]

## Flashcards

¿Qué es {{title}}?::‹respuesta›
¿Qué lo provoca?::‹respuesta›
¿Cómo se mide desde el espacio?::‹respuesta›

## Autoevaluación

- [ ] Explico el proceso sin mirar la nota
- [ ] Nombro causas, efectos y una retroalimentación
- [ ] Manejo unidades y órdenes de magnitud
- [ ] Sé qué producto NASA lo observa
- [ ] Distingo tendencia de variabilidad natural

## Fuentes

- ‹enlace o referencia›
