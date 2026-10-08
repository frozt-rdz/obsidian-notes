"""Informe final con evidencia y árbol completo, dentro del bloque."""
import contextlib,io,json,os,sys,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"assets"))
import generar_bloque as g
from proyecto import PROJECT
from contenido import GENERATORS
from ejercicios import EXERCISES
report=json.loads((ROOT/"assets/verificacion.json").read_text(encoding="utf-8"))
report.update(mermaid={"herramienta":"npx -y @mermaid-js/mermaid-cli","diagramas":19,"resultado":"Todos renderizados a SVG en carpeta temporal"},
    generadores_notebooks="Identidad literal comprobada con P.D en los seis notebooks",
    urls={"cantidad":23,"http_200":23},
    seguridad={"archivos_previos_en_destino":0,"commit_ejecutado":False,"push_ejecutado":False,"libros_plantillas":"Solo lectura"},
    limitaciones=["No se abrió Obsidian para comprobar el renderizado final.",
                  "No se ejecutaron las seis sesiones dentro de Google Colab ni los comandos de instalación conda/VS Code; se contrastaron con sus documentos oficiales.",
                  "La duración es una estimación editorial, pendiente de prueba con principiantes.",
                  "La longitud informada cuenta el cuerpo sin bloques de código ni frontmatter YAML.",
                  "La revisión pedagógica incluye comprobación manual; no hay un analizador que pruebe exhaustivamente la familiaridad previa con toda API."])
report["limpieza_temporal"]={"estado":"bloqueada por revisión automática","respuesta":"blocked by policy",
    "rutas_restantes":[".venv-temporal/",".trabajo-temporal/","assets/__pycache__/"],
    "detalle":"Se rechazó tanto la eliminación recursiva de directorios propios como la eliminación explícita de archivos de caché. No se intentó otra vía."}
report["limitaciones"].append("La eliminación del entorno y las cachés fue rechazada por la revisión automática con blocked by policy; siguen dentro del bloque. Las copias exitosas de notebooks con soluciones sí fueron descartadas por su contexto temporal.")
with tempfile.TemporaryDirectory(dir=ROOT/".trabajo-temporal") as td:
    old=Path.cwd();os.chdir(td)
    try:
        ns={}
        with contextlib.redirect_stdout(io.StringIO()):
            for code in GENERATORS:exec(code,ns)
            for e in PROJECT[:5]:exec(e["solution"],ns)
        report["resultado_proyecto_simulado"]=ns["tabla"].to_dict("records")
        conclusion=ns["conclusion"]
    finally:os.chdir(old)
name="assets/INFORME_ENTREGA.md"
text=g.front("Informe de entrega y verificación","referencias",minutes="Consulta")+"""# Informe de entrega y verificación

El bloque se escribió directamente en disco. No había una carpeta de destino previa; no se sobrescribió material del usuario. Los libros, las plantillas y las notas de otros bloques se consultaron sin modificarlos. No se ejecutó ningún commit ni push.

## Tiempos reales frente al plan

Los minutos provienen de los encabezados de los ejercicios generados. Las lecturas núcleo están incluidas en los conceptos; no suman tiempo. El notebook contiene los mismos ejercicios y no añade una tanda independiente.
"""
text+=g.table(["Día","Ejercicios núcleo","Ejercicios ampliación","Total núcleo / plan","Total ampliación / plan","Cantidad núcleo / ampliación"],
    [(r["dia"],r["min_ejercicios_nucleo"],r["min_ejercicios_ampliacion"],f'{r["nucleo"]} / 240',f'{r["ampliacion"]} / 240',f'{r["ejercicios_nucleo"]} / {r["ejercicios_ampliacion"]}') for r in report["tiempos"]])
text+="\nP5 incluye proyecto: 95 min núcleo y 120 min ampliación. Total: 60 ejercicios núcleo, 35 de ampliación y 11 etapas de proyecto —5 núcleo y 6 ampliación—. Prueba tú añade 45 microejercicios incluidos en los 75 min diarios de conceptos.\n"
text+="\n## Libros y lectura\n\nGarcimartín, A. (2022), *Introducción a Python para cálculo científico*; Delgado Quintero, S. (2022), *Aprende Python*, versión del 12 de diciembre. PDF originales intactos. Se identificó solo la inicial A. del primer autor, sin ampliarla por suposición.\n"
text+=g.table(["Día","Lectura núcleo incluida","Tiempo","Lectura ampliación","Tiempo"],[(i,*r) for i,r in enumerate(g.READINGS,1)])
text+="\nCitas, tabla de capítulos y equivalencia de páginas impresas/PDF: "+g.link("P.B Bibliografía y plan de lectura")+".\n"
text+="\n## Verificación efectuada\n\n- YAML válido en las notas; campos, etiquetas, prerequisitos y nombres comprobados.\n- Sin marcadores pendientes; tablas continuas, vallas balanceadas, enlaces existentes con alias y sin wikilinks en nodos Mermaid.\n- UTF-8, LF, sin BOM, espacios finales ni saltos triples en las notas.\n- 15 conceptos, tres por día; cuerpos de 55–71 líneas, sin contar código ni YAML. Dos recursos visuales distintos como mínimo en cada nota.\n- 695 ejecuciones de bloques y soporte, incluyendo 106 soluciones con sus asserts. Tracebacks intencionales reales y salidas de los ejemplos contrastadas.\n- Seis notebooks válidos con nbformat, ejecutados con nbclient en copias temporales con soluciones; cantidades, tiempos y comprobaciones coinciden. Copias descartadas.\n- Prueba pytest básica aprobada: un test. No se ejecutaron comandos commit o push.\n- 19 diagramas Mermaid renderizados correctamente con Mermaid CLI.\n- Seis figuras PNG regenerables; todas menores de 150 KB. La mayor ocupa 64 416 bytes. Figura del proyecto inspeccionada visualmente.\n- 23 URLs verificadas mediante herramienta web y respuesta HTTP 200.\n- MS, ME y YE ejecutados en pandas 2.3.3; escritura/lectura NetCDF y conservación de metadatos comprobadas.\n"
text+="\n## Límites y revisión manual recomendada\n\n"+ "\n".join("- "+l for l in report["limitaciones"])+"\n"
text+="\nRevisa a mano P.0 para adecuar calendarios al equipo; P4.2 para reglas de cobertura y base; P5.1 y P.Z para supuestos estadísticos; P5.2 y el mapa ampliado para coordenadas y áreas al cambiar de fuente. Antes de cualquier conclusión terrestre, reemplaza listas, CSV, mallas y tasas simuladas por productos NASA reales con versión, unidad, periodo, dominio y banderas de calidad. El mapa de solo dos años es una demostración de código.\n"
text+="\n## Versiones ejecutadas\n"+g.table(["Componente","Versión"],list(g.VERSIONS.items()))
text+="\nLas dependencias de authoría y comprobación están en requirements.txt, junto con las bibliotecas docentes. Las versiones mínimas de NumPy y SciPy utilizadas requieren Python 3.12 o superior; se verificó Python 3.13.9. La sintaxis enseñada es de Python 3.11 o superior.\n"
text+="\n## Resultado de referencia · datos simulados\n"
text+=g.table(["Región","Tasa OLS °C/década","p OLS sin corrección temporal","Años válidos"],[(r["region"],f'{r["tasa_decada"]:.6f}',f'{r["p_ols"]:.6g}',r["n_anios"]) for r in report["resultado_proyecto_simulado"]])
text+="\nLos valores anteriores son salidas de la simulación; el pvalue no autoriza inferencias sobre la Tierra real ni corrige autocorrelación.\n"+g.quote("[!success]- Conclusión ejecutada\n"+conclusion)
text+="\n## Archivos y mantenimiento\n\nLas fuentes editoriales comunes están en assets/contenido.py, ejercicios.py y proyecto.py; generar_bloque.py produce notas y notebooks y omite archivos existentes. generar_figuras.py regenera PNG. validar_bloque.py repite las comprobaciones. Los JSON conservan evidencias de versiones, fuentes, temas introducidos y resultados. Son recursos de mantenimiento, no contenido adicional de estudio.\n"
def tree(folder,prefix=""):
    paths=sorted((p for p in folder.iterdir() if not p.name.startswith(".")),key=lambda p:(not p.is_dir(),p.name.casefold()))
    if folder==ROOT/"assets" and not any(p.name=="INFORME_ENTREGA.md" for p in paths):
        paths.append(folder/"INFORME_ENTREGA.md");paths.sort(key=lambda p:(not p.is_dir(),p.name.casefold()))
    lines=[]
    for i,p in enumerate(paths):
        last=i==len(paths)-1
        lines.append(prefix+("└── " if last else "├── ")+p.name+("/" if p.is_dir() else ""))
        if p.is_dir():lines+=tree(p,prefix+("    " if last else "│   "))
    return lines
tree_lines=["P Python desde cero/","├── .trabajo-temporal/  [pruebas; limpieza bloqueada]","├── .venv-temporal/  [entorno; limpieza bloqueada]"]+tree(ROOT)
text+="\n## Árbol final\n"+g.fence("\n".join(tree_lines),"text")
(ROOT/name).write_text(g.normalize(text),encoding="utf-8",newline="\n")
(ROOT/"assets/verificacion.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8",newline="\n")
print("Informe guardado; resultado simulado:",[(r["region"],r["tasa_decada"]) for r in report["resultado_proyecto_simulado"]])
