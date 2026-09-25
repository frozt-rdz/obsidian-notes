La función lineal modela una relación constante de cambio entre una variable independiente ($x$, habitualmente el tiempo) y una variable dependiente ($y$, como temperatura o nivel del mar). Permite estimar la velocidad constante de cambio (pendiente $b$) y un valor de referencia (intercepto $a$). En análisis de datos climáticos de la NASA, la pendiente **siempre debe interpretarse junto con sus unidades físicas por unidad de tiempo** (por ejemplo, °C/década o mm/año).
$$y = a + b \cdot x$$
Donde:

- **Pendiente (**$b$**):** $b = \frac{\Delta y}{\Delta x} = \frac{y_2 - y_1}{x_2 - x_1}$
- **Intercepto (**$a$**):** $a = y - b \cdot x$
**Ejemplo numérico pequeño:**

Imagina que analizamos la temperatura media global en dos puntos temporales:

- En $x_1 = 2000$, $y_1 = 14.0\text{ °C}$
- En $x_2 = 2020$, $y_2 = 14.4\text{ °C}$

Calculamos la pendiente $b$: $$b = \frac{14.4 - 14.0}{2020 - 2000} = \frac{0.4}{20} = 0.02\text{ °C/año}$$

Si convertimos a escala decadal: $0.02 \times 10 = \mathbf{0.2\text{ °C/década}}$. Esto significa que la temperatura aumentó a razón de $0.2\text{ °C}$ por cada década transcurrida.

**Ejercicio para ti:**

Dada la siguiente serie simplificada de observaciones del nivel del mar ($y$, en mm) en tres años ($x$):

- Año 2010 ($x_1 = 2010$): $y_1 = 20\text{ mm}$
- Año 2015 ($x_2 = 2015$): $y_2 = 35\text{ mm}$
- Año 2020 ($x_3 = 2020$): $y_3 = 50\text{ mm}$
- **Calcula la pendiente** $b$ entre los años 2010 y 2020. Expresa el resultado con sus unidades físicas en **mm/año** y en **mm/década**.
$$b=\frac{50-20}{2020-2010}=\frac{30}{10}=3\text{ mm/año}=30 \text{ mm/década}$$
- **Obtén la ecuación lineal** $y = a + b \cdot x$, calculando el valor del intercepto $a$ considerando $x$ como el año.
$$a=20-3(2010)=-6010$$
$$y=-6010+3\cdot x$$


Resuelve ambos incisos y comparte tus respuestas para revisarlas paso a paso.