# Resumen conceptual

|Concepto|Pregunta que responde|
|---|---|
|Espacio muestral|¿Qué resultados pueden ocurrir?|
|Evento|¿Qué resultados me interesan?|
|Probabilidad|¿Qué tan probable es que ocurra?|
|Probabilidad condicional|¿Qué tan probable es A sabiendo B?|
|Independencia|¿B cambia la probabilidad de A?|
|Variable aleatoria|¿Cómo convierto un resultado aleatorio en un número?|
|Esperanza|¿Cuál es el promedio esperado?|
|Varianza|¿Qué tanta dispersión existe?|
|Desviación estándar|¿Qué tan dispersos están los datos en sus unidades originales?|
|Covarianza|¿Dos variables tienden a moverse juntas?|
|Correlación|¿Qué tan fuerte es su relación lineal?|
# Una chuleta para memorizar B1

Puedes quedarte inicialmente con estas ideas:
$$\boxed{P(A)=\frac{\text{favorables}}{\text{posibles}}}$$

Probabilidad de un evento.

$$\boxed{ P(A|B)=\frac{P(A\cap B)}{P(B)} }$$

Probabilidad condicional.
$$\boxed{ P(A\cap B)=P(A)P(B) }$$

Si A y B son independientes.
$$\boxed{ E[X]=\sum xP(x) }$$
Esperanza.
$$\boxed{ Var(X)=E[(X-\mu)^2] }$$

Varianza.
$$\boxed{ \sigma=\sqrt{Var(X)} }$$

Desviación estándar.
$$\boxed{ Cov(X,Y)=E[(X-\mu_X)(Y-\mu_Y)] }$$

Covarianza.
$$\boxed{ \rho= \frac{Cov(X,Y)} {\sigma_X\sigma_Y} }$$

Correlación.

# Cómo se conecta todo

La secuencia mental que te recomiendo aprender es:

```
EXPERIMENTO
     ↓
ESPACIO MUESTRAL
     ↓
EVENTOS
     ↓
PROBABILIDADES
     ↓
VARIABLE ALEATORIA
     ↓
ESPERANZA → centro
     ↓
VARIANZA → dispersión
     ↓
DESVIACIÓN ESTÁNDAR → dispersión interpretable
     ↓
COVARIANZA → movimiento conjunto
     ↓
CORRELACIÓN → fuerza y dirección de relación lineal
```

Para tu preparación de **ciencia de datos**, especialmente pensando en analizar datos científicos, la parte que más conviene dominar es esta cadena:

**probabilidad → variables aleatorias → esperanza/varianza → covarianza → correlación.**

Y hay una idea que debes tener grabada:

> **Probabilidad habla de incertidumbre; esperanza habla del centro; varianza de dispersión; covarianza de movimiento conjunto; correlación de la fuerza y dirección de una relación lineal.**