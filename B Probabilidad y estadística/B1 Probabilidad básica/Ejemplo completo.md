
# Ejemplo completo en Python

Vamos a generar datos y calcular prácticamente todo.

```
import numpy as np

horas = np.array([1, 2, 3, 4, 5])
calificaciones = np.array([60, 65, 72, 80, 88])

# Media
media_horas = np.mean(horas)
media_calificaciones = np.mean(calificaciones)

# Varianza
var_horas = np.var(horas)
var_calificaciones = np.var(calificaciones)

# Desviación estándar
std_horas = np.std(horas)
std_calificaciones = np.std(calificaciones)

# Covarianza poblacional
covarianza = np.mean(
    (horas - media_horas) *
    (calificaciones - media_calificaciones)
)

# Correlación
correlacion = np.corrcoef(
    horas,
    calificaciones
)[0, 1]

print("Media horas:", media_horas)
print("Media calificaciones:", media_calificaciones)

print("Varianza horas:", var_horas)
print("Varianza calificaciones:", var_calificaciones)

print("STD horas:", std_horas)
print("STD calificaciones:", std_calificaciones)

print("Covarianza:", covarianza)
print("Correlación:", correlacion)
```
# Una forma de visualizar todo

Piensa en una variable XX.

### Esperanza

¿Dónde está el centro?

$$E[X]$$

### Varianza

¿Cuánto se dispersa?

$$Var(X)
$$
### Desviación estándar

¿Cuánto se aleja típicamente del centro?

$$\sigma$$

### Covarianza

¿X y Y se mueven juntas?

$$Cov(X,Y)$$

### Correlación

¿Qué tan fuerte es la relación lineal?

$$r$$