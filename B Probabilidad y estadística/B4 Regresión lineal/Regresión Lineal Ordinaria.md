Es el método estadístico clásico para trazar una línea recta que represente la tendencia de un conjunto de puntos de datos. El objetivo principal al usarla es obtener la **pendiente** ($b$), la cual nos indica cuánto cambia una variable (como la temperatura) cuando otra variable cambia (como el tiempo).

La ecuación general correspondiente a un modelo de regresión lineal es:
$$Y = \beta_0 + \sum \ \beta_k X_k + \epsilon_i$$
donde  representa las estimaciones de parámetros lineales que se deben calcular y  representa los términos de error.
Para modelos que utilizan un único predictor. La ecuación general es:
$$Y = \beta_0 + \beta_1 X+ \epsilon$$
**La fórmula de la pendiente** 
Para calcular la pendiente $b$ a mano, la fórmula es:

$$b = \frac{\sum(x_i - \bar{x})(y_i - \bar{y})}{\sum(x_i - \bar{x})^2}$$

Desglosando sus partes:

- $x_i$ e $y_i$: Representan cada par de datos individuales (por ejemplo, el año y el valor de ese año).
- $\bar{x}$ e $\bar{y}$: Representan el promedio (o media) de todos los valores $x$ y de todos los valores $y$.
- $\sum$: Es la sumatoria, es decir, realizar la operación que le sigue para cada punto de datos y luego sumar todos los resultados.

**Los Supuestos del modelo** 
Para que confíes en los resultados de una regresión OLS, los datos deben cumplir con ciertas condiciones matemáticas conocidas como "supuestos":
- **Linealidad:** La relación entre la variable $x$ y la $y$ debe comportarse como una línea recta.
- **Independencia:** Los datos no deben depender unos de otros.
- **Varianza constante:** La dispersión de los puntos respecto a la línea debe mantenerse estable a lo largo de todo el gráfico (no abrirse como un embudo).
- **Normalidad de residuos:** Si graficas los errores de tu modelo, deberían formar una campana de Gauss (distribución normal).

Cuando ajustes una regresión en Python (usando `scipy.stats.linregress` o `statsmodels`), obtendrás varios valores importantes:

- **Residuos:** Es la diferencia o distancia vertical entre un dato real observado y el valor que predice la línea recta.
- **R²:** Indica qué porcentaje de la variación total de los datos logra explicar tu línea recta.
- **Error estándar de la pendiente e Intervalo de confianza:** Te muestran la incertidumbre y el rango donde se encuentra la verdadera pendiente de la población.

**¿Qué pasa cuando fallan los supuestos?** En ciencias de la Tierra, es muy común que estos supuestos fallen, y debes saber qué ocurre:

- **Autocorrelación:** Si los datos no son independientes, la prueba "cree" que tiene más información de la que realmente tiene, entregándote p-valores demasiado optimistas (diciéndote que hay una tendencia significativa cuando en realidad no la hay).
- **Valores atípicos:** Un dato extremo (un punto muy alto o bajo) jalará la recta hacia sí mismo, arruinando el valor real de la pendiente.

Imagina que tienes una miniserie temporal: $x = [1, 2, 3]$ y $y = [2, 4, 6]$.

1. Calculamos los promedios: $\bar{x} = 2$, $\bar{y} = 4$.
2. Resolvemos el numerador de la fórmula para cada punto y sumamos:
    - Punto 1: $(1 - 2)(2 - 4) = (-1)(-2) = 2$
    - Punto 2: $(2 - 2)(4 - 4) = (0)(0) = 0$
    - Punto 3: $(3 - 2)(6 - 4) = (1)(2) = 2$
    - Suma del numerador = $2 + 0 + 2 = 4$.
3. Resolvemos el denominador (las $x$) al cuadrado y sumamos:
    - $(-1)^2 + (0)^2 + (1)^2 = 1 + 0 + 1 = 2$.
4. Dividimos para obtener la pendiente: $b = \frac{4}{2} = 2$.

Calcula la pendiente a mano para estos datos:
- $x = [1, 2, 3, 4]$
- $y = [3, 5, 5, 7]$

Te sugiero empezar sacando el promedio de $x$ y el promedio de $y$. Escribe tu desarrollo paso a paso y te daré mis correcciones.

$$\bar{x}=\frac{5}{2}
$$$$\bar{y}=5$$
$$(1-\frac{5}{2})(3-5)=3$$
$$(2-\frac{5}{2})(5-5)=0$$
$$(3-\frac{5}{2})(5-5)=0$$
$$(4-\frac{5}{2})(7-5)=3$$
Suma: $6$
$$\frac{9}{4}+\frac{1}{4}+\frac{1}{4}+\frac{9}{4}=5$$
Entonces: $$b=\frac{6}{5}=1.2$$

Para cerrar este tema y dar por dominado el bloque B4, responde estas 3 preguntas de verificación basadas en los conceptos del temario:

1. ¿Qué nos indica el valor R² al aplicar una regresión lineal a una serie de datos de la NASA?
    
2. Si al graficar notas que la varianza de los residuos cambia a lo largo de tu serie de tiempo, ¿Qué supuesto esencial de la regresión OLS está fallando?
    
3. ¿Por qué el problema de la autocorrelación te arrojará p-valores demasiado optimistas al detectar tendencias?
