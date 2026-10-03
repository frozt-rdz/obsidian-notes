---
tipo: investigacion
estado: por-leer
relevancia: 3
fecha: {{date:YYYY-MM-DD}}
autores:
anio:
fuente:
doi:
enlace:
reto:
tags:
  - space-apps
  - investigacion
---

# {{title}}

> [!abstract] En una frase
> ‹Qué hicieron y qué encontraron.›

| Campo | Dato |
|---|---|
| Autores | ‹…› |
| Año y fuente | ‹…› |
| DOI o enlace | ‹…› |
| Tipo | ‹artículo, informe, documentación, tesis› |
| Datos NASA usados | ‹…› |

## Pregunta e hipótesis

> [!question] Pregunta de investigación
> ‹¿…?›

**Hipótesis:** ‹…›

## Estructura del estudio

```mermaid
flowchart LR
    Q["Pregunta"] --> D["Datos"] --> M["Método"] --> R["Resultados"] --> C["Conclusión"]
    M -. "supuesto" .-> S["‹supuesto clave›"]
    R -. "limitación" .-> L["‹limitación›"]
    D -. "sesgo posible" .-> B["‹sesgo›"]
    classDef warn fill:#b62324,stroke:#6e1516,color:#ffffff
    class L,B warn
```

## Método

‹Qué técnica usaron y por qué.›

## Datos

| Variable | Fuente | Periodo | Resolución |
|---|---|---|---|
| ‹…› | ‹…› | ‹…› | ‹…› |

## Resultados clave

1. ‹Resultado con cifra›
2. ‹Resultado con cifra›
3. ‹Resultado con cifra›

## Evaluación crítica

> [!success] Fortalezas
> ‹…›

> [!warning] Debilidades y supuestos
> ‹…›

> [!question] Preguntas que me quedan
> ‹…›

## Qué puedo reutilizar

- [ ] ‹Método o técnica›
- [ ] ‹Dato o producto›
- [ ] ‹Figura o idea de visualización›
- [ ] ‹Referencia para citar›

## Citas útiles

Solo fragmentos cortos, con página:

- «‹fragmento breve›» (p. ‹…›)

## Conexiones

```mermaid
flowchart LR
    T(("{{title}}"))
    T -- "usa" --> M["‹Método o concepto›"]
    T -- "apoya" --> H["‹Hipótesis de mi proyecto›"]
    T -- "contradice o matiza" --> O["‹Otro estudio›"]
    T -- "usa datos de" --> D["‹Producto NASA›"]
    classDef core fill:#1f6feb,stroke:#0b3d91,color:#ffffff
    class T core
```

Enlaces: [[‹Concepto relacionado›]] · [[‹Otro paper›]]

## Cita

```text
‹Formato APA u otro›
```

## Autoevaluación

- [ ] Explico la pregunta y el método en 30 segundos
- [ ] Sé qué datos usaron y de dónde salen
- [ ] Puedo nombrar una limitación seria
- [ ] Sé qué parte usaría en mi proyecto
- [ ] Verifiqué que la fuente es confiable y citable
