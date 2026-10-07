"""Etapas del proyecto y recetas de figuras originales y deterministas."""
from contenido import clean
PROJECT=[]
def stage(section,minutes,title,prompt,code,check,hint):
    PROJECT.append(dict(day="Z",id=f"PZ-{len(PROJECT)+1:02}",section=section,stars=3,minutes=minutes,kind="Reto Tierra",
        title=title,prompt=prompt,setup="",solution=clean(code),
        check=f'assert ({check}), "{title}: revisa la etapa y sus entradas"',
        hint=hint,why="Conserva datos, unidades y cobertura para que otra persona reproduzca el resultado."))

stage("Núcleo",15,"Generar, leer y limpiar",
"Genera las tres regiones de P.D con faltantes. Pasa por un CSV en memoria, convierte fechas, ordena y cuenta descartes. Comprueba unicidad fecha/región; duplicated marca filas repetidas según esas columnas. Conserva df y limpio.",
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress, theilslopes
from io import StringIO
df = pd.read_csv(StringIO(serie_mensual(faltantes=True).to_csv(index=False)))
df["fecha"] = pd.to_datetime(df["fecha"], errors="raise")
df = df.sort_values(["region", "fecha"])
assert not df.duplicated(["region", "fecha"]).any(), "Hay fechas duplicadas"
descartes = int(df["temp_C"].isna().sum())
limpio = df.dropna(subset=["temp_C"]).copy()
''', 'len(df)==864 and descartes==9 and len(limpio)==855',
"No rellenes ausencias; los conteos anuales detectarán meses excluidos.")
stage("Núcleo",20,"Climatología y cobertura anual",
"Por región calcula referencias mensuales exclusivamente en 2000–2009. Guarda series_anuales con anomalías anuales y cobertura con conteos de meses. Exige doce meses; usa índices de fechas reales.",
'''
series_anuales = {}
cobertura = {}
for region, grupo in limpio.groupby("region"):
    s = grupo.set_index("fecha")["temp_C"].sort_index()
    base = s.loc["2000":"2009"]
    clima = base.groupby(base.index.month).mean()
    assert len(clima)==12, "La base debe cubrir los doce meses"
    assert (base.groupby(base.index.month).count()==10).all(), "Base incompleta"
    anom = s - s.index.month.map(clima).to_numpy()
    n = anom.resample("YE").count()
    cobertura[region] = n
    series_anuales[region] = anom.resample("YE").mean().where(n==12)
''', 'len(series_anuales)==3 and all([s.notna().sum()==21 for s in series_anuales.values()])',
"Los años 2012, 2016 y 2021 están incompletos y deben quedar ausentes.")
stage("Núcleo",20,"Estimar y exportar tasas",
"Ajusta linregress por región con años reales, centrados en 2000. Guarda ajustes y tabla con tasa_decada,p_ols,n_anios. Incluye periodo,base,metodo,unidad,origen y exporta resultados_simulados.csv.",
'''
ajustes = {}
filas = []
for region, anual in series_anuales.items():
    s = anual.dropna()
    x = s.index.year.to_numpy() - 2000
    r = linregress(x, s.to_numpy())
    ajustes[region] = r
    filas.append({"region": region, "tasa_decada": 10*r.slope,
                  "p_ols": r.pvalue, "n_anios": len(s),
                  "periodo": "2000–2023", "base": "2000–2009",
                  "metodo": "OLS", "unidad": "°C/década", "origen": "simulado"})
tabla = pd.DataFrame(filas).sort_values("tasa_decada", ascending=False)
tabla.to_csv("resultados_simulados.csv", index=False)
''', 'tabla["region"].to_list()==["Sierra","Costa","Llanura"] and (tabla["n_anios"]==21).all() and np.allclose(tabla["tasa_decada"],[0.4,0.2,-0.1],atol=0.04)',
"No confundas las 21 observaciones válidas con 21 años consecutivos.")
stage("Núcleo",25,"Figura de evidencia",
"Dibuja series anuales con huecos visibles y sus rectas, más barras de tasas. Conserva fig,ejes. En el notebook basta ver la figura; el archivo incluido se regenera con assets/generar_figuras.py.",
'''
fig, ejes = plt.subplots(1, 2, figsize=(9, 3.5))
colores = ["#0072B2", "#D55E00", "#009E73"]
for (region, anual), color in zip(series_anuales.items(), colores):
    x = anual.index.year.to_numpy()
    r = ajustes[region]
    ejes[0].plot(x, anual, "o-", color=color, label=region, markersize=3)
    ejes[0].plot(x, r.intercept+r.slope*(x-2000), "--", color=color)
ejes[0].set(xlabel="Año", ylabel="Anomalía [°C]",
            title="Simulado · base 2000–2009")
ejes[0].legend(fontsize=8)
ejes[1].bar(tabla["region"], tabla["tasa_decada"], color="#0072B2")
ejes[1].axhline(0, color="black", linewidth=0.7)
ejes[1].set(ylabel="Tasa OLS [°C/década]", title="Simulado · 2000–2023")
fig.tight_layout()
''', 'len(ejes[0].lines)==6 and len(ejes[1].patches)==3',
"axhline traza una referencia horizontal y tight_layout ajusta márgenes. Se explican aquí antes de usarlos.")
stage("Núcleo",15,"Conclusión de cinco líneas",
"Escribe conclusion con cinco líneas: pregunta, datos, método, resultado y límite. Incluye la tasa estimada de Sierra, unidad, 21 años válidos y advertencia de datos simulados. splitlines separa un texto en líneas.",
'''
sierra = tabla.loc[tabla["region"]=="Sierra", "tasa_decada"].iloc[0]
conclusion = (
    "Pregunta: ¿qué región muestra mayor tasa de cambio?\n"
    "Datos: tres regiones simuladas, 2000–2023; 21 años completos por región.\n"
    "Método: base mensual 2000–2009, anomalías anuales y OLS sobre años reales.\n"
    f"Resultado: Sierra encabeza las tasas con {sierra:.3f} °C/década.\n"
    "Límite: son datos simulados; p_ols no demuestra causa y exige revisar autocorrelación."
)
print(conclusion)
''', 'len(conclusion.splitlines())==5 and "simulad" in conclusion and "°C/década" in conclusion',
"La tasa y la cobertura pertenecen al resultado; la validez estadística necesita los bloques B y C.")
stage("Ampliación",20,"Estimación robusta",
"Calcula theilslopes(y,x) para cada región con años reales. Guarda robustas con tasa_decada_theil, inferior y superior por década.",
'''
filas_robustas = []
for region, anual in series_anuales.items():
    s = anual.dropna()
    r = theilslopes(s.to_numpy(), s.index.year.to_numpy())
    filas_robustas.append({"region": region, "tasa_decada_theil": 10*r.slope,
                          "inferior": 10*r.low_slope, "superior": 10*r.high_slope})
robustas = pd.DataFrame(filas_robustas)
''', 'len(robustas)==3 and (robustas["inferior"]<=robustas["tasa_decada_theil"]).all() and (robustas["superior"]>=robustas["tasa_decada_theil"]).all()',
"Los límites son para la pendiente bajo los supuestos del estimador.")
stage("Ampliación",20,"Comparar métodos",
"Une tabla y robustas por región; calcula diferencia entre tasas. Identifica el mayor desacuerdo absoluto en max_diferencia.",
'''
comparacion = tabla.merge(robustas, on="region", validate="one_to_one")
comparacion["diferencia"] = comparacion["tasa_decada"]-comparacion["tasa_decada_theil"]
max_diferencia = float(comparacion["diferencia"].abs().max())
comparacion.to_csv("comparacion_simulada.csv", index=False)
''', 'len(comparacion)==3 and max_diferencia<0.05',
"one_to_one exige claves únicas en ambas tablas. Acuerdo entre métodos no prueba ausencia de sesgo.")
stage("Ampliación",20,"Tasa por celda",
"Genera la malla P.D. Reduce estacionalidad con promedios anuales antes de estimar pendiente por celda. Solo hay dos años: es una demostración de programación, sin prueba de significancia. Conserva tasa_mapa como DataArray.",
'''
import xarray as xr
ds = malla()
anual_malla = ds["temp"].resample(time="YE").mean()
tasas = np.zeros((ds.sizes["lat"], ds.sizes["lon"]))
x = anual_malla["time"].dt.year.to_numpy()
for i in range(ds.sizes["lat"]):
    for j in range(ds.sizes["lon"]):
        y = anual_malla.isel(lat=i, lon=j).to_numpy()
        tasas[i, j] = 10*linregress(x, y).slope
tasa_mapa = xr.DataArray(tasas, dims=("lat", "lon"),
                        coords={"lat": ds.lat, "lon": ds.lon},
                        attrs={"units": "degC/decade", "origen": "simulado"})
''', 'tasa_mapa.shape==(3,4) and bool((tasa_mapa.isel(lon=0)<0).all()) and bool((tasa_mapa.isel(lon=-1)>0).all())',
"Cada celda recibe los mismos años; no interpretes pvalue con esta cobertura mínima.")
stage("Ampliación",20,"Mapa y metadatos",
"Dibuja tasa_mapa con límites simétricos y guarda un Dataset NetCDF con el campo tasa. Conserva artista y archivo_mapa.",
'''
fig_mapa, ax_mapa = plt.subplots(figsize=(5, 3))
limite = float(np.abs(tasa_mapa).max())
artista = tasa_mapa.plot(ax=ax_mapa, cmap="RdBu_r", vmin=-limite, vmax=limite,
                        cbar_kwargs={"label": "Tasa simulada [°C/década]"})
ax_mapa.set(title="Simulado · dos años · demostración")
archivo_mapa = tasa_mapa.to_dataset(name="tasa")
archivo_mapa.attrs["limite"] = "Dos años; no inferencia estadística"
archivo_mapa.to_netcdf("tasa_mapa_simulada.nc", engine="netcdf4")
''', 'artista.get_clim()==(-limite,limite) and archivo_mapa["tasa"].attrs["origen"]=="simulado"',
"to_dataset asigna nombre a una variable para exportarla; cbar_kwargs configura la barra de color.")
stage("Ampliación",20,"README y repositorio local",
"Crea repo_simulado con README.md y .gitignore. Inicializa Git local con git init y consulta status mediante subprocess.run, que ejecuta una lista de argumentos externos; check=True detecta fallo. No ejecutes commit ni push. shutil.which detecta si Git está disponible; si falta, conserva los documentos.",
'''
from pathlib import Path
import subprocess
import shutil
repo = Path("repo_simulado")
repo.mkdir(exist_ok=True)
readme = (
    "# Detective simulado\n\n"
    "Datos simulados de P.D; periodo 2000–2023, base 2000–2009.\n"
    "Ejecutar las etapas PZ-01 a PZ-05 en orden en el notebook PZ.\n"
    "Dependencias: requirements.txt del bloque; semilla 2026.\n"
    "Regla: doce meses válidos por año; OLS usa años reales.\n"
    "Límites: simulación, autocorrelación, sin atribución causal.\n"
)
(repo/"README.md").write_text(readme, encoding="utf-8")
(repo/".gitignore").write_text(".venv/\n__pycache__/\n*.nc\n", encoding="utf-8")
git_disponible = shutil.which("git") is not None
if git_disponible:
    subprocess.run(["git", "init", "--quiet", str(repo)], check=True)
    estado_git = subprocess.run(["git", "-C", str(repo), "status", "--short"],
                                check=True, capture_output=True, text=True).stdout
''', '(repo/"README.md").exists() and (repo/".gitignore").exists() and (not git_disponible or (repo/".git").is_dir())',
"Este repositorio de práctica no contiene commits. Si falta Git, la rúbrica deja la inicialización pendiente.")
stage("Ampliación",20,"Entrega reproducible",
"Repite el generador con la misma semilla, verifica igualdad y agrega al README las versiones reales. importlib.metadata.version consulta la versión de una distribución instalada. Deja plan_git como texto con add y commit para lectura, sin ejecutarlo.",
'''
from importlib.metadata import version
replica = serie_mensual(faltantes=True)
original = serie_mensual(faltantes=True)
assert replica.equals(original), "Misma semilla y entorno deben reproducir datos"
versiones = {p: version(p) for p in ["numpy", "pandas", "scipy", "xarray"]}
with open(repo/"README.md", "a", encoding="utf-8") as f:
    f.write("\nVersiones verificadas: "+str(versiones)+"\n")
plan_git = "git add README.md .gitignore\n" + 'git commit -m "Documenta simulación"\n'
(repo/"plan_git_no_ejecutado.txt").write_text(plan_git, encoding="utf-8")
''', 'replica.equals(original) and "Versiones verificadas" in (repo/"README.md").read_text(encoding="utf-8")',
"El plan de comandos se guarda como texto; esta etapa no crea commits ni publica nada.")

FIGURES = [
dict(note="P3.3", name="fig_P3_3_serie.png", caption="Puntos azules: serie simulada; línea naranja: tasa impuesta, no estimada.", code=clean('''
import numpy as np
import matplotlib.pyplot as plt
rng = np.random.default_rng(2026)
t = np.arange(24)
y = 14 + 0.02*t + rng.normal(0, 0.05, 24)
fig, ax = plt.subplots(figsize=(6, 3))
ax.plot(2000+t, y, "o-", color="#0072B2", label="Serie simulada")
ax.plot(2000+t, 14+0.02*t, "--", color="#D55E00", label="Tasa impuesta")
ax.set(xlabel="Año", ylabel="Temperatura [°C]", title="Simulado · 2000–2023")
ax.legend()
fig.tight_layout()
''')),
dict(note="P3.3", name="fig_P3_3_mapa.png", caption="Ampliación: las celdas azules tienen tasa negativa, las rojas positiva, con escala simétrica.", code=clean('''
import numpy as np
import matplotlib.pyplot as plt
tasas = np.array([[-0.4, -0.2, 0.1, 0.3], [-0.3, -0.1, 0.2, 0.4]])
fig, ax = plt.subplots(figsize=(5, 3))
im = ax.imshow(tasas, origin="lower", cmap="RdBu_r", vmin=-0.4, vmax=0.4)
fig.colorbar(im, ax=ax, label="Tasa simulada [°C/década]")
ax.set(xlabel="Columna", ylabel="Fila", title="Malla simulada · tasas impuestas")
fig.tight_layout()
''')),
dict(note="P4.2", name="fig_P4_2_anomalias.png", caption="La estacionalidad domina la temperatura mensual; al restar la referencia mensual queda una anomalía con aumento impuesto.",code=clean('''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
rng = np.random.default_rng(2026)
t = np.arange(288)/12
fechas = pd.date_range("2000-01-01", periods=288, freq="MS")
s = pd.Series(14+0.02*t+2*np.sin(2*np.pi*t)+rng.normal(0,0.08,288), index=fechas)
base = s.loc["2000":"2009"]
clima = base.groupby(base.index.month).mean()
anom = s-s.index.month.map(clima).to_numpy()
anual = anom.resample("YE").mean()
fig, ejes = plt.subplots(2, 1, figsize=(6, 4), sharex=True)
ejes[0].plot(s.index, s, color="#0072B2")
ejes[0].set(ylabel="Temperatura [°C]", title="Simulado · referencia 2000–2009")
ejes[1].plot(anual.index, anual, "o-", color="#D55E00")
ejes[1].set(xlabel="Año", ylabel="Anomalía anual [°C]")
fig.tight_layout()
''')),
dict(note="P5.2", name="fig_P5_2_malla.png", caption="Promedio temporal de una malla simulada; los ejes son coordenadas. La figura muestra temperatura, no tendencia.",code=clean('''
import matplotlib.pyplot as plt
ds = malla()
fig, ax = plt.subplots(figsize=(5, 3))
ds["temp"].mean("time").plot(ax=ax, cmap="viridis", cbar_kwargs={"label": "Temperatura [°C]"})
ax.set(title="Promedio simulado · 2000–2001", xlabel="Longitud [°]", ylabel="Latitud [°]")
fig.tight_layout()
''')),
dict(note="P.D", name="fig_PD_componentes.png", caption="Componentes simulados: la temperatura combina nivel, tendencia, ciclo estacional, variabilidad lenta y ruido.",code=clean('''
import numpy as np
import matplotlib.pyplot as plt
rng = np.random.default_rng(2026)
t = np.arange(120)/12
tendencia = 0.02*t
estacion = 2*np.sin(2*np.pi*t)
variabilidad = 0.12*np.sin(2*np.pi*t/5)
ruido = rng.normal(0,0.08,120)
fig, ejes = plt.subplots(2, 1, figsize=(6, 4), sharex=True)
ejes[0].plot(t, 14+tendencia+estacion+variabilidad+ruido, color="#0072B2")
ejes[0].set(ylabel="Temperatura [°C]", title="Componentes de una serie simulada")
ejes[1].plot(t, tendencia, label="Tendencia", color="#D55E00")
ejes[1].plot(t, variabilidad, label="Variabilidad", color="#009E73")
ejes[1].plot(t, ruido, label="Ruido", color="#0072B2", alpha=0.5)
ejes[1].set(xlabel="Años desde 2000", ylabel="Contribución [°C]")
ejes[1].legend(fontsize=8)
fig.tight_layout()
''')),
dict(note="P.Z", name="fig_PZ_proyecto.png",caption="Las tres regiones simuladas muestran tasas diferentes; los huecos corresponden a años sin doce meses válidos.",code=PROJECT[3]["solution"])
]
