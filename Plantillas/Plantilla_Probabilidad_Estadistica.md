---
tipo: estadistica
estado: borrador
dificultad: 1
fecha: {{date:YYYY-MM-DD}}
prerequisitos: []
reto:
fuentes: []
tags:
  - space-apps
  - estadistica
  - flashcards
---

# {{title}}

> [!abstract] Idea clave
> ‹Una sola frase, sin jerga.›

> [!question] ¿Qué pregunta responde?
> ‹¿…?›

> [!quote]- En 30 segundos (versión hablada para el pitch)
> ‹Cómo lo explicarías en voz alta a alguien que no sabe estadística.›

## Intuición

‹Situación simple: dados, monedas, sensor, temperatura, lluvia… sin fórmulas todavía.›

```mermaid
flowchart TD
    C(("{{title}}"))
    C -- "responde a" --> Q["¿‹pregunta›?"]
    C -- "necesita" --> E["‹datos de entrada›"]
    C -- "produce" --> S["‹resultado›"]
    S -- "se interpreta como" --> I["‹significado›"]
    C -- "falla cuando" --> L["‹limitación›"]
    C -- "se parece a" --> R["‹concepto vecino›"]
    R -. "pero difiere en" .-> D["‹diferencia›"]
    classDef core fill:#1f6feb,stroke:#0b3d91,color:#ffffff
    classDef warn fill:#b62324,stroke:#6e1516,color:#ffffff
    class C core
    class L warn
```

**Conclusión intuitiva:** ‹…›

## Fórmula

$$
\text{‹fórmula›}
$$

| Símbolo | Significa |
|:-:|---|
| $‹a›$ | ‹…› |
| $‹b›$ | ‹…› |

> [!info] En palabras
> ‹Traduce la fórmula: qué operación hace primero, qué hace después y por qué.›

## Supuestos

| Supuesto | Por qué importa | Cómo lo compruebo |
|---|---|---|
| ‹independencia› | ‹…› | ‹…› |
| ‹normalidad, linealidad, etc.› | ‹…› | ‹…› |

## Ejemplo a mano

Datos (los mismos se usan en el código):

| Dato | Valor |
|---|---:|
| ‹…› | ‹…› |
| ‹…› | ‹…› |

1. Primero: $\text{‹paso 1›}$
2. Después: $\text{‹paso 2›}$
3. Resultado:

$$
\boxed{\text{‹resultado›}}
$$

## Código

```python
import numpy as np
import matplotlib.pyplot as plt

datos = np.array([...])          # mismos datos del ejemplo a mano

resultado = ...                  # cálculo
print(f"resultado = {resultado:.4f}")

plt.plot(datos, "o-")            # siempre grafica: un número solo engaña
plt.title("‹título›")
plt.xlabel("‹x›"); plt.ylabel("‹y›")
plt.show()
```

Salida esperada: `‹valor›` (debe coincidir con el ejemplo a mano).

- `‹línea clave›` → ‹qué hace›

## Interpretación

> [!success] Qué significa el resultado
> ‹El número en palabras y dentro del contexto del problema.›

## Trampas y límites

> [!warning] Error común
> ❌ ‹interpretación incorrecta› → ✅ ‹interpretación correcta›

No permite afirmar que: ‹…›

Revisa en datos de la Tierra:

- [ ] Estacionalidad (¿la tendencia es solo el ciclo anual?)
- [ ] Autocorrelación temporal (los puntos no son independientes)
- [ ] Datos faltantes, nubes, huecos
- [ ] Resolución espacial y temporal
- [ ] Unidades y escala

## Aplicación en Space Apps

**Reto:** ‹nombre› · **Pregunta:** ¿‹…›?

| Producto | Variable | Unidades | Cobertura | Resolución | Enlace |
|---|---|---|---|---|---|
| ‹…› | ‹…› | ‹…› | ‹…› | ‹…› | ‹…› |
| ‹…› | ‹…› | ‹…› | ‹…› | ‹…› | ‹…› |

```mermaid
flowchart LR
    subgraph DATOS["1 · Datos NASA"]
        A1["‹Producto A›"]
        A2["‹Producto B›"]
    end
    subgraph PREP["2 · Preparación"]
        B1["Alinear fechas y resolución"]
        B2["Enmascarar nubes y huecos"]
        B3["Quitar estacionalidad"]
    end
    subgraph ANAL["3 · Análisis"]
        C1["{{title}}"]
    end
    subgraph SAL["4 · Salida"]
        D1["‹métrica›"]
        D2["Gráfico"]
    end
    A1 & A2 --> B1 --> B2 --> B3 --> C1
    C1 --> D1 & D2
    D1 --> V{"¿Tiene sentido físico?"}
    V -- "sí" --> P["Comunicar en el pitch"]
    V -- "no" --> B1
    classDef core fill:#1f6feb,stroke:#0b3d91,color:#ffffff
    class C1 core
```

## Conexiones

```mermaid
flowchart LR
    P1["‹Prerrequisito›"] -- "es base de" --> C(("{{title}}"))
    C -- "se generaliza en" --> N1["‹Siguiente›"]
    C -- "se usa en" --> A["‹Aplicación NASA›"]
    C -- "se calcula con" --> H["‹Función de Python›"]
    C -. "no confundir con" .-> X["‹Concepto parecido›"]
    classDef core fill:#1f6feb,stroke:#0b3d91,color:#ffffff
    class C core
```

Enlaces: [[‹Prerrequisito›]] → **{{title}}** → [[‹Siguiente›]]

## Flashcards

¿Qué mide {{title}}?::‹respuesta›
¿Qué supuestos necesita {{title}}?::‹respuesta›
Fórmula de {{title}}::$\text{‹fórmula›}$

## Autoevaluación

- [ ] Lo explico sin mirar la nota
- [ ] Sé qué significa cada símbolo
- [ ] Lo resuelvo a mano y en Python con el mismo resultado
- [ ] Sé interpretar el resultado y una limitación
- [ ] Sé qué supuestos exige
- [ ] Sé cómo aplicarlo a un dato NASA

## Fuentes

- ‹enlace o referencia›

---

## Módulos opcionales (copia solo si aportan)

> [!example]- Casos o comportamiento visual
> **Caso 1 — ‹nombre›:** ‹descripción› → $\text{‹resultado›}$
> **Caso 2 — ‹nombre›:** ‹descripción› → $\text{‹resultado›}$

> [!note]- Derivación
> $$
> \text{‹paso a paso›}
> $$

> [!tip]- ¿Qué método uso?
> ```mermaid
> flowchart TD
>     S{"¿‹pregunta 1›?"}
>     S -- "sí" --> M1["‹Método A›"]
>     S -- "no" --> T{"¿‹pregunta 2›?"}
>     T -- "sí" --> M2["‹Método B›"]
>     T -- "no" --> M3["‹Método C›"]
> ```
