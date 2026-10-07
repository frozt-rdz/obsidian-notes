"""Fuente editorial única. Las notas y notebooks se generan desde estos registros."""
from textwrap import dedent

def clean(s):
    return dedent(s).strip()

FOLDERS = ["P1 Fundamentos del lenguaje", "P2 Estructuras de datos y herramientas", "P3 NumPy y visualización", "P4 pandas y series de tiempo", "P5 Python científico y buenas prácticas"]
TITLES = [
    ["Primeros pasos, variables y tipos", "Decisiones y repeticiones", "Funciones"],
    ["Listas, tuplas, diccionarios y conjuntos", "Comprensiones, objetos y herramientas útiles", "Archivos, errores y módulos"],
    ["Arreglos NumPy", "Vectorización, broadcasting y NaN", "Gráficas con matplotlib"],
    ["Series y DataFrames", "Fechas, remuestreo y anomalías", "Agrupar y resumir"],
    ["SciPy, llamar y leer resultados", "xarray y NetCDF", "Depuración, Git y código reproducible"],
]
NOTE_NAMES = [f"P{d}.{n} {t}" for d, titles in enumerate(TITLES, 1) for n, t in enumerate(titles, 1)]

ANUAL = clean('''
def serie_anual(n=24, tasa=0.02, nivel=14.0):
    """Serie simulada sin ruido; un valor por año desde 2000, en °C."""
    valores = []  # Lista vacía: iremos añadiendo valores.
    for i in range(n):
        valores.append(nivel + tasa * i)
    return valores
''')
MENSUAL = clean('''
def serie_mensual(semilla=2026, faltantes=False):
    """Tres regiones simuladas, mensuales, 2000–2023; jamás datos NASA."""
    import numpy as np
    import pandas as pd
    rng = np.random.default_rng(semilla)
    fechas = pd.date_range("2000-01-01", periods=288, freq="MS")
    t = np.arange(288) / 12  # Tiempo en años desde el inicio.
    tablas = []
    for region, tasa in zip(["Costa", "Sierra", "Llanura"], [0.02, 0.04, -0.01]):
        estacion = 2 * np.sin(2 * np.pi * t)
        variacion = 0.12 * np.sin(2 * np.pi * t / 5)
        ruido = rng.normal(0, 0.08, len(t))
        valor = 14 + tasa * t + estacion + variacion + ruido
        if faltantes:
            valor[150::53] = np.nan  # Base 2000–2009 completa.
        tablas.append(pd.DataFrame({"fecha": fechas, "region": region,
                                   "temp_C": valor}))
    return pd.concat(tablas, ignore_index=True)
''')
MALLA = clean('''
def malla(semilla=2026):
    """Dataset simulado mensual: time=24, lat=3, lon=4; temperatura en °C."""
    import numpy as np
    import pandas as pd
    import xarray as xr
    rng = np.random.default_rng(semilla)
    tiempo = pd.date_range("2000-01-01", periods=24, freq="MS")
    lat = np.array([-30.0, 0.0, 30.0])
    lon = np.array([-120.0, -90.0, -60.0, -30.0])
    t = np.arange(24).reshape(24, 1, 1) / 12
    tasas = np.array([[-0.03, -0.01, 0.01, 0.03]] * 3)
    valor = 14 + t * tasas + 0.3 * np.sin(2 * np.pi * t)
    valor = valor + rng.normal(0, 0.01, (24, 3, 4))
    ds = xr.Dataset({"temp": (("time", "lat", "lon"), valor)},
                    coords={"time": tiempo, "lat": lat, "lon": lon})
    ds.attrs["origen"] = "simulado"
    ds["temp"].attrs["units"] = "degC"
    ds["lat"].attrs["units"] = "degrees_north"
    ds["lon"].attrs["units"] = "degrees_east"
    return ds
''')
GENERATORS = [ANUAL, MENSUAL, MALLA]
CSV_SIMPLE = 'anio,temp_C\n2000,14.0\n2001,\n2002,14.4\n'

CONCEPTS = []
def concept(day, number, task, theory, code, trace, error, fix, micro, solution, app, cards, sources, introduced, extra=""):
    CONCEPTS.append(dict(day=day, number=number, task=task, theory=clean(theory), code=clean(code), trace=trace, error=error, fix=fix, micro=micro, solution=clean(solution), app=app, cards=cards, sources=sources, introduced=introduced, extra=clean(extra)))

concept(1, 1, "Convertir unidades antes de comparar tendencias",
'''Un programa es una secuencia de instrucciones. Ejecuta una celda con Shift+Enter; un archivo con `python archivo.py`. `#` inicia un comentario. `print(...)` muestra un resultado; los paréntesis contienen sus argumentos.
Una variable es una etiqueta: `t = 14.0` asocia `t` con un valor; `=` asigna y `==` compara. Una expresión produce un valor. Las líneas se ejecutan de arriba abajo.
`int` guarda enteros, `float` decimales, `str` texto entre comillas, `bool` es `True` o `False`, y `None` indica ausencia. `type(x)` consulta el tipo; `float("14.0")` convierte texto.
`+ - * /` calculan; `//` divide hacia abajo, `%` obtiene el resto y `**` eleva a una potencia. `> >= < <= != ==` comparan. `abs(x)` quita el signo. Los decimales pueden redondearse: compara con tolerancia.
Una f-string, `f"{t:.2f}"`, inserta el valor con dos decimales. La sangría agrupa instrucciones: usa cuatro espacios cuando P1.2 abra un bloque con `:`.
`assert condicion, "mensaje"` comprueba una condición: si falla, muestra `AssertionError`. En este bloque sirve para revisar ejercicios; no sustituye controles de calidad de datos.''',
'''# Temperatura y tasa simuladas; son magnitudes distintas.
t = float("14.0")
kelvin = t + 273.15
tasa = 0.02
por_decada = tasa * 10
print(f"{kelvin:.2f} K; {por_decada:.2f} °C/década")
assert abs(kelvin - 287.15) < 1e-10, "Revisa la conversión"
''',
[("1", "t = float(...)", "t → 14.0"), ("2", "kelvin = t + 273.15", "kelvin → 287.15"), ("3", "tasa * 10", "por_decada → 0.2")],
'"14.0" + 273.15', '❌ Se sumó texto y número. ✅ Convierte primero con `float`. `NameError` significa nombre no definido; `SyntaxError` indica sintaxis que Python no puede interpretar.',
["Predice `7 // 2` y `7 % 2`.", "Corrige `t = \"15\"; k = t + 273.15`.", "Completa la conversión de 0.03 °C/año a °C/década."],
'''assert 7 // 2 == 3 and 7 % 2 == 1, "Cociente y resto"
t = "15"
k = float(t) + 273.15
decada = 0.03 * 10
assert abs(k - 288.15) < 1e-10, "Kelvin"
assert abs(decada - 0.3) < 1e-10, "Tasa"
'''.replace('assert 7 // 2 == 3 and 7 % 2 == 1, "Cociente y resto"','assert 7 // 2 == 3, "Cociente"\nassert 7 % 2 == 1, "Resto"'),
"Una tasa simulada de 0.02 °C/año equivale a 0.20 °C/década. Sumar 273.15 cambia una temperatura absoluta; no cambia una diferencia ni una tasa.",
[("¿Asignar o comparar?", "= asigna; == compara"), ("¿Qué significa None?", "Ausencia explícita de valor"), ("¿Cómo paso de °C/año a °C/década?", "Multiplico por 10")],
"Delgado Quintero, 2022, cap. 3, §§3.1–3.2, pp. 46–72; Garcimartín, 2022, Python básico, §§1–2, pp. 2–3.",
"instrucción; comentario; variable; tipos; operadores; print; f-string; conversión; abs; assert; tolerancia")

concept(1, 2, "Contar años con anomalía positiva y evitar bucles infinitos",
'''`if condicion:` ejecuta un bloque cuando la condición es verdadera; `elif` prueba otra; `else` cubre lo restante. `and` exige ambas, `or` alguna y `not` niega. `in` pregunta pertenencia.
Para recorrer datos usamos aquí una lista mínima: `[a, b, c]` conserva valores en orden. `for valor in lista:` visita cada uno. Sus demás operaciones llegan en P2.1.
`range(inicio, fin, paso)` recorre enteros sin incluir `fin`; `range(3)` produce 0, 1, 2. Un acumulador guarda el progreso; `suma += valor` significa `suma = suma + valor`.
`while condicion:` repite mientras siga siendo verdadera. Debe cambiar algo que termine la repetición. Cuenta, suma y máximo se inicializan antes del bucle; para el máximo usa el primer dato o `None`.
➕ `break` termina el bucle; `continue` salta a la siguiente vuelta. No se necesitan en el núcleo.''',
'''# Anomalías simuladas en °C.
datos = [-0.2, 0.0, 0.3]
conteo = 0
suma = 0.0
mayor = None
for valor in datos:
    suma += valor
    if valor > 0:
        conteo += 1
    if mayor == None or valor > mayor:
        mayor = valor
i = 0
while i < 2:
    i += 1
if conteo == 0:
    etiqueta = "ninguno"
elif conteo == 1:
    etiqueta = "uno"
else:
    etiqueta = "varios"
print(conteo, etiqueta, i)
''',
[("1", "valor = -0.2", "conteo=0; suma=-0.2; mayor=-0.2"), ("2", "valor = 0.0", "conteo=0; suma=-0.2; mayor=0.0"), ("3", "valor = 0.3", "conteo=1; suma≈0.1; mayor=0.3")],
'if True:\nprint("simulado")', '❌ Falta sangría después de `:`. ✅ Indenta `print` cuatro espacios. Un bucle infinito puede no producir ningún error: detén la celda y revisa la condición.',
["Predice cuántas vueltas da `range(2, 5)`.", "Corrige un contador iniciado dentro del `for`.", "Completa un `while` que termine con `i == 3`."],
'''contador = 0
for i in range(2, 5):
    contador += 1
assert contador == 3, "El final no se incluye"
i = 0
while i < 3:
    i += 1
assert i == 3, "Actualiza i"
''', "El cero no cuenta como anomalía positiva. Para filtrar años válidos combina disponibilidad y condición antes de acumular.",
[("¿Incluye range su límite final?", "No"), ("¿Dónde inicializo un acumulador?", "Antes del bucle"), ("¿Qué evita un while infinito?", "Una actualización que haga falsa la condición")],
"Delgado Quintero, 2022, cap. 4, §§4.1–4.2, pp. 100–136; Garcimartín, 2022, Python básico, §§5–6, pp. 8–10.",
"if; elif; else; and; or; not; in; lista literal; for; range; while; acumuladores; +=; ampliación break continue")

concept(1, 3, "Reutilizar conversiones y cálculo de anomalías",
'''`def nombre(parametro):` define una función; llamarla ejecuta su cuerpo. `return` devuelve el resultado; `print` solo lo muestra. Sin `return`, una función devuelve `None`.
Los argumentos posicionales siguen el orden declarado; los nombrados usan `base=14`. Un valor por defecto se usa si omites ese argumento. La primera cadena del cuerpo es la docstring: explica contrato y unidades.
Un nombre creado dentro es local. Un nombre definido fuera es global: evita modificarlo desde la función. Pasa datos mediante parámetros.
Para construir la salida, `[]` crea una lista vacía y `.append(valor)` añade al final. Un método es una operación asociada a un objeto; P2 amplía esta idea.
`return a, b` devuelve una tupla, un grupo ordenado; `x, y = funcion()` desempaqueta sus dos valores. ➕ `lambda x: x * 10` expresa una función pequeña sin nombre.''',
'''def c_a_k(t):
    """Convierte temperatura absoluta de °C a K."""
    return t + 273.15

def anomalia(serie, base=14.0):
    """Resta una referencia fija a valores simulados en °C."""
    salida = []
    for valor in serie:
        salida.append(valor - base)
    return salida

def unidades(t):
    return t, c_a_k(t)

grados, kelvin = unidades(14.0)
print(anomalia([14.0, 14.5], base=14.0))
print(f"{grados:.1f} °C = {kelvin:.2f} K")
''',
[("1", "anomalia recibe serie y base", "serie=[14.0,14.5]; base=14.0"), ("2", "append(valor - base)", "salida=[0.0] y luego [0.0,0.5]"), ("3", "return salida", "la llamada produce una lista")],
'def convertir(t):\n    local = t + 273.15\nconvertir(14.0)\nprint(local)', '❌ `local` existe solo dentro de la función. ✅ Devuélvelo y asigna la llamada a otro nombre. No reemplaces `return` por `print`.',
["Predice el resultado de `anomalia([14.5])`.", "Corrige una función que imprime una conversión pero devuelve None.", "Completa una función `decada(tasa)` con `return`."],
'''def decada(tasa):
    """Tasa anual a tasa por década."""
    return tasa * 10
def convertir(t):
    return t + 273.15
assert anomalia([14.5]) == [0.5], "Referencia por defecto"
assert abs(convertir(0) - 273.15) < 1e-10, "Devuelve el valor"
assert decada(2) == 20, "Multiplica por diez"
''', "Una función permite aplicar la misma definición de anomalía a varias regiones simuladas. Registra siempre la referencia; aquí es fija, la mensual llegará en P4.",
[("¿print devuelve el dato mostrado?", "No; devuelve None"), ("¿Qué documenta una docstring?", "Entradas, salida y unidades"), ("¿Cómo saco un valor local?", "Con return y una asignación al llamar")],
"Delgado Quintero, 2022, cap. 6, §6.1, pp. 210–250; Garcimartín, 2022, Python básico, §9, pp. 12–13.",
"def; parámetro; argumento; valor por defecto; return; docstring; alcance; append; tupla; desempaquetado; ampliación lambda")

concept(2, 1, "Guardar pares año y valor, y series por región",
'''Una lista se puede modificar; una tupla conserva sus elementos. Los índices empiezan en 0; -1 es el último. `a[inicio:fin:paso]` selecciona sin incluir fin; `len(a)` cuenta elementos.
`b = a` crea otro nombre para la misma lista. `b = a.copy()` copia el primer nivel; las listas anidadas internas seguirían compartidas. `.append`, `.extend`, `.pop`, `.sort` modifican la lista; `sort()` devuelve `None`.
Un diccionario relaciona claves únicas con valores: `d["Costa"]`; `.get(clave, defecto)` permite una clave ausente. `.items()` recorre pares clave y valor.
Un conjunto `set` reúne valores únicos sin orden posicional; `.add`, `.remove`, `|` unión y `&` intersección. Los conjuntos sí son mutables.
En texto, `.strip()` quita espacios exteriores, `.split(",")` separa campos y `",".join(partes)` los reúne. `\n` dentro de una cadena representa un salto de línea.''',
'''# Series simuladas por región.
valores = [14.0, 14.2, 14.4]
copia = valores.copy()
copia[0] = 99.0
regiones = {"Costa": valores, "Sierra": [12.0, 12.3]}
anio, valor = (2000, valores[0])
campos = " Costa,14.0 ".strip().split(",")
unicos = {"Costa", "Costa", "Sierra"}
unicos.add("Llanura")
print(valores[-1], valores[:2], len(unicos))
print(",".join(campos))
''',
[("Lista", "Orden y cambios", "temperaturas"), ("Tupla", "Grupo fijo", "año y valor"), ("Diccionario", "Consultar por clave", "región → serie"), ("Conjunto", "Eliminar duplicados", "regiones únicas")],
'datos = [14.0]\nprint(datos[1])', '❌ El índice 1 pide un segundo elemento inexistente. ✅ Usa 0 o comprueba `len`. Garcimartín, p. 4, llama inmutable a `set`; se corrige conforme a Python.',
["Predice `[10, 20, 30][-1]`.", "Corrige el alias que cambia la serie original.", "Completa un diccionario con la clave Costa y dos valores."],
'''assert [10, 20, 30][-1] == 30, "Último elemento"
a = [1, 2]
b = a.copy()
b[0] = 8
assert a == [1, 2], "La copia protege el primer nivel"
d = {"Costa": [14.0, 14.2]}
assert len(d["Costa"]) == 2, "Dos años simulados"
''', "Los identificadores de región son claves. La posición de un valor en una lista no contiene por sí sola su año: guarda los años o define claramente el inicio.",
[("¿Qué devuelve sort?", "None; modifica la lista"), ("¿Qué significa -1?", "Última posición"), ("¿Un set es mutable?", "Sí; sus elementos deben poder usarse como claves")],
"Delgado Quintero, 2022, cap. 5, §§5.1–5.4, pp. 138–200; Garcimartín, 2022, Python básico, §§3–4 y 8, pp. 4–7 y 11–12.",
"índices; slicing; len; copy; alias; métodos de lista; diccionario; get; items; conjuntos; split; strip; join",
'''```text
posición:    0      1      2
valor:     14.0   14.2   14.4
negativo:   -3     -2     -1
```''')

concept(2, 2, "Transformar series y leer objetos de bibliotecas",
'''Una comprensión `[expresion for x in datos if condicion]` construye una lista; la condición es opcional. `{clave: valor for ...}` construye un diccionario. Primero entiende su bucle equivalente.
`zip(a, b)` empareja hasta la secuencia más corta; comprueba longitudes. `enumerate(a)` devuelve posición y valor. `sorted(a, key=funcion)` devuelve una lista ordenada sin modificar a; la función calcula el criterio.
`min`, `max`, `sum` resumen; `any` pregunta si alguna condición se cumple y `all` si todas. Evita aplicar min o max a una colección vacía.
Todo valor de Python es un objeto con tipo y operaciones. `objeto.atributo` consulta información; `objeto.metodo()` llama una operación. `dir(objeto)` lista nombres y `help(objeto.metodo)` describe su uso.
Leer `df.groupby(...).mean()` significa llamar groupby y luego mean sobre su resultado; todavía no lo ejecutamos. `resultado.slope` será un atributo numérico en P5.
➕ Una tupla con nombre permite posiciones y atributos; una `dataclass` agrupa campos con nombre. Aquí solo leerás `registro.region` y `registro.tasa` de objetos suministrados; no escribirás clases.''',
'''anios = [2000, 2001, 2002]
valores = [14.0, 14.5, 14.2]  # Simulados.
anomalias = [v - 14.0 for v in valores]
por_anio = {a: v for a, v in zip(anios, valores)}
def segundo(par):
    return par[1]
ordenados = sorted(por_anio.items(), key=segundo)
for i, valor in enumerate(anomalias):
    assert i < len(anomalias), "Posición válida"
print(anomalias)
print(ordenados[-1][0], any([v > 0 for v in anomalias]))
''',
[("1", "v - 14.0", "14.0 → 0.0; 14.5 → 0.5"), ("2", "zip(anios, valores)", "2000 ↔ 14.0"), ("3", "sorted(..., key=segundo)", "2001 queda último")],
'datos = [14.0]\nprint(datos.shape)', '❌ Una lista no tiene atributo shape. ✅ Usa `len(datos)`; shape se introduce para arreglos NumPy. Los paréntesis distinguen una llamada de la lectura de un atributo.',
["Predice `[v * 10 for v in [0.1, 0.2]]`.", "Corrige zip si faltó un año: comprueba ambas longitudes antes.", "Completa un diccionario año → anomalía con zip."],
'''r = [v * 10 for v in [0.1, 0.2]]
assert r == [1.0, 2.0], "Elemento a elemento"
anios = [2000, 2001]
valores = [0.1, 0.2]
assert len(anios) == len(valores), "No pierdas años con zip"
d = {a: v for a, v in zip(anios, valores)}
assert d[2001] == 0.2, "Conserva el par"
''', "Ordenar regiones por tasa necesita un criterio explícito. Las herramientas abreviadas conservan el significado de un bucle bien escrito.",
[("¿zip exige igual longitud?", "No; hay que comprobarla"), ("¿Atributo o método?", "El método se llama con paréntesis"), ("¿sorted modifica su entrada?", "No; crea una lista")],
"Delgado Quintero, 2022, cap. 5, §§5.1–5.3, pp. 138–191, y cap. 6, §6.2, p. 251; Garcimartín, 2022, Tópicos adicionales, §3, pp. 39–41.",
"comprensiones; zip; enumerate; sorted key; min max sum any all; objeto; atributo; método; dir help; ampliación lectura de namedtuple y dataclass")

concept(2, 3, "Leer un CSV simulado con faltantes y errores visibles",
'''Un módulo reúne herramientas; `import math` lo carga y `from pathlib import Path` trae un nombre. `as` crea un alias. `pip` instala paquetes desde la terminal: `python -m pip install -r requirements.txt` dentro del entorno.
`Path("datos.csv")` representa una ruta; `/` une partes de rutas. `.exists()` comprueba existencia. `with open(ruta, modo, encoding="utf-8") as f:` abre y cierra incluso si algo falla; `r` lee, `w` reemplaza y `x` crea sin sobrescribir. `.read()` lee; `.write(texto)` escribe.
`try` ejecuta algo que puede fallar; `except ValueError` trata una conversión inválida. `raise ValueError("mensaje")` detiene la función con una explicación. Atrapa errores concretos y cuenta los descartes.
`math` ofrece funciones matemáticas; `statistics.mean` promedia; `datetime.date` representa fechas. `random` existe para azar general, pero el bloque científico usará `np.random.default_rng(semilla)` desde P3.
CSV significa valores separados por comas. `split` basta para estos datos sencillos sin comas entrecomilladas; pandas leerá CSV generales en P4. ➕ Un módulo propio es un archivo `.py` cuyas funciones importas; evita llamarlo numpy.py.''',
'''from pathlib import Path
import statistics
# Archivo simulado en el directorio de práctica.
ruta = Path("temperatura_P2.csv")
texto = "anio,temp_C\\n2000,14.0\\n2001,\\n2002,14.4\\n"
with open(ruta, "w", encoding="utf-8") as f:
    f.write(texto)
with open(ruta, "r", encoding="utf-8") as f:
    lineas = f.read().split("\\n")
validos = []
faltantes = 0
for linea in lineas[1:]:
    if linea != "":
        anio, valor = linea.split(",")
        try:
            validos.append(float(valor))
        except ValueError:
            faltantes += 1
print(len(validos), faltantes, statistics.mean(validos))
''',
[("1", "float('14.0')", "validos=[14.0]"), ("2", "float('') → except", "faltantes=1"), ("3", "float('14.4')", "validos=[14.0,14.4]")],
'float("")', '❌ Un campo vacío no es un número. ✅ Regístralo como faltante; no lo reemplaces silenciosamente por cero. `FileNotFoundError` apunta a una ruta ausente.',
["Predice cuántos valores conserva el ejemplo.", "Corrige `except:` para capturar solo ValueError.", "Completa una función que rechace una serie vacía con raise."],
'''def media_segura(datos):
    if len(datos) == 0:
        raise ValueError("La serie está vacía")
    return sum(datos) / len(datos)
assert len(validos) == 2, "Se conservan dos valores"
try:
    float("")
except ValueError:
    estado = "faltante"
assert estado == "faltante", "Trata el error concreto"
assert media_segura([14, 16]) == 15, "Media válida"
''', "Conserva el número de filas excluidas y la razón. En el proyecto exportarás resultados junto a periodo, referencia y unidades.",
[("¿Qué hace with?", "Cierra el recurso al salir"), ("¿Qué modo evita sobrescribir?", "x"), ("¿Por qué except ValueError?", "No oculta errores ajenos a la conversión")],
"Delgado Quintero, 2022, cap. 5, §5.5, pp. 201–208, y cap. 6, §§6.3–6.4, pp. 280–294; Garcimartín, 2022, Python básico, §§7 y 11, pp. 10–11 y 16–19.",
"import; from; alias; pip; Path; with open; read write; CSV; try except; raise; math statistics datetime random; ampliación módulo propio")

concept(3, 1, "Representar años y seleccionar celdas de una malla",
'''`import numpy as np` abrevia el módulo. Un arreglo `np.array` guarda valores de un tipo común y permite cálculo por elemento; multiplicar una lista la repite.
`np.arange(inicio, fin, paso)` excluye el fin; `np.linspace(inicio, fin, n)` incluye ambos extremos por defecto. `np.zeros((filas, columnas))` inicia con ceros. `dtype=float` admite decimales y faltantes.
`shape` describe tamaños por eje; `ndim` cuenta ejes; `size` cuenta elementos. `reshape` cambia la forma conservando el número total de elementos.
`a[fila, columna]` selecciona una celda; `a[:, 1:]` toma todas las filas desde la columna 1. Una máscara como `a > 0` produce booleanos; `a[mascara]` selecciona verdaderos.
Una rebanada básica suele ser una vista que comparte memoria; `.copy()` la independiza. `np.array_equal(a,b)` compara arreglos exactamente; `np.allclose(a,b)` compara números con tolerancia.''',
'''import numpy as np
a = np.arange(6, dtype=float).reshape(2, 3)  # Malla simulada.
region = a[:, 1:].copy()
region[0, 0] = 99.0
lat = np.linspace(-30, 30, 2)
ceros = np.zeros((2, 3))
positivos = a[a > 0]
print(a.shape, a.ndim, a.size)
print(a[0, 1], positivos.size)
''',
[("1", "arange(6)", "shape=(6,)"), ("2", "reshape(2,3)", "shape=(2,3)"), ("3", "a[:,1:].copy()", "shape=(2,2); memoria separada")],
'import numpy as np\nnp.arange(5).reshape(2, 3)', '❌ Cinco valores no caben en seis celdas. ✅ El producto de shape debe ser size. En una matriz, el eje 0 recorre filas y el eje 1 columnas; no son coordenadas geográficas por sí mismos.',
["Predice shape de zeros((3,4)).", "Corrige reshape(2,3) si hay solo cinco valores.", "Completa una selección independiente de la primera fila."],
'''assert np.zeros((3, 4)).shape == (3, 4), "Tres por cuatro"
b = np.arange(6).reshape(2, 3)
fila = b[0, :].copy()
fila[0] = 99
assert b[0, 0] == 0, "Copia independiente"
''', "Una matriz simulada necesita vectores lat y lon para saber dónde están sus celdas. P5 pondrá nombres y coordenadas con xarray.",
[("¿Qué cuenta ndim?", "Ejes"), ("¿Qué conserva reshape?", "El número total de elementos"), ("¿Una rebanada siempre copia?", "No; usa copy si modificarás datos independientes")],
"Delgado Quintero, 2022, cap. 8, §8.2, pp. 326–368; Garcimartín, 2022, NumPy, §§1–2, pp. 22–24.",
"ndarray; array arange linspace zeros; dtype shape ndim size; reshape; índice 2D; máscara; vista; array_equal allclose",
'''```text
shape = (2, 3)       columnas: 0 1 2
fila 0                        0 1 2
fila 1                        3 4 5
```''')

concept(3, 2, "Restar referencias a muchas celdas y conservar faltantes",
'''Vectorizar es operar sobre un arreglo completo. `a - b` resta por elemento. Broadcasting alinea formas desde la derecha: cada tamaño debe coincidir o ser 1; las dimensiones ausentes se tratan como 1.
`axis` indica el eje que se reduce: en tiempo × región, `mean(axis=0)` elimina tiempo y conserva regiones. `axis=1` elimina regiones. `sum`, `min`, `max` siguen la misma regla.
`np.nan` marca un dato ausente en arreglos float. `np.isnan(a)` lo identifica; `nanmean`, `nanmin`, `nanmax` y `nansum` omiten faltantes. Una media sin valores válidos no es cero.
`np.where(condicion, si, no)` elige por elemento; `np.diff(a)` resta vecinos y reduce en uno el tamaño. `np.isfinite` descarta NaN e infinitos. `np.abs`, `np.sin`, `np.cos` trabajan por elemento; `np.deg2rad` convierte grados a radianes; `np.pi` es pi.
Adelanto: `np.average(valores, weights=np.cos(np.deg2rad(lat)))` pondera filas de una malla regular en latitud y longitud; su justificación y máscaras van en bloque D (nota pendiente).
`np.random.default_rng(semilla)` crea un generador repetible; `.normal(media, desviacion, size)` genera ruido simulado. ➕ `time.perf_counter()` da segundos de un reloj para medir duración; mide muchas repeticiones y comprueba primero igualdad.''',
'''import numpy as np
datos = np.array([[14.0, 12.0], [14.4, np.nan]])
base = np.array([14.0, 12.0])
anom = datos - base  # Simulado: tiempo × región menos región.
media = np.nanmean(anom, axis=0)
pasos = np.diff(datos[:, 0])
marcas = np.where(np.isnan(datos), -999.0, datos)
pesos = np.cos(np.deg2rad(np.array([-30.0, 30.0])))
regional = np.average(np.array([14.0, 16.0]), weights=pesos)
print(np.round(media, 2), np.round(pasos, 2), regional)
''',
[("1", "datos - base", "shape (2,2) - (2,) → (2,2)"), ("2", "nanmean(axis=0)", "media → [0.2,0.0]"), ("3", "diff", "[14.0,14.4] → [0.4]")],
'import numpy as np\nnp.zeros((2, 3)) - np.zeros(2)', '❌ Los tamaños finales 3 y 2 no coinciden. ✅ Si la referencia es por fila, conviértela a `(2,1)` con reshape. `np.round(x,2)` redondea solo para presentar.',
["Predice la forma al restar (4,3) y (3,).", "Corrige comparar `x == np.nan`.", "Completa la media por región de datos con NaN."],
'''assert (np.zeros((4, 3)) - np.zeros(3)).shape == (4, 3), "Alinea derecha"
x = np.array([1.0, np.nan])
assert np.isnan(x)[1], "NaN se detecta con isnan"
r = np.nanmean(datos, axis=0)
assert np.allclose(r, [14.2, 12.0]), "Elimina tiempo"
''', "Usa -999 solo como señal de exportación si el formato lo exige; no lo promedies. Registra cuántos valores válidos sostienen cada media simulada.",
[("¿Desde dónde alinea broadcasting?", "Desde la derecha"), ("¿NaN es igual a sí mismo?", "No; usa isnan"), ("¿axis=0 en tiempo × región?", "Reduce tiempo y conserva región")],
"Delgado Quintero, 2022, cap. 8, §8.2, pp. 326–368; Garcimartín, 2022, NumPy, §§3–4, pp. 24–25.",
"vectorización; broadcasting; axis; nan; nanmean; isnan isfinite; where diff; sin cos deg2rad pi average; default_rng normal; round; ampliación perf_counter",
'''```text
datos:       tiempo región   (24, 3)
referencia:         región       (3,)
resultado:   tiempo región   (24, 3)
```''')

concept(3, 3, "Mostrar una serie simulada con unidades y una tasa espacial",
'''`Figure` es el lienzo y `Axes` una zona de dibujo. `fig, ax = plt.subplots()` crea ambos. `ax.plot(x,y)` une puntos; `scatter` dibuja puntos; `bar` compara categorías; `hist(..., bins=...)` cuenta intervalos.
`ax.set(title=..., xlabel=..., ylabel=...)` rotula; `label` nombra una serie y `ax.legend()` muestra la leyenda. Usa azul `#0072B2` y naranja `#D55E00`, además de marcadores o guiones para distinguir.
Una paleta divergente `RdBu_r` representa signos opuestos. Fija `vmin=-limite, vmax=limite` para que cero quede en el centro; indica siempre unidad y periodo.
La recta aquí es la tendencia conocida del simulador, no una regresión calculada. P5 enseñará a estimarla.
➕ `imshow(matriz, origin="lower", extent=[oeste,este,sur,norte])` dibuja celdas; `pcolormesh(lon,lat,matriz,shading="auto")` acepta coordenadas. `fig.colorbar(im, ax=ax)` añade escala. `fig.savefig(ruta,dpi=100)` guarda; `plt.close(fig)` libera memoria.''',
'''import numpy as np
import matplotlib.pyplot as plt
rng = np.random.default_rng(2026)
t = np.arange(24)
y = 14 + 0.02 * t + rng.normal(0, 0.05, 24)  # Simulado.
fig, ax = plt.subplots(figsize=(6, 3))
ax.plot(2000 + t, y, "o-", color="#0072B2", label="Serie simulada")
ax.plot(2000 + t, 14 + 0.02 * t, "--", color="#D55E00", label="Tasa impuesta")
ax.set(xlabel="Año", ylabel="Temperatura [°C]", title="Simulado · 2000–2023")
ax.legend()
print(len(ax.lines))
''',
[("Línea", "Orden temporal", "plot"), ("Dispersión", "Relación de pares", "scatter"), ("Barras", "Regiones", "bar"), ("Histograma", "Distribución", "hist")],
'import matplotlib.pyplot as plt\nfig, ax = plt.subplots()\nax.plot([2000, 2001], [14.0])', '❌ Cada x necesita un y. ✅ Revisa las longitudes antes de dibujar. Una pendiente visual depende también de los límites de los ejes.',
["Predice cuántas líneas añade el ejemplo.", "Corrige una gráfica sin unidades en y.", "Completa la leyenda de una serie llamada Simulado."],
'''assert len(ax.lines) == 2, "Serie y tendencia impuesta"
ax.set_ylabel("Temperatura [°C]")
assert ax.get_ylabel() == "Temperatura [°C]", "Unidad visible"
ax.legend()
assert ax.get_legend() is not None, "Leyenda creada"
''', "La figura permite revisar si la señal simulada y las unidades son coherentes antes de interpretar resultados. Un mapa sin proyección ni costas es una vista de la malla, no cartografía completa.",
[("¿Figure o Axes?", "Lienzo o zona de dibujo"), ("¿Cómo centro la paleta en cero?", "Límites simétricos"), ("¿Qué debe aparecer en el título?", "Origen simulado y periodo; unidades en ejes")],
"Delgado Quintero, 2022, cap. 8, §8.4, pp. 433–474; Garcimartín, 2022, matplotlib, §§1–2, pp. 26–30.",
"Figure Axes; subplots; plot scatter bar hist; set; legend; colores; vmin vmax; ampliación imshow pcolormesh savefig close")

concept(4, 1, "Cargar y revisar una tabla mensual sin borrar información por accidente",
'''Una `Series` es una columna con etiquetas. Un `DataFrame` reúne columnas con un índice compartido. `pd.read_csv` interpreta un CSV; `StringIO` de `io` permite leer texto en memoria como archivo.
`head()` muestra primeras filas; `info()` imprime tipos y conteos; `describe()` resume columnas numéricas. `.columns`, `.index` y `.shape` describen la tabla; `.to_numpy()` extrae valores sin etiquetas.
`df["temp_C"]` es una Series; `df[["temp_C"]]` sigue siendo tabla. `loc[etiquetas, columnas]` usa etiquetas; `iloc[posiciones]` usa posiciones. Una máscara filtra filas.
`df["kelvin"] = df["temp_C"] + 273.15` crea una columna. Usa `df.loc[mascara, "columna"] = valor` para asignar; evita encadenar dos selecciones.
`isna()` detecta faltantes; `dropna(subset=[...])` elimina filas en columnas especificadas; `fillna(valor)` rellena con una decisión explícita. No asumas que cero representa una temperatura desconocida. `.copy()` conserva una tabla independiente.''',
'''import pandas as pd
from io import StringIO
texto = "fecha,temp_C\\n2000-01-01,14.0\\n2000-02-01,\\n2000-03-01,14.4\\n"
df = pd.read_csv(StringIO(texto))  # CSV simulado.
faltantes = df["temp_C"].isna().sum()
limpio = df.dropna(subset=["temp_C"]).copy()
limpio["kelvin"] = limpio["temp_C"] + 273.15
seleccion = limpio.loc[limpio["temp_C"] > 14.0, "temp_C"]
print(df.shape, faltantes, seleccion.iloc[0])
''',
[("1", "read_csv", "índice=0,1,2; columnas=fecha,temp_C"), ("2", "dropna", "índice=0,2; dos filas"), ("3", "iloc[0] en seleccion", "primera posición; etiqueta original 2")],
'import pandas as pd\ndf = pd.DataFrame({"temp_C": [14.0]})\ndf["temperatura"]', '❌ La clave solicitada no existe. ✅ Consulta `df.columns`. No confundas la etiqueta 2 con la segunda fila después de filtrar.',
["Predice cuántas filas conserva dropna en el ejemplo.", "Corrige `limpio.loc[1]` para pedir la segunda posición.", "Completa una columna de anomalías contra 14 °C."],
'''assert len(limpio) == 2, "Se excluye un faltante"
assert limpio.iloc[1]["temp_C"] == 14.4, "Segunda posición"
limpio["anom"] = limpio["temp_C"] - 14
assert abs(limpio.iloc[1]["anom"] - 0.4) < 1e-10, "Resta referencia"
''', "Cuenta filas antes y después de limpiar. La tabla conserva fechas como texto hasta P4.2; no supongas que el orden alfabético arregla cualquier fecha.",
[("¿Qué usa iloc?", "Posiciones"), ("¿Qué devuelve df con una columna por nombre?", "Una Series"), ("¿Por qué no rellenar siempre con cero?", "Puede inventar una señal física")],
"Delgado Quintero, 2022, cap. 8, §8.3, pp. 369–432; Garcimartín, 2022, Python básico, §11, pp. 16–19, como antecedente de archivos; no cubre pandas.",
"pandas; Series DataFrame; StringIO; read_csv; head info describe; loc iloc; columnas; isna dropna fillna")

concept(4, 2, "Pasar de meses a anomalías anuales con una referencia declarada",
'''`pd.to_datetime(..., errors="raise")` convierte texto; `.dt.month` extrae mes de una Series de fechas. `set_index("fecha")` crea un `DatetimeIndex`; `sort_index()` ordena; `s.loc["2000":"2009"]` recorta un periodo inclusivo.
`resample("YE").mean()` agrupa por fin de año; `ME` significa fin de mes y `MS` inicio de mes. En pandas 2.3 usamos ME/YE; los antiguos M/Y de algunos ejemplos están obsoletos.
`groupby(indice.month)` reúne en 12 grupos todos los eneros, febreros, etc. `.mean()` estima la climatología mensual: una referencia distinta por mes, usando solo el periodo base.
`s.index.month.map(clima)` busca la referencia de cada mes; restarla da anomalías. Revisa que los 12 meses existan en la base. `count()` cuenta valores válidos y `.where(condicion)` deja NaN donde no se cumple.
Para el núcleo, exige 12 meses válidos por año. Es una regla didáctica conservadora: evita promediar años con estaciones distintas. El bloque C (nota pendiente) tratará cobertura, días por mes y referencias.
➕ `rolling(3, min_periods=3).mean()` suaviza tres pasos; no añade observaciones independientes ni debe sustituir la serie al estimar una tendencia sin justificación.''',
'''import pandas as pd
import numpy as np
fechas = pd.date_range("2000-01-01", periods=36, freq="MS")
s = pd.Series(14 + 0.02 * np.arange(36) / 12, index=fechas)
base = s.loc["2000":"2001"]  # Simulado; base breve solo didáctica.
clima = base.groupby(base.index.month).mean()
referencia = s.index.month.map(clima).to_numpy()
anom = s - referencia
conteos = anom.resample("YE").count()
anual = anom.resample("YE").mean().where(conteos == 12)
print(anual.round(2).to_list())
''',
[("1", "groupby mes en base", "36 meses totales; base 24; referencia 12"), ("2", "restar referencia", "36 anomalías conservan su fecha"), ("3", "resample YE", "3 medias, cada una con 12 meses")],
'import pandas as pd\ns = pd.Series([14.0, 14.2])\ns.resample("YE").mean()', '❌ El índice es numérico, no temporal. ✅ Convierte fecha y úsala de índice. `to_list()` convierte Series a lista; `round(2)` redondea la presentación.',
["Predice cuántos valores tiene clima.", "Corrige un resample sin DatetimeIndex.", "Completa el filtro anual que exige doce meses válidos."],
'''assert len(clima) == 12, "Una referencia por mes"
fechas = pd.to_datetime(["2000-01-01", "2000-02-01"])
reparada = pd.Series([14.0, 14.2], index=fechas)
assert len(reparada.resample("ME").mean()) == 2, "Índice temporal"
valida = anom.resample("YE").mean().where(conteos == 12)
assert valida.notna().sum() == 3, "Tres años completos"
''', "En P.Z la base será 2000–2009, dentro de una serie simulada 2000–2023. Cambiar una referencia mensual fija cambia niveles; los patrones de faltantes pueden afectar también la pendiente estimada.",
[("¿Qué contiene una climatología mensual?", "Doce referencias calculadas en la base"), ("¿Qué hace YE?", "Agrupa con etiqueta al final del año"), ("¿Media de un año incompleto?", "Aplicar y documentar un umbral de cobertura")],
"Delgado Quintero, 2022, cap. 8, §8.3, pp. 369–432, para Series y agrupación; las APIs temporales se apoyan en pandas. Garcimartín no tiene capítulo de series pandas.",
"to_datetime; dt; date_range; DatetimeIndex; set_index sort_index; resample MS ME YE; groupby mean; map; count where; notna; to_list; ampliación rolling")

concept(4, 3, "Resumir regiones y exportar una tabla de tasas comparables",
'''Agrupar tiene tres pasos: separar filas por región, aplicar una operación y reunir resultados. `groupby("region").agg(media=("temp_C","mean"), n=("temp_C","count"))` nombra columnas de salida.
`pd.concat([a,b], ignore_index=True)` apila tablas; `merge` une por una clave. `validate="many_to_one"` exige una fila de metadatos por clave; revisa coincidencias para no perder o duplicar regiones.
`sort_values("tasa_decada", ascending=False)` ordena; `to_csv(ruta,index=False)` exporta sin la columna de índice. `reset_index()` convierte el índice en columna cuando hace falta.
Podemos recorrer `for region, grupo in df.groupby("region")`. Antes de P5 solo calcularemos la tasa entre extremos: cambio dividido por años, multiplicado por 10. No es una regresión ni una prueba de significancia.
➕ `pivot_table(index="anio", columns="region", values="temp_C", aggfunc="mean")` transforma filas en una tabla año × región; declarar mean evita ocultar cómo se resuelven duplicados.''',
'''import pandas as pd
df = pd.DataFrame({"region": ["Costa", "Costa", "Sierra", "Sierra"],
                   "anio": [2000, 2010, 2000, 2010],
                   "temp_C": [14.0, 14.2, 12.0, 12.4]})
resumen = df.groupby("region").agg(media=("temp_C", "mean"), n=("temp_C", "count"))
filas = []
for region, grupo in df.groupby("region"):
    g = grupo.sort_values("anio")
    tasa = (g["temp_C"].iloc[-1] - g["temp_C"].iloc[0])
    tasa = 10 * tasa / (g["anio"].iloc[-1] - g["anio"].iloc[0])
    filas.append({"region": region, "tasa_decada": tasa})
tasas = pd.DataFrame(filas).sort_values("tasa_decada", ascending=False)
meta = pd.DataFrame({"region": ["Costa", "Sierra"], "origen": ["simulado", "simulado"]})
tabla = tasas.merge(meta, on="region", how="left", validate="many_to_one")
tabla.to_csv("tasas_P4.csv", index=False)
print(tabla["region"].to_list())
''',
[("1", "separar", "Costa: 2 filas; Sierra: 2 filas"), ("2", "aplicar tasa entre extremos", "Costa≈0.2; Sierra≈0.4 °C/década"), ("3", "reunir y ordenar", "Sierra, Costa")],
'import pandas as pd\na = pd.DataFrame({"region": ["Costa"]})\nb = pd.DataFrame({"region": ["Costa", "Costa"]})\na.merge(b, on="region", validate="many_to_one")', '❌ Hay claves duplicadas en la tabla de metadatos. ✅ Resuelve la duplicación antes de unir; no retires validate para silenciar el problema.',
["Predice qué región queda primero.", "Corrige una exportación que añade un índice innecesario.", "Completa un resumen con media y conteo válido."],
'''assert tabla.iloc[0]["region"] == "Sierra", "Mayor tasa primero"
texto_csv = tabla.to_csv(index=False)
assert texto_csv.startswith("region,"), "Sin índice extra"
r = df.groupby("region").agg(media=("temp_C", "mean"), n=("temp_C", "count"))
assert r.loc["Costa", "n"] == 2, "Cuenta valores válidos"
''', "La tasa entre extremos sirve para practicar tablas con datos simulados. P5 reemplaza ese cálculo por linregress usando todos los años válidos.",
[("¿Qué hace concat?", "Apila tablas"), ("¿Qué hace merge?", "Une por claves"), ("¿Tasa entre extremos es OLS?", "No; solo usa dos puntos")],
"Delgado Quintero, 2022, cap. 8, §8.3, pp. 369–432; Garcimartín no cubre pandas; Python básico, §11, pp. 16–19, sirve de antecedente de exportación.",
"groupby agg; concat; merge validate; sort_values; reset_index; to_csv; tasa entre extremos; ampliación pivot_table")

concept(5, 1, "Llamar estimadores de tendencia y leer sus resultados con unidades",
'''`linregress(x,y)` ajusta una recta a pares válidos. Usa años reales, no posiciones si faltan años. `slope` es tasa por año; `intercept` nivel en x=0; `rvalue` correlación; `pvalue` prueba de pendiente cero; `stderr` error estándar de la pendiente.
`theilslopes(y,x)` devuelve pendiente robusta, intercepto y límites inferior/superior para la pendiente; observa que su orden y,x difiere de linregress. `kendalltau(x,y)` devuelve `statistic` y `pvalue`: asociación ordenada, no tasa en °C.
Una máscara `np.isfinite(x) & np.isfinite(y)` conserva pares. En arreglos usa `&`, `|`, `~` con paréntesis para combinar o negar máscaras. `and` no combina arreglos.
La teoría va en bloques B y C (nota pendiente). Un pvalue pequeño no mide importancia ni atribución causal; la autocorrelación temporal puede invalidar la lectura ingenua de estos resultados.
➕ `pymannkendall.original_test(y)` devuelve una tupla con nombres: trend, h, p, Tau, slope. Su slope usa pasos de observación: solo conviértela a °C/década si cada paso es un año regular.
➕ `statsmodels.api.OLS(y, sm.add_constant(x)).fit()` ajusta con intercepto; `.summary()` muestra coeficientes, errores y pruebas. OLS significa mínimos cuadrados ordinarios.''',
'''import numpy as np
from scipy.stats import linregress, theilslopes, kendalltau
x = np.arange(2000, 2010)
y = np.array([0.00, 0.03, 0.03, 0.07, 0.07, 0.11, 0.11, 0.15, 0.15, 0.19])
ok = np.isfinite(x) & np.isfinite(y)
r = linregress(x[ok] - 2000, y[ok])  # Simulado; origen en 2000.
robusto = theilslopes(y[ok], x[ok])
tau = kendalltau(x[ok], y[ok])
print(f"slope={r.slope:.4f}; intercept={r.intercept:.4f}")
print(f"r={r.rvalue:.4f}; p={r.pvalue:.3g}; stderr={r.stderr:.4f}")
print(f"Theil={robusto.slope:.4f}; tau={tau.statistic:.4f}")
''',
[("slope × 10", "Tasa", "°C/década"), ("intercept", "Nivel en el origen", "°C"), ("pvalue", "Probabilidad bajo hipótesis nula y supuestos", "sin unidad"), ("stderr", "Incertidumbre del estimador", "°C/año")],
'from scipy.stats import linregress\nlinregress([2000, 2001], [14.0, 14.2, 14.3])', '❌ Los años y valores tienen distinta longitud. ✅ Conserva pares válidos y años distintos. En SciPy 1.18.1, años constantes pueden devolver NaN con advertencias en vez de detenerse: valida antes.',
["Predice las unidades de 10 * r.slope.", "Corrige intercambiar x e y en theilslopes.", "Completa una máscara común para x e y."],
'''decada = 10 * r.slope
assert 0.15 < decada < 0.25, "Tasa simulada cercana a 0.2"
rob = theilslopes(y, x)
assert rob.low_slope <= rob.slope <= rob.high_slope, "Límites de pendiente"
ok = np.isfinite(x) & np.isfinite(y)
assert ok.sum() == 10, "Diez pares válidos"
''', "Reporta tasa, unidad, periodo, número de años y método. Una conclusión de significancia requiere revisar supuestos en los bloques posteriores; este ejemplo solo enseña a leer campos.",
[("¿Qué devuelve slope?", "Cambio de y por unidad de x"), ("¿Qué mide tau?", "Asociación por orden, no pendiente"), ("¿p pequeño demuestra causa?", "No")],
"Delgado Quintero, 2022, cap. 6, §§6.1–6.2, pp. 210–251, para funciones y objetos; Garcimartín, 2022, Python básico, §§7 y 9, pp. 10–13. Ninguno desarrolla estas APIs estadísticas.",
"SciPy; linregress atributos; theilslopes; kendalltau; máscaras & | ~; ampliación pymannkendall y statsmodels OLS")

concept(5, 2, "Seleccionar una región y guardar una malla con coordenadas",
'''Un `DataArray` es un arreglo con dimensiones, coordenadas y atributos. Un `Dataset` reúne variables que pueden compartir dimensiones. `attrs` guarda metadatos; no convierte unidades automáticamente.
`ds["temp"]` obtiene la variable. `sel(lat=..., method="nearest")` busca coordenadas; `isel(time=0)` usa posición. `sel(lat=slice(a,b))` recorta un intervalo; slice construye el rango etiquetado.
`mean(dim="time")` elimina tiempo y deja un mapa; `mean(dim=["lat","lon"])` deja una serie. `groupby("time.month").mean("time")` calcula doce referencias. `where(condicion)` enmascara.
`.plot()` dibuja según dimensiones; para un mapa primero reduce tiempo. `to_netcdf(ruta, engine="netcdf4")` escribe; `with xr.open_dataset(...) as ds:` lee y cierra. `.load()` trae los datos a memoria antes de cerrar.
NetCDF conserva dimensiones y coordenadas; comprueba units y origen después de leer. `.sizes` informa tamaños y `.dims` nombres. El generador malla de P.D usa estas operaciones ya explicadas.
➕ `resample(time="YE").mean()` promedia por año. `.weighted(pesos).mean(("lat","lon"))` pondera espacialmente; pesos sin NaN y alineados con lat; el área real se estudia en bloque D (nota pendiente).''',
'''import numpy as np
import pandas as pd
import xarray as xr
tiempo = pd.date_range("2000-01-01", periods=24, freq="MS")
v = 14 + np.arange(24).reshape(24, 1, 1) * 0.02 / 12 + np.zeros((24, 3, 4))
ds = xr.Dataset({"temp": (("time", "lat", "lon"), v)},
                coords={"time": tiempo, "lat": [-30, 0, 30], "lon": [-120, -90, -60, -30]})
ds.attrs["origen"] = "simulado"
ds["temp"].attrs["units"] = "degC"
region = ds["temp"].sel(lat=slice(-30, 0)).mean(dim=["lat", "lon"])
celda = ds["temp"].sel(lat=2, lon=-88, method="nearest")
clima = ds["temp"].groupby("time.month").mean("time")
mapa = ds["temp"].where(ds["temp"] > 0).mean(dim="time")
ds.to_netcdf("malla_P5.nc", engine="netcdf4")
with xr.open_dataset("malla_P5.nc", engine="netcdf4") as lectura:
    copia = lectura.load()
print(region.shape, mapa.shape, clima.sizes["month"])
''',
[("1", "Dataset", "temp: time=24, lat=3, lon=4"), ("2", "sel + mean espacio", "serie: time=24"), ("3", "mean tiempo", "mapa: lat=3, lon=4")],
'import xarray as xr\na = xr.DataArray([1, 2], dims="lat", coords={"lat": [0, 30]})\na.sel(lat=15)', '❌ No existe la coordenada exacta 15. ✅ Usa nearest si esa aproximación es adecuada y registra la coordenada elegida. Un recorte vacío puede deberse al orden descendente de latitud.',
["Predice la forma al promediar time.", "Corrige sel(lat=2) para elegir la celda más cercana.", "Completa una lectura que conserve datos tras cerrar NetCDF."],
'''assert mapa.shape == (3, 4), "Conserva espacio"
c = ds["temp"].sel(lat=2, method="nearest")
assert float(c["lat"]) == 0, "Coordenada elegida"
with xr.open_dataset("malla_P5.nc", engine="netcdf4") as archivo:
    memoria = archivo.load()
assert memoria.attrs["origen"] == "simulado", "Metadatos conservados"
''', "Las celdas y fechas del ejemplo son simuladas. Para datos NASA revisa calendario, unidades, latitudes, longitudes y máscara antes de reutilizar la selección.",
[("¿sel o isel?", "Coordenadas o posiciones"), ("¿attrs convierte °C a K?", "No; solo describe"), ("¿mean time produce qué?", "Un mapa si quedan lat y lon")],
"Delgado Quintero, 2022, cap. 8, §8.2, pp. 326–368; Garcimartín, 2022, NumPy, §§1–2, pp. 22–24, como antecedentes de arreglos. xarray y NetCDF se apoyan en documentación oficial.",
"xarray; DataArray Dataset; dims coords attrs sizes; sel isel nearest slice; mean dim; groupby time.month; where plot; NetCDF load; ampliación weighted resample")

concept(5, 3, "Localizar errores y entregar código reproducible al equipo",
'''Un traceback enumera llamadas y termina con tipo de error y mensaje. Lee esa última línea y busca la última línea de tu código. `print(tipo, forma)` ayuda a acotar; `assert` comprueba una expectativa concreta.
Prefiere funciones pequeñas con docstring y entradas explícitas. Fija semilla, periodo, referencia y versiones. Un `venv` aísla bibliotecas; `requirements.txt` declara dependencias; un README explica ejecución y límites.
Git registra versiones. El área de trabajo contiene cambios; `add` prepara una selección; `commit` crea una versión local. Una rama es una línea de trabajo. `.gitignore` evita incluir entornos, cachés y archivos grandes.
Los comandos de la tabla son material de estudio. En esta entrega no se ejecuta ningún commit ni push. Para el proyecto escribirás README y un plan de comandos que otra persona pueda revisar.
➕ pytest descubre funciones `test_...` en archivos `test_...py`; usa asserts como los del bloque. Ejecuta `python -m pytest archivo.py` en un entorno de práctica. `time.perf_counter` mide duración; compara respuestas antes de optimizar.''',
'''import numpy as np
def media_valida(valores):
    """Media en °C de una serie simulada finita, sin modificarla."""
    a = np.array(valores, dtype=float)
    assert a.size > 0, "Falta al menos un valor"
    assert np.isfinite(a).all(), "Hay valores no finitos"
    return float(a.mean())
rng = np.random.default_rng(2026)
datos = rng.normal(14, 0.1, 6)
resultado = media_valida(datos)
print(f"Media simulada: {resultado:.4f} °C")
''',
[("git init", "Inicia un repositorio de práctica", "No ejecutar en esta bóveda"), ("git status", "Muestra cambios", "Lectura"), ("git switch -c practica", "Crea una rama", "Plan didáctico"), ("git add README.md", "Prepara ese archivo", "Plan didáctico"), ('git commit -m "Documenta datos simulados"', "Guarda una versión local", "Solo explicado; no ejecutado")],
'def revisar(x):\n    assert x > 0, "Se necesitan datos"\nrevisar(0)', '❌ Falló una condición documentada. ✅ Revisa el dato de entrada; no borres el assert para ocultarlo. Los asserts pueden desactivarse con Python optimizado: para entrada externa usa raise.',
["Predice qué ocurre con media_valida([14,16]).", "Corrige una función que depende de una variable global.", "Completa un assert que verifique una media esperada."],
'''def media_explicita(datos):
    """Media con entrada explícita."""
    return sum(datos) / len(datos)
assert media_valida([14, 16]) == 15, "Media conocida"
assert media_explicita([2, 4]) == 3, "Sin globales"
''', "Compartir una conclusión exige poder reconstruirla. El proyecto deja código, metadatos, figuras y límites; publicar o versionar queda bajo control del equipo.",
[("¿Por dónde leo un traceback?", "Tipo y mensaje final, luego mi línea más cercana"), ("¿Qué fija una semilla?", "La secuencia pseudoaleatoria bajo el mismo entorno"), ("¿Git add crea una versión?", "No; prepara cambios para un commit posterior")],
"Delgado Quintero, 2022, cap. 6, §§6.3–6.4, pp. 280–294; Garcimartín, 2022, Python básico, §9, pp. 12–13, para funciones. Git y pytest: documentación oficial.",
"traceback; depuración; reproducibilidad; requirements; Git init status add commit ramas; gitignore README; ampliación pytest perf_counter")

# Aclaraciones breves antes de ejecutar los ejemplos o ejercicios relacionados.
CONCEPTS[3]["theory"] += "\nLa comparación x is None pregunta identidad con el objeto de ausencia; is not None la niega."
CONCEPTS[4]["theory"] += "\nlist(recorrido) recoge un recorrido en una lista; reverse=True invierte el orden en sorted."
CONCEPTS[7]["theory"] += "\nnp.round(x,2) redondea a dos decimales para presentar; no cambies datos analíticos solo para ocultar ruido."
CONCEPTS[9]["theory"] += "\nnotna() es la máscara de valores presentes; pd.isna(valor) comprueba ausencia en un valor aislado."
CONCEPTS[10]["theory"] += '\npd.date_range(inicio, periods=n, freq="MS") crea n fechas al inicio de cada mes. to_list() devuelve una lista y round(2) redondea la presentación.'
CONCEPTS[13]["theory"] += "\ncbar_kwargs configura la escala de color de plot; el campo label define su etiqueta."
CONCEPTS[0]["errors_extra"] = [
    ("temperatura =", "SyntaxError: falta la expresión a la derecha de la asignación; escribe temperatura = 14.0."),
    ("print(temperatura_no_definida)", "NameError: ese nombre no fue definido; asigna su valor antes de usarlo."),
]
