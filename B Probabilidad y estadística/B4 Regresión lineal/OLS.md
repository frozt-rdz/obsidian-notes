## 1. ¿Qué problema resuelve una regresión lineal?

Imagina que tienes datos de este tipo:

|Temperatura (°C)|Consumo eléctrico|
|---|---|
|20|2|
|22|3|
|24|5|
|26|4|
|28|6|

Queremos saber:

> ¿El consumo eléctrico tiende a aumentar cuando aumenta la temperatura?

Podríamos dibujar los puntos:

```
Y
6 |                 ●
5 |          ●
4 |             ●
3 |     ●
2 | ●
  +---------------------- X
    20  22  24  26  28
```

La **regresión lineal** busca encontrar una recta que represente lo mejor posible esa relación:

$$\hat y = a + bx$$

donde:

- $x$ = variable que usamos para explicar/predicir
- $y$= variable que queremos estudiar
- $a$ = intercepto
- $b$= pendiente
- $\hat y$ = valor que predice el modelo

---

# 2. ¿Qué significa la pendiente?

La pendiente bb es probablemente **la parte más importante que debes entender**.

$$b= \frac{\sum (x_i-\bar{x})(y_i-\bar{y})} {\sum (x_i-\bar{x})^2}$$

No te preocupes todavía por memorizarla. Primero entiende su significado.

Si:

$b=0.9$

significa aproximadamente:

> **Por cada aumento de 1 unidad en X, Y aumenta 0.9 unidades en promedio.**

Si:

$b=5$

entonces:

> Cuando X aumenta 1 unidad, Y aumenta aproximadamente 5 unidades.

Si:

$b=-2$

entonces:

> Cuando X aumenta 1 unidad, Y disminuye aproximadamente 2 unidades.

### Interpretación rápida

| Pendiente   | Interpretación                        |
| ----------- | ------------------------------------- |
| $b>0$       | X y Y aumentan juntas                 |
| $b<0$       | Cuando X aumenta, Y disminuye         |
| $b\approx0$ | No hay una relación lineal apreciable |

**Importante:** una pendiente distinta de cero muestra una asociación lineal estimada; por sí sola **no demuestra causalidad**.

---

# 3. ¿Por qué aparecen $\bar{x}$ y $\bar{y}$?

La barra significa **promedio**.

Por ejemplo, si:

x=[1,2,3,4,5]

entonces:

$$\bar{x}=\frac{1+2+3+4+5}{5}=3$$


Y si:

y=[2,3,5,4,6]

entonces:

$\bar{y}=\frac{2+3+5+4+6}{5}=4$

La fórmula de la pendiente básicamente está preguntando:

> "Cuando X se aleja de su promedio, ¿Y tiende también a alejarse de su promedio?"

---

# 4. Hagamos una regresión completa a mano

Utilizaremos:

x=[1,2,3,4,5] y=[2,3,5,4,6]

Primero:

$\bar{x}=3$ 
$\bar{y}=4$

Construimos una tabla:

| $x_i$ | $y_i$ | $x_i-\bar{x}$ | $y_i-\bar y$ | producto | cuadrado |
| ----- | ----- | ------------- | ------------ | -------- | -------- |
| 1     | 2     | -2            | -2           | 4        | 4        |
| 2     | 3     | -1            | -1           | 1        | 1        |
| 3     | 5     | 0             | 1            | 0        | 0        |
| 4     | 4     | 1             | 0            | 0        | 1        |
| 5     | 6     | 2             | 2            | 4        | 4        |
|       |       |               |              | **9**    | **10**   |

Por tanto:

$b=\frac{9}{10}=0.9$

Nuestra pendiente es:

$\boxed{b=0.9}$

---

# 5. ¿Y el intercepto?

La ecuación es:

$\hat y=a+bx$

Podemos obtener $a$ con:

$a=\bar y-b\bar x$

Entonces:

$$a=4-(0.9)(3)$$

$$a=1.3$$

Así que nuestra recta es:

$$\boxed{\hat{y}=1.3+0.9x}$$

Esta es nuestra regresión lineal ajustada.

## 6. ¿Qué significa la recta?

Nuestra ecuación:

$$\hat{y}=1.3+0.9x$$

significa:

El modelo estima que $Y$ aumenta $0.9$ unidades por cada unidad que aumenta $X$.

Por ejemplo, si:

$x=10$

el modelo predice:

$$\hat{y}=1.3+0.9(10)=10.3$$

## 7. Los residuos

Aquí aparece uno de los conceptos fundamentales.

El modelo produce:

$\hat{y}$

pero tenemos un valor real:

$y$

La diferencia es el residuo:

$$e_i=y_i-\hat{y}_i$$

Es decir:

$$\boxed{\text{Residuo}=\text{valor observado}-\text{valor predicho}}$$

Para nuestros datos:

|**X**|**Y real**|**Y predicho**|**Residuo**|
|---|---|---|---|
|1|2|2.2|-0.2|
|2|3|3.1|-0.1|
|3|5|4.0|1.0|
|4|4|4.9|-0.9|
|5|6|5.8|0.2|

Por ejemplo, para $x=3$:

$$\hat{y}=1.3+0.9(3)=4$$

pero el valor real fue:

$y=5$

entonces:

$$e=5-4=1$$

El modelo se quedó $1$ unidad por debajo.

## 8. Visualiza el residuo

Imagina:

Plaintext

```
Y
6 |                 ● real
5 |          ●
4 |        -----------●--------  recta
3 |     ●
2 | ●
  +-------------------------
```

La distancia vertical entre cada punto y la recta representa el residuo.

Una buena regresión intenta que esas distancias sean, en general, pequeñas.

## 9. ¿Qué significa OLS?

OLS significa:

- Ordinary Least Squares
    
- Mínimos Cuadrados Ordinarios
    

¿Por qué "mínimos cuadrados"?

Porque OLS busca los coeficientes que minimizan:

$$\sum e_i^2$$

es decir:

$$\boxed{SSE=\sum(y_i-\hat{y}_i)^2}$$

¿Por qué elevamos al cuadrado?

Porque:

- evita que positivos y negativos se cancelen;
    
- hace que errores grandes pesen más.
    

En nuestro ejemplo:

$$SSE=1.9$$

## 10. ¿Qué es $R^2$?

Este es otro concepto que debes dominar.

$R^2$ indica qué proporción de la variabilidad observada en $Y$ queda explicada por el modelo lineal con $X$.

Su fórmula:

$$R^2=1-\frac{SSE}{SST}$$

donde:

$$SSE=\sum(y_i-\hat{y}_i)^2$$

y

$$SST=\sum(y_i-\bar{y})^2$$

En nuestro ejemplo, $SSE=1.9$ y $SST=10$, por lo tanto:

$$R^2=1-\frac{1.9}{10}$$

$$R^2=0.81$$

o:

$$\boxed{R^2=81\%}$$

**¿Cómo interpretarlo?**

Podemos decir:

> En esta muestra, el modelo lineal con $X$ explica aproximadamente el 81% de la variabilidad observada de $Y$.

No significa:

"El modelo tiene 81% de probabilidad de ser correcto."

Tampoco significa:

"$X$ causa el 81% de $Y$."

Eso sería una interpretación incorrecta.

## 11. Los cuatro supuestos principales

Aquí empieza la parte que puede parecer más complicada, pero realmente son cuatro preguntas muy sencillas. Cuando hacemos una regresión lineal, asumimos ciertas propiedades sobre la relación y los errores.

### Supuesto 1: Linealidad

La relación entre $X$ e $Y$ debe poder representarse razonablemente con una recta.

Por ejemplo, esto puede funcionar:

Plaintext

```
      ●
    ●
  ●
●
```

Pero si tenemos:

Plaintext

```
●             ●
  ●         ●
    ●     ●
      ●
```

hay una relación curva. Una recta no representa bien ese comportamiento.

**¿Cómo detectarla?**

Mira un gráfico de **residuos vs $X$**.

Idealmente queremos algo parecido a:

Plaintext

```
residuo
  |
  |   •    •
0 | •   •     •
  |    •   •
  +---------------- X
```

No debería aparecer una estructura clara.

Si observas esto, podría existir curvatura:

Plaintext

```
residuo
  |
  | •       •
0 |   •   •
  |     •
  +---------------- X
```

### 12. Supuesto 2: Independencia

Los errores de una observación no deberían depender de los errores de otra. Esto es especialmente importante cuando los datos tienen un orden temporal.

Por ejemplo:

- Temperatura enero
    
- Temperatura febrero
    
- ...
    
    Los datos de hoy pueden estar relacionados con los de ayer. Eso puede producir autocorrelación.
    

### 13. ¿Qué es autocorrelación?

Imagina estos residuos:

`+ + + + + - - - - -`

No parecen aleatorios. Hay grupos. Podría significar que un residuo positivo tiende a ser seguido por otro residuo positivo. Eso viola la independencia.

**¿Por qué importa?**

Porque puedes creer que tienes mucha evidencia estadística cuando en realidad estás contando información repetida o dependiente. En datos temporales esto es muy común.

**Ejemplo NASA**

Supón que tenemos:

|**Día**|**Radiación solar**|
|---|---|
|1|102|
|2|113|
|3|124|
|4|125|
|5|130|

No necesariamente son cinco observaciones independientes en el sentido estadístico. El valor de hoy puede estar relacionado con el de ayer.

### 14. Supuesto 3: Varianza constante

También se llama **homocedasticidad**.

Significa que el tamaño de los errores debería mantenerse aproximadamente constante a lo largo del rango de $X$.

Un patrón saludable:

Plaintext

```
residuos
  |
 + •    • •
0   • •    •
 - •   • •
  +---------------- X
```

Un problema típico (parece un abanico):

Plaintext

```
residuos
  |
  |       •
  |     • • •
0 |   • •   • •
  | • •
  +---------------- X
```

Los errores son pequeños para $X$ pequeñas y grandes para $X$ grandes. Eso se llama **heterocedasticidad**.

### 15. ¿Qué pasa si falla la varianza constante?

La línea de regresión puede seguir estimando razonablemente la relación media, pero las estimaciones de incertidumbre habituales (errores estándar, pruebas e intervalos de confianza) pueden quedar mal calibradas.

Una violación de un supuesto no significa automáticamente que "la regresión no sirve". Significa que debemos entender qué parte del análisis queda afectada.

### 16. Supuesto 4: Normalidad de los residuos

Aquí suele haber mucha confusión. No estamos diciendo necesariamente "X debe ser normal" ni "Y debe ser normal".

La condición que normalmente nos interesa para la inferencia clásica es que los errores/residuos tengan una distribución aproximadamente normal (forma de campana), especialmente importante con muestras pequeñas.

Plaintext

```
              ##
            ######
          ##########
        ##############
      ##################
------------------------------
```

**¿Para qué importa?**

Principalmente para justificar la distribución exacta de ciertas cantidades utilizadas para construir: pruebas t, intervalos de confianza y p-valores.

## 17. Resumen de los cuatro supuestos

|**Supuesto**|**Pregunta**|
|---|---|
|**Linealidad**|¿La relación puede aproximarse con una recta?|
|**Independencia**|¿Los errores son independientes entre sí?|
|**Varianza constante**|¿El tamaño del error es similar en todo $X$?|
|**Normalidad**|¿Los residuos son aproximadamente normales?|

Una forma fácil de recordarlo: **Recta – Independientes – Mismo ruido – Campana**

## 18. ¿Qué pasa con los valores atípicos?

Un valor atípico es una observación que está muy alejada de las demás.

Ejemplo:

Plaintext

```
Y
|                  ●
|        ● ●
|     ●
|   ●
| ●
+--------------------- X
```

Ese punto lejano puede influir muchísimo en la recta.

## 19. No confundas valor atípico con punto influyente

Son conceptos relacionados, pero distintos.

Un punto puede ser raro en $Y$. Pero un punto con un $X$ extremo puede tener mucha capacidad de cambiar la pendiente.

Ejemplo:

Plaintext

```
●  ●
  ● ●
    ●
                         ●
```

Ese último punto está muy lejos en $X$ y puede ejercer una influencia grande sobre la recta. Por eso, en análisis de datos conviene revisar observaciones potencialmente influyentes, no simplemente eliminarlas porque "molestan".

## 20. ¿Por qué los valores atípicos son peligrosos?

Supongamos que tienes una pendiente que parece claramente positiva:

Plaintext

```
●
  ●
   ●
    ●
     ●
```

Pero agregamos un punto lejano:

Plaintext

```
●
  ●
   ●
    ●
     ●                         ●
```

La recta puede cambiar considerablemente. Por eso nunca conviene decir: _"Voy a borrar este dato porque se ve raro"_.

Primero hay que preguntarse: ¿Es un error de medición, una observación válida pero extrema, o un caso diferente? En un reto científico como NASA Space Apps, esa distinción puede ser importante.

## 21. Error estándar de la pendiente

Ahora pasamos a una parte más estadística. Ya sabemos que:

$$b=0.9$$

Pero, ¿qué tan precisa es esa estimación? Para eso usamos el error estándar de la pendiente.

Primero calculamos la desviación residual:

$$s=\sqrt{\frac{SSE}{n-2}}$$

En nuestro ejemplo:

$$s=\sqrt{\frac{1.9}{5-2}}$$

$$s\approx0.796$$

Después:

$$SE(b)=\frac{s}{\sqrt{\sum(x_i-\bar{x})^2}}$$

Como $\sum(x_i-\bar{x})^2=10$, tenemos:

$$SE(b)=\frac{0.796}{\sqrt{10}}$$

$$\boxed{SE(b)\approx0.252}$$

## 22. ¿Qué significa ese 0.252?

Tenemos:

$$b=0.9$$

y:

$$SE(b)=0.252$$

El mensaje intuitivo es:

Nuestra estimación de la pendiente tiene una incertidumbre asociada de aproximadamente $0.252$ bajo el modelo estadístico asumido.

No significa que $b=0.9\pm0.252$ sea automáticamente un intervalo de confianza. Eso es otra cosa.

## 23. Intervalo de confianza de la pendiente

Queremos construir un rango plausible para la verdadera pendiente poblacional.

Un intervalo de confianza del 95% tiene la forma:

$$b\pm t_{0.975,n-2}SE(b)$$

Como tenemos $n=5$, los grados de libertad son:

$$df=n-2=3$$

Para 95%:

$$t_{0.975,3}\approx3.182$$

Entonces:

$$0.9\pm(3.182)(0.252)$$

aproximadamente:

$$0.9\pm0.801$$

por lo que:

$$\boxed{IC_{95\%}\approx[0.099, 1.701]}$$

**Interpretación**

Una manera apropiada de expresarlo es:

> El intervalo de confianza del 95% para la pendiente es aproximadamente de 0.099 a 1.701. Como el intervalo no incluye 0, esto proporciona evidencia contra una pendiente poblacional igual a cero bajo las condiciones y supuestos del modelo.

## 24. Algo importantísimo sobre los intervalos de confianza

No interpretes un intervalo de confianza del 95% como: _"Hay un 95% de probabilidad de que la verdadera pendiente esté dentro de este intervalo."_

La interpretación frecuentista estricta es diferente. Para tu nivel actual, piensa:

> El procedimiento utilizado para construir estos intervalos tiene una cobertura del 95% a largo plazo bajo los supuestos correspondientes.

## 25. Nuestra regresión completa

Para nuestros datos:

$$\boxed{\hat{y}=1.3+0.9x}$$

Tenemos esta tabla de resultados básica:

|**Estadístico**|**Símbolo**|**Resultado**|
|---|---|---|
|Intercepto|$a$|1.30|
|Pendiente|$b$|0.90|
|Error estándar de pendiente|$SE(b)$|0.252|
|Suma de cuadrados del error|$SSE$|1.90|
|Coeficiente de determinación|$R^2$|0.81|
|Error residual|$s$|0.796|
|Intervalo de Confianza (95%)|$IC$ de $b$|[0.099, 1.701]|

## 26. ¿Cómo se vería una tabla típica de software?

Programas como R, Python/statsmodels, SPSS, Excel, etc., suelen dar algo parecido a:

|**Variable**|**Coeficiente**|**Error estándar**|**t**|**p-valor**|
|---|---|---|---|---|
|Intercepto|1.300|0.835|1.558|—|
|X|0.900|0.252|3.576|—|

Además:

|**Medida**|**Valor**|
|---|---|
|$R^2$|0.810|
|Observaciones|5|
|Error residual|0.796|

No necesitas memorizar todavía cómo calcula cada software el p-valor. Lo importante es entender qué representa cada columna.

## 27. ¿Qué es el estadístico $t$?

Para la pendiente:

$$t=\frac{b-0}{SE(b)}$$

Entonces:

$$t=\frac{0.9}{0.252}$$

$$\boxed{t\approx3.576}$$

¿Por qué usamos 0?

Porque normalmente queremos probar:

$$H_0: b=0$$

contra algo como:

$$H_1: b\neq0$$

En palabras: _"¿La pendiente podría ser simplemente cero?"_

## 28. La tabla que realmente deberías aprender a leer

Cuando te den algo como:

| Coeficiente | Estimate | Std. Error |  t value | p-value |
| ----------- | -------: | ---------: | -------: | ------: |
| Intercepto  |     1.30 |      0.835 |     1.56 |     ... |
| X           | **0.90** |  **0.252** | **3.58** |     ... |

debes poder decir:

- **Estimate ($0.90$):** Es la pendiente estimada. Por cada unidad adicional de $X$, $Y$ cambia aproximadamente $0.90$ unidades, en promedio.
    
- **Std. Error ($0.252$):** Es la incertidumbre estimada de ese coeficiente.
    
- **t value ($3.58$):** Indica cuántos errores estándar se encuentra la estimación respecto al valor 0 bajo la prueba correspondiente.
    
- **p-value:** Nos ayuda a evaluar la evidencia contra $H_0: b=0$. No debes interpretarlo como "probabilidad de que la hipótesis nula sea verdadera".
    

## 29. La diferencia entre pendiente y $R^2$

Es fundamental no confundirlos.

- **Pendiente ($b$):** Responde: ¿Cuánto cambia $Y$ cuando $X$ aumenta una unidad?
    
- **$R^2$:** Responde: ¿Qué proporción de la variabilidad de $Y$ queda explicada por este modelo lineal?
    

Por ejemplo, $b=2.5$ y $R^2=0.30$ podría ocurrir perfectamente. Significaría: El efecto lineal estimado por unidad de $X$ es 2.5, pero el modelo solo explica alrededor del 30% de la variabilidad de $Y$.

## 30. Un detalle importante: $R^2$ alto no significa modelo perfecto

Podrías tener $R^2=0.95$ y aun así tener problemas de: autocorrelación, valores atípicos, heterocedasticidad, relación no lineal, variables omitidas o errores de medición. Por eso: nunca mires únicamente el $R^2$.

## 31. ¿Cómo comprobar los supuestos?

Para una regresión sencilla, piensa en gráficos de diagnóstico.

**A. Residuos vs valores ajustados**

Sirve especialmente para detectar no linealidad y heterocedasticidad. Queremos algo aproximadamente aleatorio:

Plaintext

```
  •    •      •
     •   •
•       •    •
-------------------
```

No queremos un patrón estructurado o un abanico.

**B. Histograma de residuos**

Nos ayuda a evaluar la forma de la distribución.

**C. Q-Q plot**

Ayuda a evaluar si los residuos son aproximadamente normales. Idealmente los puntos siguen aproximadamente una línea.

**D. Residuos vs tiempo**

Especialmente importante si los datos están ordenados temporalmente.

Podrías encontrar algo como `+ + + + - - - - + + +`, lo cual sugiere dependencia/autocorrelación.

## 32. Ejemplo aplicado a un problema "tipo NASA"

Supón que tienes datos de observaciones científicas:

|**Hora**|**Radiación solar**|**Temperatura**|
|---|---|---|
|1|100|20|
|2|120|21|
|3|150|24|
|4|180|26|
|5|200|28|

Podrías plantear:

$$X = \text{Radiación solar}$$

$$Y = \text{Temperatura}$$

y ajustar:

$$\hat{T}=a+bR$$

Ahora puedes investigar: ¿Existe una asociación lineal entre radiación y temperatura? Y reportar:

- pendiente
    
- error estándar
    
- IC 95%
    
- $R^2$
    
- residuos
    
- posibles valores atípicos
    
- posibles problemas de dependencia temporal
    

Esto es mucho más cercano al tipo de razonamiento que deberás aplicar en un reto de datos que simplemente "saber la fórmula".