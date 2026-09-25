En lugar de usar teoremas matemáticos abstractos para calcular la incertidumbre o los p-valores, usamos la fuerza bruta computacional sobre nuestros propios datos, mezclándolos de distintas formas para ver qué tan raros son nuestros resultados originales.

**Métodos principales**:

- **Bootstrap:** Sacas datos al azar de tu muestra _permitiendo que se repitan_ (con reemplazo) para armar miles de "muestras clon" del mismo tamaño. Le calculas la pendiente a cada clon para armar un **intervalo de confianza** empírico, sin suponer ninguna distribución normal. Para series con autocorrelación, se usa el **Bootstrap por bloques** (sacas fragmentos seguidos de datos en lugar de puntos sueltos).

- **Pruebas de permutación (Permutation tests):** Mezclas el orden temporal de tus datos sin repetirlos. Calculas la pendiente a cada desorden. Esto te ayuda a ver si la tendencia que observaste es rara (significativa) o si cualquier desorden aleatorio te daría una pendiente similar.

**Ejemplo numérico (Prueba de permutación)**
Tienes el tiempo $x = [1, 2, 3]$ y una variable observada $y = [2, 1, 3]$.
Tu pendiente original calculada es $b = 0.5$.
Para saber si es significativa, desordenamos $y$. Las permutaciones posibles (sin repetir) de 3 datos son $3! = 3 \times 2 \times 1 = 6$.
Esos 6 arreglos de $y$ generan estas pendientes:

1. `[1, 2, 3]` -> $b = 1.0$
    
2. `[1, 3, 2]` -> $b = 0.5$
    
3. `[2, 1, 3]` -> $b = 0.5$ (tu original)
    
4. `[2, 3, 1]` -> $b = -0.5$
    
5. `[3, 1, 2]` -> $b = -0.5$
    
6. `[3, 2, 1]` -> $b = -1.0$
    

De estas 6 opciones, **3** son iguales o mayores a tu pendiente original ($0.5$). Por lo tanto, tu "p-valor" empírico es $3/6 = 0.5$. Con un p-valor del 50%, concluyes que la tendencia original no es estadísticamente significativa; es muy probable que sea producto del azar.

**Tu turno (Ejercicio)**

Tienes un nuevo set de datos de 4 años, $x = [1, 2, 3, 4]$, y observaste un aumento perfecto en tu variable: $y = [10, 20, 30, 40]$.

1. ¿Cuántas permutaciones posibles en total puedes armar con esos 4 datos de $y$?
    
2. Si generas todas esas permutaciones, ¿cuál será el arreglo exacto de $y$ que te dé la pendiente más **negativa** posible?
    
3. Si tu tendencia original (`[10, 20, 30, 40]`) produce la pendiente más alta posible de todos los escenarios, ¿cuál sería el p-valor empírico de esa tendencia exacta? (Recuerda: casos iguales o más extremos / total de permutaciones).