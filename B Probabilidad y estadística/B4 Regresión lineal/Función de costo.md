La pérdida permite medir la diferencia existente entre los datos reales (_y_) y los datos obtenidos tras realizar la Regresión Lineal (que en adelante llamaremos $\hat{y}$).
Existen diferentes formas de definir matemáticamente esta pérdida, pero la más usada es a través del error cuadrático medio (ECM), definido de la siguiente manera:
$$ECM = \displaystyle \frac{1}{N} \sum_{i=1}^{N}\left(y_i-\hat{y}_i\right)^2$$
![[ECM.png]]
Así, el ECM mide el error promedio existente entre los datos originales y los datos obtenidos a partir de la Regresión Lineal.
### Definición de la línea recta que mejor se ajusta a los datos

Teniendo en cuenta que la pérdida es una medida de la diferencia existente entre los datos originales y la predicción, podemos definir la recta que mejor se ajusta a los datos como aquella que **minimiza** el error cuadrático medio.

Teniendo en cuenta que cada punto de la regresión se calcula como:
$$\hat{y}_i = wx_i + b$$

y reemplazando en la ecuación anterior, tenemos que el error cuadrático medio es:
$$ECM = \displaystyle \frac{1}{N} \sum_{i=1}^{N}\left(y_i-wx_i-b\right)^2$$

Por tanto, la Regresión Lineal es simplemente un problema de optimización, consistente en **encontrar los valores  y  óptimos que minimizan la pérdida**.