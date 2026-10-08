---
tipo: datos
estado: borrador
dificultad: 1
fecha: '2026-10-07'
libreria: python
version: 3.13.9
prerequisitos: []
reto: Earth System Trend Detective
fuentes:
- P.B Bibliografía y plan de lectura
tags:
- space-apps
- bloque-p
- python
- flashcards
bloque: P
subtema: P
dia: 0
orden: 0
prioridad: E
nivel: básico
tiempo_estimado: Soporte distribuido en P1–P5
aliases:
- Datos sintéticos de práctica
---

# Datos sintéticos de práctica

> [!warning] Todo es simulado
> Ninguna cifra es una medición NASA. Las tasas son impuestas para practicar; no uses las salidas como evidencia del sistema terrestre.

Lee por etapas: serie_anual después de P1.3; CSV después de P2.3; figura después de P3.3; serie_mensual después de P4.3; malla después de P5.2. Los notebooks incluyen únicamente los generadores necesarios, idénticos a esta nota. Son soporte suministrado, no ejercicios adicionales.

```mermaid
flowchart LR
    N0["Nivel"]
    N1["Tendencia"]
    N0 --> N1
    N2["Estacionalidad"]
    N1 --> N2
    N3["Variabilidad lenta"]
    N2 --> N3
    N4["Ruido"]
    N3 --> N4
    N5["Serie simulada"]
    N4 --> N5
    classDef core fill:#1f6feb,stroke:#0b3d91,color:#ffffff
    class N3 core
```

Los componentes se suman; el diagrama indica el orden de construcción. La anatomía formal de una serie va en bloque C (nota pendiente). La semilla fija permite repetir ruido pseudoaleatorio; no lo convierte en observación.

| Generador | Salida | Convención |
|---|---|---|
| serie_anual | Lista de 24 valores | 2000–2023; nivel 14 °C; tasa 0.02 °C/año; sin ruido |
| serie_mensual | DataFrame de 864 filas | 288 meses × 3 regiones; 2000–2023; nueve ausencias opcionales |
| malla | Dataset 24×3×4 | 24 meses desde 2000; lat/lon en grados; temperatura degC |

## Serie anual · P1

```python
def serie_anual(n=24, tasa=0.02, nivel=14.0):
    """Serie simulada sin ruido; un valor por año desde 2000, en °C."""
    valores = []  # Lista vacía: iremos añadiendo valores.
    for i in range(n):
        valores.append(nivel + tasa * i)
    return valores
```

## Serie mensual · P4

```python
def serie_mensual(semilla=2026, faltantes=False):
    """Tres regiones simuladas, mensuales, 2000–2023; jamás datos NASA."""
    import numpy as np
    import pandas as pd
    rng = np.random.default_rng(semilla)
    fechas = pd.date_range("2000-01-01", periods=288, freq="MS")
    t = np.arange(288) / 12  # Tiempo en años desde el inicio.
    tablas = []
    for region, tasa in zip(["Costa", "Sierra", "Llanura"], [0.02, 0.04, -0.01]):
        estacion = 2 * np.sin(2 * np.pi * t)
        variacion = 0.12 * np.sin(2 * np.pi * t / 5)
        ruido = rng.normal(0, 0.08, len(t))
        valor = 14 + tasa * t + estacion + variacion + ruido
        if faltantes:
            valor[150::53] = np.nan  # Base 2000–2009 completa.
        tablas.append(pd.DataFrame({"fecha": fechas, "region": region,
                                   "temp_C": valor}))
    return pd.concat(tablas, ignore_index=True)
```

## Malla · P5

```python
def malla(semilla=2026):
    """Dataset simulado mensual: time=24, lat=3, lon=4; temperatura en °C."""
    import numpy as np
    import pandas as pd
    import xarray as xr
    rng = np.random.default_rng(semilla)
    tiempo = pd.date_range("2000-01-01", periods=24, freq="MS")
    lat = np.array([-30.0, 0.0, 30.0])
    lon = np.array([-120.0, -90.0, -60.0, -30.0])
    t = np.arange(24).reshape(24, 1, 1) / 12
    tasas = np.array([[-0.03, -0.01, 0.01, 0.03]] * 3)
    valor = 14 + t * tasas + 0.3 * np.sin(2 * np.pi * t)
    valor = valor + rng.normal(0, 0.01, (24, 3, 4))
    ds = xr.Dataset({"temp": (("time", "lat", "lon"), valor)},
                    coords={"time": tiempo, "lat": lat, "lon": lon})
    ds.attrs["origen"] = "simulado"
    ds["temp"].attrs["units"] = "degC"
    ds["lat"].attrs["units"] = "degrees_north"
    ds["lon"].attrs["units"] = "degrees_east"
    return ds
```

## CSV sencillo · P2

Tres observaciones simuladas; el campo vacío de 2001 es ausencia. Los ejercicios escriben este texto embebido.

```csv
anio,temp_C
2000,14.0
2001,
2002,14.4
```

## Comprobaciones de soporte · después de P5

```python
a=serie_anual()
b=serie_mensual(faltantes=True)
ds=malla()
assert len(a)==24, "Veinticuatro valores"
assert len(b)==864 and b["temp_C"].isna().sum()==9, "Tres ausencias por región"
assert b.equals(serie_mensual(faltantes=True)), "Repetibilidad"
assert ds["temp"].shape==(24,3,4), "Tiempo, latitud, longitud"
assert ds.attrs["origen"]=="simulado", "Procedencia explícita"
```

![[fig_PD_componentes.png]]

Componentes simulados: la temperatura combina nivel, tendencia, ciclo estacional, variabilidad lenta y ruido.

> [!tip]- Código de figura · ampliación o soporte
> Ejecuta desde assets; para P5 carga malla de P.D. tight_layout ajusta márgenes; savefig exporta; close libera memoria.
> ```python
> import numpy as np
> import matplotlib.pyplot as plt
> rng = np.random.default_rng(2026)
> t = np.arange(120)/12
> tendencia = 0.02*t
> estacion = 2*np.sin(2*np.pi*t)
> variabilidad = 0.12*np.sin(2*np.pi*t/5)
> ruido = rng.normal(0,0.08,120)
> fig, ejes = plt.subplots(2, 1, figsize=(6, 4), sharex=True)
> ejes[0].plot(t, 14+tendencia+estacion+variabilidad+ruido, color="#0072B2")
> ejes[0].set(ylabel="Temperatura [°C]", title="Componentes de una serie simulada")
> ejes[1].plot(t, tendencia, label="Tendencia", color="#D55E00")
> ejes[1].plot(t, variabilidad, label="Variabilidad", color="#009E73")
> ejes[1].plot(t, ruido, label="Ruido", color="#0072B2", alpha=0.5)
> ejes[1].set(xlabel="Años desde 2000", ylabel="Contribución [°C]")
> ejes[1].legend(fontsize=8)
> fig.tight_layout()
> fig.savefig("fig_PD_componentes.png", dpi=100, bbox_inches="tight")
> plt.close(fig)
> ```

Las figuras P3 y P4 usan simulaciones mínimas propias para evitar dependencias antes de tiempo. Para datos reales reemplaza el generador por un producto NASA con metadatos, controles de calidad, cobertura y unidades verificadas.

Fuentes: [[P.B Bibliografía y plan de lectura|Bibliografía y plan de lectura]]; diseño original de simulaciones.
