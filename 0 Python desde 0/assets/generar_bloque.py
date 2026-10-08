"""Generación desde una fuente común, sin sobrescribir archivos existentes."""
import contextlib, io, json, os, platform, re, subprocess, sys, tempfile
from datetime import date
from importlib.metadata import version
from pathlib import Path
import nbformat as nbf
import yaml
from contenido import *
from ejercicios import EXERCISES
from proyecto import PROJECT, FIGURES
ROOT=Path(__file__).resolve().parents[1]
WORK=ROOT/".trabajo-temporal"
WORK.mkdir(exist_ok=True)
os.environ["MPLBACKEND"]="Agg"
os.environ["MPLCONFIGDIR"]=str(WORK/"mpl")
import matplotlib.pyplot as plt
TODAY=date.today().isoformat()
VERSIONS={p:version(p) for p in ["numpy","pandas","matplotlib","scipy","xarray","netCDF4","nbformat","nbclient","ipykernel","PyYAML","PyMuPDF","statsmodels","pymannkendall","pytest"]}
VERSIONS["python"]=platform.python_version()
NB_NAMES=["P1_Fundamentos","P2_Estructuras_y_herramientas","P3_NumPy_y_visualizacion","P4_pandas_y_series_de_tiempo","P5_Python_cientifico","PZ_Proyecto_integrador"]
CREATED=[]; SKIPPED=[]
def normalize(text):
    text=text.replace("◊",chr(96))
    text="\n".join(line.rstrip() for line in text.replace("\r\n","\n").splitlines())
    return re.sub(r"\n{3,}","\n\n",text).strip()+"\n"
def write(rel,text):
    p=ROOT/rel
    if p.exists():
        SKIPPED.append(str(rel)); return
    p.parent.mkdir(parents=True,exist_ok=True)
    with p.open("x",encoding="utf-8",newline="\n") as f: f.write(normalize(text))
    CREATED.append(str(rel))
def link(name,alias=None):
    return f"[[{name}|{alias or name.split(' ',1)[-1]}]]"
class QD(yaml.SafeDumper): pass
def qstr(d,v):
    return d.represent_scalar("tag:yaml.org,2002:str",v,style='"' if "[[" in v else None)
QD.add_representer(str,qstr)
def front(title,kind="python",day=0,order=0,level="básico",library="python",minutes="25 min",prereq=None,extra=None):
    data=dict(tipo=kind,estado="borrador",dificultad={"básico":1,"intermedio":2,"avanzado":3}[level],fecha=TODAY,
        libreria=library,version=VERSIONS.get(library,VERSIONS["python"]),prerequisitos=[link(n) for n in prereq or []],
        reto="Earth System Trend Detective",fuentes=["P.B Bibliografía y plan de lectura"],tags=["space-apps","bloque-p","python","flashcards"],
        bloque="P",subtema=f"P{day}" if day else "P",dia=day,orden=order,prioridad="E",nivel=level,tiempo_estimado=minutes,aliases=[title])
    data.update(extra or {})
    return "---\n"+yaml.dump(data,Dumper=QD,allow_unicode=True,sort_keys=False)+"---\n\n"
def fence(code,lang="python"):
    f=chr(96)*3
    return f"\n{f}{lang}\n{code.strip()}\n{f}\n"
def quote(s,n=1):
    return "\n".join("> "*n+line for line in s.strip().splitlines())+"\n"
def table(headers,rows):
    return "\n| "+" | ".join(headers)+" |\n|"+"|".join(["---"]*len(headers))+"|\n"+"".join("| "+" | ".join(map(str,r))+" |\n" for r in rows)
def diagram(labels):
    lines=["flowchart LR"]
    for i,label in enumerate(labels):
        lines.append(f'    N{i}["{label}"]')
        if i: lines.append(f"    N{i-1} --> N{i}")
    lines+=["    classDef core fill:#1f6feb,stroke:#0b3d91,color:#ffffff",f"    class N{len(labels)//2} core"]
    return fence("\n".join(lines),"mermaid")
def concept_diagram(day,number,labels):
    if (day,number)==(1,2):
        code='''flowchart TD
    I["Iniciar conteo en cero"] --> C{"¿Quedan valores?"}
    C -- "sí" --> V["Leer siguiente valor"]
    V --> P{"¿Es positivo?"}
    P -- "sí" --> S["Sumar uno al conteo"]
    P -- "no" --> C
    S --> C
    C -- "no" --> O["Mostrar conteo"]
    classDef core fill:#1f6feb,stroke:#0b3d91,color:#ffffff
    class C,P core'''
    elif (day,number)==(2,3):
        code='''flowchart TD
    I["Texto del campo"] --> T["try convertir a float"]
    T --> C{"¿Conversión válida?"}
    C -- "sí" --> V["Guardar valor y año"]
    C -- "ValueError" --> E["except registrar faltante"]
    V --> F["Continuar lectura"]
    E --> F
    classDef core fill:#1f6feb,stroke:#0b3d91,color:#ffffff
    class T,E core'''
    else:return diagram(labels)
    return fence(code,"mermaid")
def execute(code,ns):
    out=io.StringIO()
    with contextlib.redirect_stdout(out): exec(compile(code,"<ejemplo>","exec"),ns)
    return out.getvalue().strip()
def traceback_real(code):
    with tempfile.TemporaryDirectory(dir=WORK,prefix="error-") as td:
        p=Path(td)/"error_intencional.py";p.write_text(code+"\n",encoding="utf-8")
        r=subprocess.run([sys.executable,"error_intencional.py"],cwd=td,text=True,encoding="utf-8",capture_output=True,env={**os.environ,"PYTHONIOENCODING":"utf-8","PYTHON_COLORS":"0"})
        assert r.returncode!=0,"Error intencional no falló"
        return r.stderr.strip().replace(str(p),"error_intencional.py")
SOURCES=[
("Python","https://docs.python.org/3/tutorial/","Sintaxis, colecciones y módulos"),
("venv 3.13","https://docs.python.org/3.13/tutorial/venv.html","Entornos y pip"),
("NumPy","https://numpy.org/doc/stable/user/","Arreglos y broadcasting"),
("pandas","https://pandas.pydata.org/docs/user_guide/","Tablas y faltantes"),
("pandas 2.3 temporal","https://pandas.pydata.org/pandas-docs/version/2.3/user_guide/timeseries.html","MS, ME, YE"),
("Matplotlib","https://matplotlib.org/stable/","Figure y Axes"),
("SciPy","https://docs.scipy.org/doc/scipy/","Contratos científicos"),
("linregress","https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html","Campos de regresión"),
("theilslopes","https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.theilslopes.html","Pendiente robusta"),
("kendalltau","https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.kendalltau.html","Asociación por rangos"),
("xarray","https://docs.xarray.dev/","Arreglos etiquetados y NetCDF"),
("Project Pythia","https://foundations.projectpythia.org/","Geociencias"),
("Python Data Science Handbook","https://jakevdp.github.io/PythonDataScienceHandbook/","Refuerzo científico"),
("Colab FAQ","https://research.google.com/colaboratory/faq.html","Notebook alojado"),
("Abrir Colab","https://colab.research.google.com/notebooks/intro.ipynb","Puede solicitar sesión"),
("VS Code","https://code.visualstudio.com/docs/python/environments","Seleccionar intérprete"),
("Jupyter","https://jupyter.org/install","Instalar notebook"),
("conda","https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html","Crear entornos"),
("statsmodels","https://www.statsmodels.org/stable/regression.html","OLS"),
("pyMannKendall","https://github.com/mmhs013/pyMannKendall","original_test"),
("Git","https://git-scm.com/docs/gittutorial","Versiones locales"),
("pytest","https://docs.pytest.org/en/stable/getting-started.html","Prueba básica")]
READINGS=[
("Garcimartín, Python básico §§1–2, pp. 2–3","10 min","Delgado Quintero, cap. 3 §3.1 pp. 46–51; cap. 4 §4.1 pp. 100–103; cap. 6 §6.1 pp. 210–213","45 min"),
("Garcimartín, Python básico §§3–4, pp. 4–7","15 min","Delgado Quintero, cap. 5 §§5.3 y 5.5 pp. 174–178 y 201–205; cap. 6 §6.3 pp. 280–282","45 min"),
("Garcimartín, NumPy §§1–2, pp. 22–24","15 min","Garcimartín, NumPy §§3–4 pp. 24–25 y matplotlib §§1–2 pp. 26–30; Delgado Quintero, cap. 8 §8.2 pp. 326–330","45 min"),
("Delgado Quintero, cap. 8 §8.3.1, pp. 370–373","15 min","Delgado Quintero, cap. 8 §8.3.2, pp. 381–385, 422–424 y 427–432","45 min"),
("Delgado Quintero, cap. 6 §6.3, pp. 280–282","10 min","Delgado Quintero, cap. 6 §§6.3–6.4, pp. 283–291; Garcimartín, Python básico §9, pp. 12–13","30 min dentro del repaso de 60")]

def bibliography():
    text=front("Bibliografía y plan de lectura","referencias",minutes="Consulta integrada")+"""# Bibliografía y plan de lectura

## Dos libros locales

**Garcimartín, A. (2022). *Introducción a Python para cálculo científico*. Sprinter Verlag.** PDF de 60 páginas físicas, ISBN 978-84-8081-728-8. Autor y editorial tal como aparecen; no se expande la inicial A. Portada interior y pie editorial verifican 2022. Archivo: ◊Recursos SpaceApps/Libros/python-calculo-cientifico.pdf◊.

Resumen útil para repasar sintaxis y pasar a arreglos y gráficos. Quien empieza de cero necesita las trazas y prácticas del bloque. Índice impreso p. 1 sin números de página: se verificaron los encabezados en el cuerpo. En el texto principal, página física PDF = página impresa + 3; no aplicar esta regla a anexos.

**Delgado Quintero, S. (2022). *Aprende Python* [PDF, versión del 12 de diciembre de 2022].** Documento del autor, sin editorial identificada. PDF de 516 páginas físicas. Archivo: ◊Recursos SpaceApps/Libros/python-aprende-sergio-delgado-quintero.pdf◊. Portada, metadatos e índice i–ii verifican autor, título, fecha y capítulos.

Para principiantes que necesitan ampliar tipos, control, colecciones o funciones. El capítulo 8 reúne NumPy, pandas y Matplotlib. En el texto principal, página física PDF = página impresa + 4. Los rangos son selecciones dentro de secciones comprobadas, no capítulos enteros obligatorios.

## Lecturas por día

La lectura núcleo sustituye parte de los 75 min de conceptos; **no suma tiempo**. Las notas también permiten completar esa lectura sin abrir los PDF. En ampliación, detente al agotar el tiempo y marca páginas pendientes.
"""
    text+=table(["Día","Núcleo","Tiempo incluido","Ampliación","Tiempo"],[(i,*r) for i,r in enumerate(READINGS,1)])
    text+="\n## Nota → capítulos y páginas comprobados\n\nG = Garcimartín (2022); DQ = Delgado Quintero (2022). En G, el nombre del bloque desambigua secciones cuya numeración se reinicia. Un antecedente no equivale a cobertura de una API.\n"
    for c in CONCEPTS:
        text+=f"\n- {link(NOTE_NAMES[(c['day']-1)*3+c['number']-1])}: {c['sources']}\n"
    rows=[
    ("P1.1","Python básico §§1–2, pp. 2–3","cap. 3 §§3.1–3.2, pp. 46–72"),
    ("P1.2","Python básico §§5–6, pp. 8–10","cap. 4 §§4.1–4.2, pp. 100–136"),
    ("P1.3","Python básico §9, pp. 12–13","cap. 6 §6.1, pp. 210–250"),
    ("P2.1","Python básico §§3–4,8, pp. 4–7,11–12","cap. 5 §§5.1–5.4, pp. 138–200"),
    ("P2.2","Tópicos adicionales §3, pp. 39–41; §5 p. 44","cap. 5 §§5.1–5.3, pp. 138–191; §6.2 p. 251"),
    ("P2.3","Python básico §§7,11, pp. 10–11,16–19","§5.5 pp. 201–208; §§6.3–6.4 pp. 280–294"),
    ("P3.1","NumPy §§1–2 pp. 22–24","§8.2 pp. 326–368"),
    ("P3.2","NumPy §§3–4 pp. 24–25","§8.2 pp. 326–368"),
    ("P3.3","matplotlib §§1–2 pp. 26–30","§8.4 pp. 433–474"),
    ("P4.1","§11 pp. 16–19: archivos, sin pandas","§8.3 pp. 369–432"),
    ("P4.2","Sin pandas temporal","§8.3 pp. 369–432: Series/agrupación; fechas mediante documentación"),
    ("P4.3","Sin pandas; §11 pp. 16–19: archivos","§8.3.2: agrupación pp. 427–428; merge pp. 431–432"),
    ("P5.1","§§7,9 pp. 10–13: antecedente de llamadas","§§6.1–6.2 pp. 210–251: antecedente de funciones/objetos"),
    ("P5.2","NumPy §§1–2 pp. 22–24: antecedente; sin xarray","§8.2 pp. 326–368: antecedente; sin xarray"),
    ("P5.3","Python básico §9 pp. 12–13: funciones","§§6.3–6.4 pp. 280–294: errores/módulos")]
    text+=table(["Nota","G","DQ"],rows)
    text+="""\n## Correcciones y APIs actuales

- G p. 4 llama inmutable a set: se corrige a mutable según Python.
- G p. 22 puede confundir ejes: en a[fila,columna], axis=0 reduce filas y deja una cifra por columna.
- Se usan default_rng, Figure/Axes y ME/YE. La documentación estable de pandas puede mostrar 3.x; aquí se ejecutó 2.3.3.
- Los libros no desarrollan las APIs SciPy, xarray, Git y pytest de este bloque; se recurre a documentación oficial.

## Fuentes web

URLs abiertas al preparar el material. Colab puede pedir sesión; Pythia respondió con un aviso de interfaz dinámica. Las versiones ejecutadas constan en el informe.
"""
    text+=table(["Recurso","Propósito"],[(f"[{n}]({u})",p) for n,u,p in SOURCES])
    text+="""\n## Bibliografía posterior

*Think Stats* (Allen Downey); *Forecasting: Principles and Practice* (Hyndman y Athanasopoulos); *Python Data Science Handbook* (VanderPlas); Project Pythia; tutoriales de Earthdata; documentación de earthaccess y pymannkendall; Khan Academy, 3Blue1Brown y StatQuest. Se citan por nombre, sin asignar ediciones o páginas no verificadas.

## Guía de cita

Usa Apellido, año, capítulo o bloque, sección y páginas, enlazando esta nota. Para APIs registra recurso, función, URL, fecha de consulta y versión ejecutada. Para datos NASA registra producto, versión, variable, unidad, dominio, periodo y fecha de descarga; no inventes DOI.

Ejercicios, código y figuras son originales para este bloque. No se reproducen pasajes ni código textual de los libros. Los PDF no se modificaron.
"""
    write("P.B Bibliografía y plan de lectura.md",text)

def figure_block(f):
    code=f["code"]+f'\nfig.savefig("{f["name"]}", dpi=100, bbox_inches="tight")\nplt.close(fig)'
    return f'\n![[{f["name"]}]]\n\n{f["caption"]}\n\n> [!tip]- Código de figura · ampliación o soporte\n> Ejecuta desde assets; para P5 carga malla de P.D. tight_layout ajusta márgenes; savefig exporta; close libera memoria.\n'+quote(fence(code))

def concepts():
    flows=[
    ["Etiqueta","Valor con tipo","Conversión con unidad"],["Dato","Condición positiva","Actualizar conteo"],
    ["Serie y referencia","Función anomalia","Lista de diferencias"],["Datos","Colección","Posición o clave"],
    ["Objeto","Método o atributo","Resultado"],["Leer campo","try convertir","Dato o except registrado"],
    ["Lista","Arreglo con shape","Selección"],["Tiempo por región","Referencia por región","Anomalías"],
    ["Figure","Axes","Datos y etiquetas"],["CSV","Índice y columnas","Filas válidas"],
    ["Fechas","Base mensual","Anomalías","Año y cobertura"],["Separar","Aplicar","Combinar"],
    ["Pares válidos","Estimador","Campos y unidades"],["Dimensiones y coordenadas","Dataset","Selección y reducción"],
    ["Archivos","git add prepara","git commit registra localmente"]]
    for i,c in enumerate(CONCEPTS):
        d,n=c["day"],c["number"]; title=TITLES[d-1][n-1];name=NOTE_NAMES[i]
        prev=NOTE_NAMES[i-1] if i else "P.0 Empezar aquí"
        nxt=NOTE_NAMES[i+1] if i<14 else "P.Z Proyecto integrador"
        lib="python" if d<3 or (d,n)==(5,3) else {3:"numpy",4:"pandas",5:"scipy"}[d]
        if (d,n)==(3,3):lib="matplotlib"
        if (d,n)==(5,2):lib="xarray"
        level="básico" if d==1 or (d,n)==(2,1) else "avanzado" if (d,n) in [(3,2),(4,2),(4,3),(5,2),(5,3)] else "intermedio"
        with tempfile.TemporaryDirectory(dir=WORK) as td:
            old=Path.cwd();os.chdir(td)
            try:
                ns={};output=execute(c["code"],ns);execute(c["solution"],ns)
            finally:os.chdir(old);plt.close("all")
        err=traceback_real(c["error"])
        text=front(title,day=d,order=n,level=level,library=lib,prereq=[prev])
        text+=f"# {title}\n\n> [!abstract] Qué hace\n> {c['task']}.\n\n> [!question] Tarea del Detective\n> {c['app']}\n\n## Modelo mental y sintaxis mínima\n"
        text+=concept_diagram(d,n,flows[i])+c["extra"]+"\n"+c["theory"]+"\n"
        text+="\n> [!info] Tiempo\n> 15 min lectura/ejemplos + 10 min Prueba tú. Las ampliaciones se estudian dentro de su presupuesto opcional.\n"
        text+=fence(c["code"])+"Salida esperada, capturada al ejecutar:\n"+fence(output or "(sin salida)","text")
        text+=table(["Paso o elemento","Línea u operación","Estado o interpretación"],c["trace"])
        text+="\n> [!warning] Error intencional · ejecuta separado\n> "+c["fix"]+"\n"+quote(fence(c["error"]))+quote(fence(err,"text"))
        for bad,explanation in c.get("errors_extra",[]):
            text+="\n> [!warning]- Otro error intencional\n> ❌ "+explanation+" ✅ Repara la causa antes de seguir.\n"
            text+=quote(fence(bad))+quote(fence(traceback_real(bad),"text"))
        if (d,n)==(5,3):
            text+=diagram(["Última línea: tipo y mensaje","Última llamada propia: archivo y línea","Entrada que incumple el contrato","Corregir y repetir"])
        text+="\n## Prueba tú · 10 min\n"+"\n".join(f"{j}. {m}" for j,m in enumerate(c["micro"],1))+"\n\n> [!success]- Solución comprobada\n"+quote(fence(c["solution"]))
        text+="\n## Mini aplicación al reto\n\n"+c["app"]+"\n"
        for f in FIGURES:
            if f["note"]==f"P{d}.{n}":text+=figure_block(f)
        text+=f"\nEnlaces: {link(prev,'Antes')} → {link(nxt,'Después')} · {link(f'P{d}.E Ejercicios P{d}','Practicar')}.\n\n## Flashcards\n"
        text+="\n".join(f"{q}::{a}" for q,a in c["cards"])+"\n\n- [ ] Reproduzco la salida y paso los asserts de Prueba tú sin copiar.\n- [ ] Explico forma, unidad y origen simulado.\n\n## Fuentes\n"
        text+=c["sources"]+"\n"+link("P.B Bibliografía y plan de lectura","Páginas y documentación verificada")+".\n"
        write(Path(FOLDERS[d-1])/(name+".md"),text)

def render_ex(e):
    mark="◆" if e["section"]=="Núcleo" else "➕"
    starter=(e["setup"]+"\n" if e["setup"] else "")+"# TU CÓDIGO AQUÍ"
    solution=(e["setup"]+"\n" if e["setup"] else "")+e["solution"]
    return (f"> [!question] {e['id']} · {mark} · {'⭐'*e['stars']} · {e['kind']} · {e['minutes']} min · {e['title']}\n"+
        quote("Datos simulados. "+e["prompt"])+quote(fence(starter))+"> > [!example]- Comprueba tu respuesta\n"+quote(fence(e["check"]),2)+
        "> > [!tip]- Pista\n"+quote(e["hint"],2)+"> > [!success]- Solución\n"+quote(fence(solution),2)+quote("**Por qué:** "+e["why"],2)+"\n")

INSTALL='%pip install -q "numpy>=2,<3" "pandas>=2.2,<3" matplotlib scipy xarray netCDF4 statsmodels pymannkendall pytest'
def notebook(day,entries):
    name=NB_NAMES[day-1] if isinstance(day,int) else NB_NAMES[-1]
    gens=GENERATORS[:1] if isinstance(day,int) and day<4 else GENERATORS[:2] if day==4 else GENERATORS
    cells=[nbf.v4.new_markdown_cell(f"# {name}\n\nTodos los datos son **simulados**. Lee primero las tres notas del día. Completa una celda y ejecuta su comprobación; esta fallará hasta resolver el ejercicio. Resolver aquí cuenta como los ejercicios de la nota, no duplica el trabajo.\n\nLa primera celda de código contiene los generadores pertinentes de P.D, idénticos a la nota. P1–P3: solo serie_anual. P4: añade serie_mensual. P5: añade malla. Las funciones importan dependencias al llamarse. Si faltan bibliotecas ejecuta antes la instalación opcional.\n\nEjecuta en un directorio de práctica: se crean CSV y NetCDF allí. No se necesitan archivos de datos externos."),
        nbf.v4.new_code_cell("\n\n".join(gens),metadata={"role":"datos"}),
        nbf.v4.new_markdown_cell("## Instalación opcional para Colab\n\n%pip instala en el entorno del notebook. Ejecuta una vez antes de usar bibliotecas; reinicia si cambiaste versiones. En local usa venv y requirements.txt."),
        nbf.v4.new_code_cell(INSTALL,metadata={"role":"instalacion","tags":["instalacion-opcional"]})]
    if day==3:cells.append(nbf.v4.new_markdown_cell("Las comprobaciones gráficas inspeccionan lines, patches, collections y métodos get_: listas de elementos dibujados y propiedades. No necesitas escribir ese soporte."))
    if day=="Z":cells.append(nbf.v4.new_markdown_cell("Las etapas comparten variables: ejecuta en orden. Git solo se inicializa en una carpeta de práctica; **no se ejecuta commit ni push**."))
    section=None
    for e in entries:
        if e["section"]!=section:
            section=e["section"];total=sum(x["minutes"] for x in entries if x["section"]==section)
            cells.append(nbf.v4.new_markdown_cell(f"## {section} · {total} min"))
        cells.append(nbf.v4.new_markdown_cell(f"### {e['id']} · {'⭐'*e['stars']} · {e['kind']} · {e['minutes']} min · {e['title']}\n\n**Datos simulados.** {e['prompt']}\n\n<details><summary>Pista</summary>\n\n{e['hint']}\n\n</details>",metadata={"exercise_id":e["id"],"minutes":e["minutes"],"section":section}))
        cells.append(nbf.v4.new_code_cell((e["setup"]+"\n" if e["setup"] else "")+"# TU CÓDIGO AQUÍ",metadata={"exercise_id":e["id"],"role":"respuesta"}))
        cells.append(nbf.v4.new_code_cell(e["check"],metadata={"exercise_id":e["id"],"role":"comprobacion"}))
    nb=nbf.v4.new_notebook(cells=cells,metadata={"kernelspec":{"display_name":"Python 3","language":"python","name":"python3"},"language_info":{"name":"python","version":platform.python_version()},"bloque":"P"})
    nbf.validate(nb);write(Path("notebooks")/(name+".ipynb"),nbf.writes(nb))

def exercises():
    for d in range(1,6):
        entries=[e for e in EXERCISES if e["day"]==d]
        core=sum(e["minutes"] for e in entries if e["section"]=="Núcleo");amp=sum(e["minutes"] for e in entries if e["section"]=="Ampliación")
        text=front(f"Ejercicios P{d}","practica",day=d,order=4,minutes=f"{core} min + {amp} min opcionales",prereq=[NOTE_NAMES[d*3-1]],extra={"tiempo_nucleo":core,"tiempo_ampliacion":amp})
        text+=f"# Ejercicios P{d}\n\nCompleta primero las tres notas. Estos ejercicios coinciden con {link(NB_NAMES[d-1]+'.ipynb','el notebook')}; resolverlos allí cuenta como esta práctica, no como una segunda tanda.\n\nDatos simulados. Copia los generadores pertinentes de {link('P.D Datos sintéticos de práctica','P.D')} o usa el notebook. Cada ejercicio regular contiene sus entradas. Ejecuta la solución y luego la comprobación.\n\n> [!tip] Regla de atasco\n> Al doble del tiempo abre la pista; al triple lee la solución, ciérrala y repite. Al agotar la sesión usa el tiempo restante para entender la solución; lleva repeticiones adicionales al refuerzo opcional.\n"
        if d==3:text+="\nSoporte de comprobaciones gráficas: lines, patches y collections son colecciones de elementos dibujados; get_... lee sus propiedades.\n"
        if d==5:text+="\nPara la prueba de ampliación ejecuta en terminal de práctica: ◊python -m pytest test_conversion.py◊. Ningún ejercicio ejecuta commit ni push.\n"
        for sec in ["Núcleo","Ampliación"]:
            total=sum(e["minutes"] for e in entries if e["section"]==sec)
            text+=f"\n## {'◆' if sec=='Núcleo' else '➕'} {sec} · {total} min\n\n"
            for e in entries:
                if e["section"]==sec:text+=render_ex(e)
        nxt=f"P{d+1}.0 Índice P{d+1}" if d<5 else "P.Z Proyecto integrador"
        text+=f"\n## Reto de integración y autoevaluación\n\nEl último reto de cada sección integra el día. El reto final es {entries[-1]['id']}; ya está incluido en el tiempo.\n\n- [ ] Paso los asserts del núcleo y explico una corrección.\n- [ ] Distingo dato simulado, operación y unidad.\n- [ ] Repito el reto núcleo sin mirar.\n\nCierra con las cinco preguntas de {link(f'P{d}.0 Índice P{d}')}. Sigue en {link(nxt)}.\n"
        write(Path(FOLDERS[d-1])/f"P{d}.E Ejercicios P{d}.md",text);notebook(d,entries)

def data_note():
    text=front("Datos sintéticos de práctica","datos",minutes="Soporte distribuido en P1–P5")+"""# Datos sintéticos de práctica

> [!warning] Todo es simulado
> Ninguna cifra es una medición NASA. Las tasas son impuestas para practicar; no uses las salidas como evidencia del sistema terrestre.

Lee por etapas: serie_anual después de P1.3; CSV después de P2.3; figura después de P3.3; serie_mensual después de P4.3; malla después de P5.2. Los notebooks incluyen únicamente los generadores necesarios, idénticos a esta nota. Son soporte suministrado, no ejercicios adicionales.
"""
    text+=diagram(["Nivel","Tendencia","Estacionalidad","Variabilidad lenta","Ruido","Serie simulada"])
    text+="\nLos componentes se suman; el diagrama indica el orden de construcción. La anatomía formal de una serie va en bloque C (nota pendiente). La semilla fija permite repetir ruido pseudoaleatorio; no lo convierte en observación.\n"
    text+=table(["Generador","Salida","Convención"],[("serie_anual","Lista de 24 valores","2000–2023; nivel 14 °C; tasa 0.02 °C/año; sin ruido"),("serie_mensual","DataFrame de 864 filas","288 meses × 3 regiones; 2000–2023; nueve ausencias opcionales"),("malla","Dataset 24×3×4","24 meses desde 2000; lat/lon en grados; temperatura degC")])
    for title,code in zip(["Serie anual · P1","Serie mensual · P4","Malla · P5"],GENERATORS):
        text+=f"\n## {title}\n"+fence(code)
    text+="\n## CSV sencillo · P2\n\nTres observaciones simuladas; el campo vacío de 2001 es ausencia. Los ejercicios escriben este texto embebido.\n"+fence(CSV_SIMPLE,"csv")
    text+="\n## Comprobaciones de soporte · después de P5\n"+fence('''a=serie_anual()
b=serie_mensual(faltantes=True)
ds=malla()
assert len(a)==24, "Veinticuatro valores"
assert len(b)==864 and b["temp_C"].isna().sum()==9, "Tres ausencias por región"
assert b.equals(serie_mensual(faltantes=True)), "Repetibilidad"
assert ds["temp"].shape==(24,3,4), "Tiempo, latitud, longitud"
assert ds.attrs["origen"]=="simulado", "Procedencia explícita"''')
    text+=figure_block(next(f for f in FIGURES if f["note"]=="P.D"))
    text+="\nLas figuras P3 y P4 usan simulaciones mínimas propias para evitar dependencias antes de tiempo. Para datos reales reemplaza el generador por un producto NASA con metadatos, controles de calidad, cobertura y unidades verificadas.\n\nFuentes: "+link("P.B Bibliografía y plan de lectura")+"; diseño original de simulaciones.\n"
    write("P.D Datos sintéticos de práctica.md",text)

def project_note():
    text=front("Detective de tendencias en miniatura","proyecto",day=5,order=5,level="intermedio",minutes="95 min + 120 min opcionales",prereq=[NOTE_NAMES[-1]],extra={"tiempo_nucleo":95,"tiempo_ampliacion":120})
    text+="""# Detective de tendencias en miniatura

> [!abstract] Entrega
> Una tabla de tasas, una figura y cinco líneas de conclusión reproducibles. Datos simulados en tres regiones.

Parte del Día 5: núcleo 95 min, ampliación 120 min. Las etapas comparten variables; ejecútalas en orden en el notebook. Los asserts comprueban cálculos, no validan por sí solos una inferencia científica.

Entrada: P.D. Salida: temperaturas y anomalías en °C; tasas en °C/década, con periodo y base explícitos. Doce meses válidos por año es una regla didáctica conservadora, no un estándar universal.
"""
    text+=diagram(["CSV simulado","Limpiar y contar","Base mensual 2000–2009","Anomalías anuales","Tasas y figura","Conclusión"])
    text+=f"\nEnlaces: {link('P.D Datos sintéticos de práctica','Datos')} · {link(NB_NAMES[-1]+'.ipynb','Notebook autosuficiente')}.\n"
    for sec,total in [("Núcleo",95),("Ampliación",120)]:
        text+=f"\n## {'◆' if sec=='Núcleo' else '➕'} {sec} · {total} min\n\n"
        for e in PROJECT:
            if e["section"]==sec:text+=render_ex(e)
        if sec=="Núcleo":text+=figure_block(next(f for f in FIGURES if f["note"]=="P.Z"))
    text+="""\n## Rúbrica

- [ ] Origen simulado; 864 filas y 9 faltantes detectados.
- [ ] Base 2000–2009 con diez valores de cada mes por región.
- [ ] Veintiún años completos por región; años reales con sus huecos.
- [ ] Tabla con unidad, periodo, base, método, cobertura y origen.
- [ ] Tres series, tres rectas y barras; huecos visibles.
- [ ] Cinco líneas: pregunta, datos, método, resultado y límite.
- [ ] Ampliación: método robusto y mapa marcado como demostración de dos años.
- [ ] Ampliación: README, .gitignore y repositorio local si Git está disponible; sin commit ni push.

Cada casilla vale un punto. Las seis primeras completan el núcleo; las otras dos no bloquean el cierre. Un pvalue no basta para afirmar significancia válida con dependencia temporal: revisar en bloques B y C.

## Qué viene después
"""
    text+=table(["Bloque","Decisión siguiente"],[("B Probabilidad y estadística (nota pendiente)","Incertidumbre, supuestos y pruebas"),("C Series de tiempo (nota pendiente)","Autocorrelación, estacionalidad y cobertura"),("D Matemáticas espaciales (nota pendiente)","Áreas, ponderación y proyecciones"),("F Comunicación y producto (nota pendiente)","Datos NASA, relato y entrega")])
    text+="\nFuentes: "+link("P.B Bibliografía y plan de lectura")+".\n"
    write("P.Z Proyecto integrador.md",text);notebook("Z",PROJECT)

QUESTIONS=[
["¿Qué diferencia = de ==?","¿Por qué convertir texto con float?","¿Cuándo termina range?","¿Dónde se inicia un acumulador?","¿Qué cambia al sustituir return por print?"],
["¿Qué cambia al modificar un alias?","¿Cuál es el último índice?","¿Qué devuelve sort?","¿Qué pierde zip con longitudes distintas?","¿Por qué conservar el año al descartar un valor?"],
["¿Qué describen shape y ndim?","¿Cuándo hace falta copy?","¿Qué elimina axis=0?","¿Por qué NaN no es cero?","¿Qué implican límites simétricos de color?"],
["¿Qué diferencia loc de iloc?","¿Cómo se crea un índice temporal?","¿Qué datos forman la climatología?","¿Cuántos meses exige el proyecto?","¿Qué detecta validate en merge?"],
["¿En qué unidad está slope?","¿Por qué conservar años con huecos?","¿Qué diferencia sel de isel?","¿Qué debe conservar NetCDF?","¿Qué limita la conclusión?"]]
ANSWERS=[
["Asignación frente a comparación.","Para calcular numéricamente.","Antes del límite final.","Antes del bucle.","print muestra y devuelve None."],
["Ambos nombres ven la misma lista.","-1.","None; modifica la lista.","Elementos sobrantes de la más larga.","Para no desplazar correspondencias temporales."],
["Tamaños y número de ejes.","Para independizar una vista que modificarás.","El primer eje: tiempo si es tiempo×región.","Es ausencia, no observación.","Cero central y magnitudes opuestas comparables."],
["Etiquetas frente a posiciones.","to_datetime y set_index.","La base declarada agrupada por mes.","Doce válidos.","Claves que incumplen la cardinalidad."],
["Unidad de y por unidad de x.","Para no comprimir intervalos faltantes.","Coordenadas frente a posiciones.","Dimensiones, coordenadas, unidades y origen.","Simulación y supuestos estadísticos pendientes."]]
def hh(n):return f"{n//60:02}:{n%60:02}"
def indices():
    cheats=[
    [("float(texto)","Convertir a decimal"),("if / for / while","Decidir y repetir"),("def ... return","Reutilizar"),("assert condición, mensaje","Comprobar")],
    [("a[-1],a[:3]","Último y rebanada"),("d.items(),zip(a,b)","Pares"),("sorted(a,key=f)","Ordenar"),("with open / try except","Archivo y error")],
    [("shape / reshape","Leer/cambiar forma"),("a[mascara]","Seleccionar"),("nanmean(a,axis=0)","Media por columna"),("fig,ax=plt.subplots()","Lienzo y eje")],
    [("loc / iloc","Etiquetas/posiciones"),("resample YE","Agrupar año"),("groupby mes","Referencias mensuales"),("merge validate","Unir con comprobación")],
    [("linregress(x,y).slope*10","Tasa por década con x anual"),("theilslopes(y,x)","Orden inverso"),("sel / isel / mean","Seleccionar y reducir"),("git status","Leer cambios")]]
    for d in range(1,6):
        entries=[e for e in EXERCISES if e["day"]==d];core=sum(e["minutes"] for e in entries if e["section"]=="Núcleo")
        text=front(f"Índice P{d}","indice",day=d,order=0,minutes="240 min + 240 min opcionales")+f"# Día {d} · {FOLDERS[d-1].split(' ',1)[1]}\n\nObjetivo: {CONCEPTS[(d-1)*3]['task'].lower()}.\nAl terminar podrás {CONCEPTS[d*3-1]['task'].lower()}.\n\n## Plan hora por hora · estudio efectivo\n"
        tasks=[("Entorno 15 + diagnóstico 15",30)] if d==1 else [("Flashcards del día anterior",15)]
        tasks += [(f"P{d}.{n}: lectura 15 + Prueba tú 10",25) for n in range(1,4)]
        remain=core
        while remain:
            chunk=min(60,remain);tasks.append(("Ejercicios núcleo en notebook",chunk));remain-=chunk
        if d==5:tasks += [("Proyecto núcleo etapas 1–3",55),("Proyecto núcleo etapas 4–5",40)]
        tasks.append(("Cierre: cinco preguntas",10))
        rows=[];clock=0
        for label,mins in tasks:
            rows.append((f"{hh(clock)}–{hh(clock+mins)}","◆ Núcleo",label,mins));clock+=mins
        assert clock==240
        optional=[("Lectura",45),("Ejercicios extra",60),("Ejercicios extra",60),("Ejercicios extra",30),("Refuerzo de errores",45)] if d<5 else [("Ejercicios extra",60),("Proyecto ampliado etapas 6–8",60),("Proyecto ampliado etapas 9–11",60),("Repaso: lectura 30 + flashcards 15 + repetir fallo 15",60)]
        for label,mins in optional:
            rows.append((f"{hh(clock)}–{hh(clock+mins)}","➕ Ampliación",label,mins));clock+=mins
        text+=table(["Hora acumulada","Ruta","Actividad","Min"],rows)
        text+="\nHaz pausas según necesidad: cuatro horas de estudio efectivo. Resolver en notebook cuenta dentro de ejercicios. Lleva apartados ➕ y repeticiones adicionales al presupuesto opcional.\n"
        text+=f"\n## Lectura recomendada\n\nNúcleo: {READINGS[d-1][0]} · {READINGS[d-1][1]}, incluido en conceptos. Ampliación: {READINGS[d-1][2]} · {READINGS[d-1][3]}. {link('P.B Bibliografía y plan de lectura','Páginas verificadas')}.\n"
        text+=table(["Nota","Nivel"],[(link(f"P{d}.{n} {t}"),"⭐" if d==1 and n<3 or (d,n)==(2,1) else "⭐⭐⭐" if (d,n) in [(3,2),(4,2),(4,3),(5,2),(5,3)] else "⭐⭐") for n,t in enumerate(TITLES[d-1],1)])
        text+=f"\n{link(f'P{d}.E Ejercicios P{d}','Ejercicios')} · {link(NB_NAMES[d-1]+'.ipynb','Notebook')}.\n\n## Al terminar sabrás\n"
        text+="\n".join(f"- [ ] {c['task']}." for c in CONCEPTS[(d-1)*3:d*3])+"\n\n## Chuleta rápida\n"+table(["Sintaxis","Uso"],cheats[d-1])
        text+="\n## Cierre del día · 10 min\n\nDos minutos por pregunta. Responde sin mirar y verifica; registra un fallo para mañana.\n\n"
        text+="\n".join(f"{i}. {q}" for i,q in enumerate(QUESTIONS[d-1],1))+"\n\n> [!success]- Respuestas\n"+quote("\n".join(f"{i}. {a}" for i,a in enumerate(ANSWERS[d-1],1)))
        prev=f"P{d-1}.0 Índice P{d-1}" if d>1 else "P.0 Empezar aquí";nxt=f"P{d+1}.0 Índice P{d+1}" if d<5 else "P.Z Proyecto integrador"
        text+=f"\nAntes: {link(prev)} · Después: {link(nxt)}.\n"
        write(Path(FOLDERS[d-1])/f"P{d}.0 Índice P{d}.md",text)

def start():
    text=front("Empezar aquí","indice",minutes="30 min incluidos en Día 1")+"""# Bloque P — Python desde cero

Para compañeros que nunca han programado y necesitan seguir código científico del Detective. En cinco días practicarás cargar → limpiar → anomalías → tendencia → mapa → compartir. La teoría estadística y espacial sigue en otros bloques.

Ruta: concepto → Prueba tú → ejercicios en notebook → cierre. El notebook contiene los mismos ejercicios que la nota: se resuelven una vez. Todas las cifras y figuras son **simuladas**. El nombre del reto y el contexto NASA Space Apps 2026 proceden del encargo; no se presentan como convocatoria oficial verificada.

## Plan de cinco días
"""
    rows=[]
    for d in range(1,6):
        core="30 entorno y diagnóstico + 75 conceptos + 125 ejercicios + 10 cierre" if d==1 else "15 repaso + 75 conceptos + 140 ejercicios + 10 cierre" if d<5 else "15 repaso + 75 conceptos + 45 ejercicios + 95 proyecto + 10 cierre"
        amp="150 ejercicios + 45 lectura + 45 refuerzo" if d<5 else "60 ejercicios + 120 proyecto + 60 repaso"
        rows.append((d,link(f"P{d}.0 Índice P{d}"),core,amp))
    text+=table(["Día","Subbloque","◆ Núcleo 240 min","➕ Ampliación 240 min"],rows)
    text+="""\nCada concepto: 15 min lectura/ejemplos + 10 Prueba tú. La lectura del libro núcleo se integra en esos 15 min. Día 1: 15 min entorno y 15 diagnóstico. Desde Día 2: 15 min flashcards del día anterior.

Los tiempos son estimaciones para principiantes, no una garantía individual. Al agotarse una sesión usa pistas y soluciones; lleva repeticiones adicionales a ampliación. Conserva el cierre y el proyecto.

| Disponibilidad | Calendario |
|---|---|
| 4 h diarias | Lunes P1, martes P2, miércoles P3, jueves P4, viernes P5 con P.Z; solo núcleo |
| 8 h diarias | Cada día P1–P5: núcleo y ampliación; el quinto incluye ambos niveles del proyecto |
| Fin de semana doble | Jueves P1 4 h, viernes P2 4 h, sábado P3 4 h + P4 4 h, domingo P5 con P.Z 4 h + ampliación 4 h |

Un fin de semana puede doblar dedicación: núcleo + ampliación, o dos días de núcleo. Sigue P1 → P2 → P3 → P4 → P5 → P.Z. **No saltes el proyecto del Día 5.**

## Leyenda y estudio

- ◆ Núcleo; ➕ ampliación.
- ⭐ básico 5 min; ⭐⭐ intermedio 10–12 min; ⭐⭐⭐ avanzado 20 min. Retos Tierra 15–25 min, con su tiempo explícito.
- Tipos: Predice la salida; Corrige el error; Completa el código; Escribe desde cero; Reto Tierra con P.D.
- La distribución por cantidad ronda 40 % básico, 45 % intermedio y el resto avanzado. P5 tiene cinco ejercicios: 40/40/20.
- Atasco: al doble del tiempo abre la pista; al triple abre la solución, ciérrala y repite.
- Repasa flashcards ◊pregunta::respuesta◊ sin mirar primero; pueden usarse sin complemento.

Fuera del bloque: generadores con yield, decoradores, clases complejas, pytest avanzado, dask, Parquet y Docker.

## Mapa del Detective
"""
    text+=diagram(["Datos NASA en el reto real","Cargar P2.3 y P4.1","Limpiar P4.1","Anomalías P4.2","Tendencia P5.1","Mapa P5.2","Compartir P5.3 y P.Z"])
    text+="Enlaces: "+" · ".join(link(n) for n in [NOTE_NAMES[5],NOTE_NAMES[9],NOTE_NAMES[10],NOTE_NAMES[12],NOTE_NAMES[13],NOTE_NAMES[14],"P.Z Proyecto integrador"])+".\n"
    text+="""\n## Tres rutas de ejecución · elige una

**Colab, sin instalar en tu computadora.** Abre Colab desde la bibliografía, inicia sesión si se solicita, elige Archivo → Subir notebook y selecciona el ipynb del día. Shift+Enter ejecuta una celda. Ejecuta la celda %pip antes de necesitar bibliotecas; se instala en la sesión remota. Descarga el notebook para conservar trabajo; los archivos de la sesión son temporales. [Colab oficial](https://research.google.com/colaboratory/faq.html).

**Local con VS Code o Jupyter.** Python 3.13 reproduce la versión principal comprobada. Abre terminal en P Python desde cero, crea un entorno y usa su intérprete. VS Code: Python: Select Interpreter → .venv; para notebooks selecciona ese kernel. [VS Code oficial](https://code.visualstudio.com/docs/python/environments).
"""
    text+=fence('python -m venv .venv\n.venv\\Scripts\\python.exe -m pip install -r requirements.txt\n.venv\\Scripts\\python.exe -m pip install notebook\n.venv\\Scripts\\python.exe -m notebook',"powershell")
    text+="\nEn macOS/Linux sustituye el intérprete por ◊.venv/bin/python◊. También puedes guardar ◊practica.py◊ y ejecutarlo con el intérprete del entorno. Notebook mezcla texto y celdas; un archivo .py contiene instrucciones. [venv](https://docs.python.org/3.13/tutorial/venv.html) y [Jupyter](https://jupyter.org/install).\n"
    text+="\n**conda.** Si ya está instalado, crea un entorno independiente y después instala los requisitos dentro. Son comandos de terminal, no Python. [conda oficial](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).\n"
    text+=fence("conda create -n detective-p python=3.13 pip\nconda activate detective-p\npython -m pip install -r requirements.txt\npython -m pip install notebook\npython -m notebook","bash")
    text+="""\nLa preparación instaló paquetes solo en un entorno virtual temporal. Estas instrucciones son para futuras sesiones. No ejecutes comandos de terminal en una celda Python salvo la celda %pip suministrada.

## Diagnóstico · 10 preguntas · 15 min

Predice sin ejecutar. Si nunca has programado, marca «no sé». Evalúa conocimientos previos; por eso muestra sintaxis aún no enseñada. No consultes soluciones antes de puntuar.
"""
    diagnostic=["print(9//2,9%2)","print(float('2.5')*2)","x=3\nprint(x>0 and x<5)","s=0\nfor i in range(4):\n    s+=i\nprint(s)","def f(x):\n    return x*10\nprint(f(0.02))","a=[1,2,3]\nprint(a[-1],a[:2])","a=[1,2]\nb=a\nb[0]=9\nprint(a)","d={'Costa':14,'Sierra':12}\nprint(d['Costa'])","print([x*2 for x in [1,2,3]])","try:\n    float('')\nexcept ValueError:\n    print('faltante')"]
    for i,code in enumerate(diagnostic,1):text+=f"\n### {i}. Predice la salida\n"+fence(code)
    text+="\n> [!success]- Respuestas · un punto por respuesta completamente correcta\n"
    for i,code in enumerate(diagnostic,1):text+=quote(f"{i}. ◊{execute(code,{})}◊")
    text+="""\n**8–10 puntos:** puedes saltar P1 y P2 y empezar en P3. Dedica las 8 h de núcleo ahorradas a ejercicios de ampliación P3 150 min, P4 150 min y P5 con proyecto ampliado 180 min. Las lecturas y refuerzos adicionales siguen opcionales. Consulta cualquier concepto que hayas fallado antes de usarlo.

**0–7 puntos:** sigue P1–P5. La puntuación mide familiaridad con código, no capacidad científica.

## Seguimiento en Obsidian

El panel requiere Dataview; los índices funcionan sin ese complemento.
"""
    text+=fence('TABLE dia, nivel, tiempo_estimado, estado\nFROM "P Python desde cero"\nWHERE bloque = "P" AND tipo = "python"\nSORT dia ASC, orden ASC',"dataview")
    text+=f"\nComienza: {link('P1.0 Índice P1')} · {link('P.B Bibliografía y plan de lectura')} · {link('P.D Datos sintéticos de práctica')} · {link('P.Z Proyecto integrador')}.\n"
    write("P.0 Empezar aquí.md",text)

def supporting():
    req="\n".join(f"{p}>={v}"+(",<3" if p in ["numpy","pandas"] else "") for p,v in VERSIONS.items() if p!="python")
    write("requirements.txt","# Verificado con Python "+VERSIONS["python"]+"\n# Bibliotecas docentes y de validación; NumPy 2.x y pandas 2.x.\n"+req)
    figscript='''"""Regenera las seis figuras originales dentro de assets."""
from pathlib import Path
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from contenido import GENERATORS
from proyecto import PROJECT, FIGURES
ROOT=Path(__file__).resolve().parent
os.chdir(ROOT)
ns={}
for codigo in GENERATORS:
    exec(codigo,ns)
for figura in FIGURES:
    if figura["note"]=="P.Z":
        for etapa in PROJECT[:3]:
            codigo="\\n".join(l for l in etapa["solution"].splitlines() if "resultados_simulados.csv" not in l)
            exec(codigo,ns)
    exec(figura["code"],ns)
    ns["fig"].savefig(ROOT/figura["name"],dpi=100,bbox_inches="tight")
    plt.close("all")
    print(figura["name"],(ROOT/figura["name"]).stat().st_size)
'''
    write("assets/generar_figuras.py",figscript)
    write("assets/versiones.json",json.dumps(VERSIONS,ensure_ascii=False,indent=2))
    write("assets/mapa_pedagogico.json",json.dumps({f"P{c['day']}.{c['number']}":c["introduced"] for c in CONCEPTS},ensure_ascii=False,indent=2))
    write("assets/fuentes_verificadas.json",json.dumps({"fecha":TODAY,"fuentes":[dict(nombre=n,url=u,proposito=p,verificacion="URL abierta con herramienta web") for n,u,p in SOURCES]},ensure_ascii=False,indent=2))
if __name__=="__main__":
    bibliography();concepts();exercises();data_note();project_note();indices();start();supporting()
    print(json.dumps({"creados":len(CREATED),"omitidos":SKIPPED},ensure_ascii=False))
