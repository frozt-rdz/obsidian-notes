---
tipo: concepto
estado: borrador
dificultad: 1
fecha: {{date:YYYY-MM-DD}}
prerequisitos: []
reto:
fuentes: []
tags:
  - space-apps
  - flashcards
---

# {{title}}

> [!abstract] Idea clave
> ‹Una sola frase, sin jerga.›

> [!question] ¿Qué problema resuelve o qué pregunta responde?
> ‹¿…?›

> [!quote]- En 30 segundos (versión hablada para el pitch)
> ‹Cómo lo explicarías en voz alta a alguien que no conoce el tema.›

## Intuición

‹Analogía o situación cotidiana. Sin fórmulas ni tecnicismos todavía.›

```mermaid
flowchart TD
    C(("{{title}}"))
    C -- "responde a" --> Q["¿‹pregunta›?"]
    C -- "está formado por" --> P["‹parte o componente›"]
    C -- "produce" --> R["‹resultado o efecto›"]
    C -- "se usa cuando" --> U["‹situación›"]
    C -- "falla cuando" --> L["‹limitación›"]
    C -- "se parece a" --> V["‹concepto vecino›"]
    V -. "pero difiere en" .-> D["‹diferencia›"]
    classDef core fill:#1f6feb,stroke:#0b3d91,color:#ffffff
    classDef warn fill:#b62324,stroke:#6e1516,color:#ffffff
    class C core
    class L warn
```

**Conclusión intuitiva:** ‹…›

## Definición

> [!note] Definición
> ‹Definición precisa en una o dos frases.›

Partes o componentes:

- **‹parte 1›**: ‹qué es y qué hace›
- **‹parte 2›**: ‹…›
- **‹parte 3›**: ‹…›

## Cómo funciona

1. ‹Paso 1›
2. ‹Paso 2›
3. ‹Paso 3›

## Ejemplo

> [!example] ‹Nombre del ejemplo›
> **Situación:** ‹…›
> **Qué ocurre:** ‹…›
> **Resultado:** ‹…›

## Errores y límites

> [!warning] Error común
> ❌ ‹idea incorrecta› → ✅ ‹idea correcta›

No aplica cuando: ‹…›

## Aplicación en Space Apps

**Reto:** ‹nombre› · **Pregunta:** ¿‹…›?

```mermaid
flowchart LR
    P["Problema del reto"] --> D["Datos NASA"]
    D --> A["{{title}}"]
    A --> V{"¿Resultado con sentido?"}
    V -- "sí" --> C["Comunicar en el pitch"]
    V -- "no" --> D
    classDef core fill:#1f6feb,stroke:#0b3d91,color:#ffffff
    class A core
```

## Conexiones

```mermaid
flowchart LR
    A["‹Prerrequisito›"] -- "es base de" --> C(("{{title}}"))
    C -- "lleva a" --> S["‹Siguiente tema›"]
    C -- "se usa en" --> U["‹Aplicación›"]
    C -. "no confundir con" .-> X["‹Concepto parecido›"]
    classDef core fill:#1f6feb,stroke:#0b3d91,color:#ffffff
    class C core
```

Enlaces: [[‹Prerrequisito›]] → **{{title}}** → [[‹Siguiente tema›]]

## Flashcards

¿Qué es {{title}}?::‹respuesta›
¿Cuándo se usa {{title}}?::‹respuesta›
¿Cuál es un error común con {{title}}?::‹respuesta›

## Autoevaluación

- [ ] Lo explico sin mirar la nota
- [ ] Doy un ejemplo propio
- [ ] Reconozco un error común y un límite
- [ ] Sé cómo aplicarlo en un reto

## Fuentes

- ‹enlace o referencia›

---

## Módulos opcionales (copia solo si aportan)

> [!note]- Fórmula
> $$
> \text{‹fórmula›}
> $$
> | Símbolo | Significa |
> |:-:|---|
> | $‹a›$ | ‹…› |

> [!example]- Código
> ```python
> # ‹ejemplo mínimo›
> ```

> [!example]- Tabla comparativa
> | Criterio | ‹A› | ‹B› |
> |---|---|---|
> | ‹criterio 1› | ‹…› | ‹…› |
> | ‹criterio 2› | ‹…› | ‹…› |

> [!tip]- Mapa mental de repaso
> ```mermaid
> mindmap
>   root((‹Concepto›))
>     Qué es
>       ‹definición›
>     Cómo funciona
>       ‹paso›
>     Cuándo usarlo
>       ‹caso›
>     Cuándo NO
>       ‹límite›
> ```
