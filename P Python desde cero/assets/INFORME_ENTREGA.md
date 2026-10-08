---
tipo: referencias
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
tiempo_estimado: Consulta
aliases:
- Informe de entrega y verificación
---

# Informe de entrega y verificación

El bloque se escribió directamente en disco. No había una carpeta de destino previa; no se sobrescribió material del usuario. Los libros, las plantillas y las notas de otros bloques se consultaron sin modificarlos. No se ejecutó ningún commit ni push.

## Tiempos reales frente al plan

Los minutos provienen de los encabezados de los ejercicios generados. Las lecturas núcleo están incluidas en los conceptos; no suman tiempo. El notebook contiene los mismos ejercicios y no añade una tanda independiente.

| Día | Ejercicios núcleo | Ejercicios ampliación | Total núcleo / plan | Total ampliación / plan | Cantidad núcleo / ampliación |
|---|---|---|---|---|---|
| 1 | 125 | 150 | 240 / 240 | 240 / 240 | 13 / 8 |
| 2 | 140 | 150 | 240 / 240 | 240 / 240 | 14 / 8 |
| 3 | 140 | 150 | 240 / 240 | 240 / 240 | 14 / 8 |
| 4 | 140 | 150 | 240 / 240 | 240 / 240 | 14 / 8 |
| 5 | 45 | 60 | 240 / 240 | 240 / 240 | 5 / 3 |

P5 incluye proyecto: 95 min núcleo y 120 min ampliación. Total: 60 ejercicios núcleo, 35 de ampliación y 11 etapas de proyecto —5 núcleo y 6 ampliación—. Prueba tú añade 45 microejercicios incluidos en los 75 min diarios de conceptos.

## Libros y lectura

Garcimartín, A. (2022), *Introducción a Python para cálculo científico*; Delgado Quintero, S. (2022), *Aprende Python*, versión del 12 de diciembre. PDF originales intactos. Se identificó solo la inicial A. del primer autor, sin ampliarla por suposición.

| Día | Lectura núcleo incluida | Tiempo | Lectura ampliación | Tiempo |
|---|---|---|---|---|
| 1 | Garcimartín, Python básico §§1–2, pp. 2–3 | 10 min | Delgado Quintero, cap. 3 §3.1 pp. 46–51; cap. 4 §4.1 pp. 100–103; cap. 6 §6.1 pp. 210–213 | 45 min |
| 2 | Garcimartín, Python básico §§3–4, pp. 4–7 | 15 min | Delgado Quintero, cap. 5 §§5.3 y 5.5 pp. 174–178 y 201–205; cap. 6 §6.3 pp. 280–282 | 45 min |
| 3 | Garcimartín, NumPy §§1–2, pp. 22–24 | 15 min | Garcimartín, NumPy §§3–4 pp. 24–25 y matplotlib §§1–2 pp. 26–30; Delgado Quintero, cap. 8 §8.2 pp. 326–330 | 45 min |
| 4 | Delgado Quintero, cap. 8 §8.3.1, pp. 370–373 | 15 min | Delgado Quintero, cap. 8 §8.3.2, pp. 381–385, 422–424 y 427–432 | 45 min |
| 5 | Delgado Quintero, cap. 6 §6.3, pp. 280–282 | 10 min | Delgado Quintero, cap. 6 §§6.3–6.4, pp. 283–291; Garcimartín, Python básico §9, pp. 12–13 | 30 min dentro del repaso de 60 |

Citas, tabla de capítulos y equivalencia de páginas impresas/PDF: [[P.B Bibliografía y plan de lectura|Bibliografía y plan de lectura]].

## Verificación efectuada

- YAML válido en las notas; campos, etiquetas, prerequisitos y nombres comprobados.
- Sin marcadores pendientes; tablas continuas, vallas balanceadas, enlaces existentes con alias y sin wikilinks en nodos Mermaid.
- UTF-8, LF, sin BOM, espacios finales ni saltos triples en las notas.
- 15 conceptos, tres por día; cuerpos de 55–71 líneas, sin contar código ni YAML. Dos recursos visuales distintos como mínimo en cada nota.
- 695 ejecuciones de bloques y soporte, incluyendo 106 soluciones con sus asserts. Tracebacks intencionales reales y salidas de los ejemplos contrastadas.
- Seis notebooks válidos con nbformat, ejecutados con nbclient en copias temporales con soluciones; cantidades, tiempos y comprobaciones coinciden. Copias descartadas.
- Prueba pytest básica aprobada: un test. No se ejecutaron comandos commit o push.
- 19 diagramas Mermaid renderizados correctamente con Mermaid CLI.
- Seis figuras PNG regenerables; todas menores de 150 KB. La mayor ocupa 64 416 bytes. Figura del proyecto inspeccionada visualmente.
- 23 URLs verificadas mediante herramienta web y respuesta HTTP 200.
- MS, ME y YE ejecutados en pandas 2.3.3; escritura/lectura NetCDF y conservación de metadatos comprobadas.

## Límites y revisión manual recomendada

- No se abrió Obsidian para comprobar el renderizado final.
- No se ejecutaron las seis sesiones dentro de Google Colab ni los comandos de instalación conda/VS Code; se contrastaron con sus documentos oficiales.
- La duración es una estimación editorial, pendiente de prueba con principiantes.
- La longitud informada cuenta el cuerpo sin bloques de código ni frontmatter YAML.
- La revisión pedagógica incluye comprobación manual; no hay un analizador que pruebe exhaustivamente la familiaridad previa con toda API.
- La eliminación del entorno y las cachés fue rechazada por la revisión automática con blocked by policy; siguen dentro del bloque. Las copias exitosas de notebooks con soluciones sí fueron descartadas por su contexto temporal.

Revisa a mano P.0 para adecuar calendarios al equipo; P4.2 para reglas de cobertura y base; P5.1 y P.Z para supuestos estadísticos; P5.2 y el mapa ampliado para coordenadas y áreas al cambiar de fuente. Antes de cualquier conclusión terrestre, reemplaza listas, CSV, mallas y tasas simuladas por productos NASA reales con versión, unidad, periodo, dominio y banderas de calidad. El mapa de solo dos años es una demostración de código.

## Versiones ejecutadas

| Componente | Versión |
|---|---|
| numpy | 2.5.3 |
| pandas | 2.3.3 |
| matplotlib | 3.11.2 |
| scipy | 1.18.1 |
| xarray | 2026.9.0 |
| netCDF4 | 1.7.4 |
| nbformat | 5.11.1 |
| nbclient | 0.11.0 |
| ipykernel | 7.4.0 |
| PyYAML | 6.0.3 |
| PyMuPDF | 1.28.2 |
| statsmodels | 0.15.0 |
| pymannkendall | 1.4.3 |
| pytest | 9.1.1 |
| python | 3.13.9 |

Las dependencias de authoría y comprobación están en requirements.txt, junto con las bibliotecas docentes. Las versiones mínimas de NumPy y SciPy utilizadas requieren Python 3.12 o superior; se verificó Python 3.13.9. La sintaxis enseñada es de Python 3.11 o superior.

## Resultado de referencia · datos simulados

| Región | Tasa OLS °C/década | p OLS sin corrección temporal | Años válidos |
|---|---|---|---|
| Sierra | 0.375554 | 2.17272e-11 | 21 |
| Costa | 0.172073 | 1.13007e-06 | 21 |
| Llanura | -0.125370 | 5.00283e-05 | 21 |

Los valores anteriores son salidas de la simulación; el pvalue no autoriza inferencias sobre la Tierra real ni corrige autocorrelación.
> [!success]- Conclusión ejecutada
> Pregunta: ¿qué región muestra mayor tasa de cambio?
> Datos: tres regiones simuladas, 2000–2023; 21 años completos por región.
> Método: base mensual 2000–2009, anomalías anuales y OLS sobre años reales.
> Resultado: Sierra encabeza las tasas con 0.376 °C/década.
> Límite: son datos simulados; p_ols no demuestra causa y exige revisar autocorrelación.

## Archivos y mantenimiento

Las fuentes editoriales comunes están en assets/contenido.py, ejercicios.py y proyecto.py; generar_bloque.py produce notas y notebooks y omite archivos existentes. generar_figuras.py regenera PNG. validar_bloque.py repite las comprobaciones. Los JSON conservan evidencias de versiones, fuentes, temas introducidos y resultados. Son recursos de mantenimiento, no contenido adicional de estudio.

## Árbol final

```text
P Python desde cero/
├── .trabajo-temporal/  [pruebas; limpieza bloqueada]
├── .venv-temporal/  [entorno; limpieza bloqueada]
├── assets/
│   ├── __pycache__/
│   │   ├── contenido.cpython-313.pyc
│   │   ├── ejercicios.cpython-313.pyc
│   │   ├── proyecto.cpython-313.pyc
│   │   └── validar_bloque.cpython-313.pyc
│   ├── contenido.py
│   ├── ejercicios.py
│   ├── fig_P3_3_mapa.png
│   ├── fig_P3_3_serie.png
│   ├── fig_P4_2_anomalias.png
│   ├── fig_P5_2_malla.png
│   ├── fig_PD_componentes.png
│   ├── fig_PZ_proyecto.png
│   ├── fuentes_verificadas.json
│   ├── generar_bloque.py
│   ├── generar_figuras.py
│   ├── INFORME_ENTREGA.md
│   ├── mapa_pedagogico.json
│   ├── proyecto.py
│   ├── validar_bloque.py
│   ├── verificacion.json
│   └── versiones.json
├── notebooks/
│   ├── P1_Fundamentos.ipynb
│   ├── P2_Estructuras_y_herramientas.ipynb
│   ├── P3_NumPy_y_visualizacion.ipynb
│   ├── P4_pandas_y_series_de_tiempo.ipynb
│   ├── P5_Python_cientifico.ipynb
│   └── PZ_Proyecto_integrador.ipynb
├── P1 Fundamentos del lenguaje/
│   ├── P1.0 Índice P1.md
│   ├── P1.1 Primeros pasos, variables y tipos.md
│   ├── P1.2 Decisiones y repeticiones.md
│   ├── P1.3 Funciones.md
│   └── P1.E Ejercicios P1.md
├── P2 Estructuras de datos y herramientas/
│   ├── P2.0 Índice P2.md
│   ├── P2.1 Listas, tuplas, diccionarios y conjuntos.md
│   ├── P2.2 Comprensiones, objetos y herramientas útiles.md
│   ├── P2.3 Archivos, errores y módulos.md
│   └── P2.E Ejercicios P2.md
├── P3 NumPy y visualización/
│   ├── P3.0 Índice P3.md
│   ├── P3.1 Arreglos NumPy.md
│   ├── P3.2 Vectorización, broadcasting y NaN.md
│   ├── P3.3 Gráficas con matplotlib.md
│   └── P3.E Ejercicios P3.md
├── P4 pandas y series de tiempo/
│   ├── P4.0 Índice P4.md
│   ├── P4.1 Series y DataFrames.md
│   ├── P4.2 Fechas, remuestreo y anomalías.md
│   ├── P4.3 Agrupar y resumir.md
│   └── P4.E Ejercicios P4.md
├── P5 Python científico y buenas prácticas/
│   ├── P5.0 Índice P5.md
│   ├── P5.1 SciPy, llamar y leer resultados.md
│   ├── P5.2 xarray y NetCDF.md
│   ├── P5.3 Depuración, Git y código reproducible.md
│   └── P5.E Ejercicios P5.md
├── P.0 Empezar aquí.md
├── P.B Bibliografía y plan de lectura.md
├── P.D Datos sintéticos de práctica.md
├── P.Z Proyecto integrador.md
└── requirements.txt
```
