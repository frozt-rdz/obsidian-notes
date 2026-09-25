Se usa para minimizar el ECM, y será una función de dos variables:  $w$ y $b$. Por tanto, al hacer una gráfica de su comportamiento, encontraremos que para el caso de la Regresión Lineal ésta tiene forma de tazón, como se muestra en la figura de abajo. El mínimo que estamos buscando se encuentra al fondo de dicho tazón:
![[La pérdida (o función de costo) en la Regresión Lineal.png]]
Así, al usar el Gradiente Descendente para minimizar la pérdida, lo que haremos es de forma iterativa calcular los valores de _w_ y _b_ que hacen que el ECM sea cada vez más pequeño (que nos acerquemos progresivamente al fondo del tazón). Para ello usamos la ecuación general del gradiente descendente:
$$w \leftarrow w – \alpha dw$$
$$b \leftarrow b – \alpha db$$


donde $\alpha$ es la tasa de aprendizaje y  $dw$ y $db$ hacen referencia a la derivada (gradiente) de la pérdida con respecto a los parámetros $w$ y $b$:
$$dw = \displaystyle -\frac{2}{N} \sum_{i=1}^{N}x\left(y_i-wx_i-b\right)$$
$$db = \displaystyle -\frac{2}{N} \sum_{i=1}^{N}\left(y_i-wx_i-b\right)$$