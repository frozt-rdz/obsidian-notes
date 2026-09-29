Este es uno de los conceptos **más importantes de toda la estadística**.

El Teorema del Límite Central, o **TLC**, dice de manera simplificada:

> Cuando tomamos muestras suficientemente grandes de una población, la distribución de la **media muestral** tiende a parecerse a una distribución normal, bajo condiciones apropiadas, aunque la población original no sea normal.

Esto es increíblemente útil.
# Imagina una población rara

Supongamos que tenemos una población donde los datos tienen una distribución muy extraña:

```
****
**
*
*
************
```

No parece normal.

Ahora hacemos esto:

1. Tomamos una muestra de 30 personas.
2. Calculamos la media.
3. Repetimos miles de veces.
4. Guardamos todas esas medias.

Obtendremos algo parecido a:

```
                *
             *******
           ***********
         ***************
       *******************
     ************************
```

Aunque la población original no era normal, **las medias muestrales tienden a formar una distribución aproximadamente normal**.

# ¿Por qué esto es tan útil?

Porque normalmente no conocemos toda la población.

Supongamos que quieres saber cuánto tarda un usuario en abrir una aplicación.

No puedes medir a todos los usuarios del mundo.

Pero puedes tomar muestras.

Si tomas muchas muestras y calculas sus medias, el TLC nos permite modelar el comportamiento de esas medias aproximadamente con una normal cuando el tamaño de muestra es suficientemente grande y se cumplen las condiciones pertinentes.