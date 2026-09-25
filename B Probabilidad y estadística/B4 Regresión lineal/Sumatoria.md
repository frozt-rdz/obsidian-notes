La sumatoria es una notación compacta para expresar la adición de una secuencia de números. 
Es indispensable para construir promedios, ajustar regresiones y calcular los estadísticos de detección de tendencias en datos climáticos
$$\sum_{i=1}^{n} x_i = x_1 + x_2 + \dots + x_n$$
**Ejemplo numérico pequeño:**

Dada una serie de $n = 3$ mediciones $x = [3, ,5, 2]$ :$$\sum_{i=1}^{3} x_i = x_1 + x_2 + x_3 = 3 + 5 + 2 = 10$$

---

**Ejercicio para ti:**

Dada la siguiente serie de datos de anomalía de temperatura $x = [2, -1, 4, 0, 3]$ (donde $n = 5$):

1. Calcula a mano el valor de $\sum_{i=1}^{5} x_i$.
$$ = 2+(-1)+4+0+3=8$$
2. Calcula el valor de $\sum_{i=1}^{5} (x_i - 1)$.
$$=(2-1)+(-1-1)+(4-1)+(0-1)+(3-1)=1-2+3-1+2=3$$

Resuelve ambos incisos y comparte tus respuestas para revisarlas paso a paso

$$\sum_{i=1}^{n} c \cdot a_i = c \sum_{i=1}^{n} a_i
$$
$$\sum_{i=1}^{n} c = n \cdot c
$$
$$\sum_{i=1}^{n} (a_i + b_i) = \sum_{i=1}^{n} a_i + \sum_{i=1}^{n} b_i
$$
$$\sum_{i=1}^{n} a_i = \sum_{i=1}^{k} a_i + \sum_{i=k+1}^{n} a_i$$
**Preguntas de verificación (Tema 1: Notación de sumatoria)**1

Para cerrar este primer tema del **Bloque A1**2, responde estas 3 preguntas cortas:

1. **Propiedad de constante:** Si $k$ es un número constante, ¿a qué es igual $\sum_{i=1}^{n} k \cdot x_i$?
$$k\sum_{i=1}^n x_i$$
2. **Cálculo directo:** Si se sabe que $\sum_{i=1}^{10} x_i = 40$, ¿cuál es el valor de $\sum_{i=1}^{10} (x_i + 2)$?
$$60$$
3. **Aplicación climática:** ¿Cómo se escribe la fórmula de la media aritmética ($\bar{x}$) de una serie temporal de $n$ datos usando la notación $\Sigma$?
$$ \bar{x} = \frac{\sum_{i=1}^{n} x_i}{n}$$