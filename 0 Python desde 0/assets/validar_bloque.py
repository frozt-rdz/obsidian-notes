"""Audita notas, código, presupuesto, notebooks y figuras; temporales dentro del bloque."""
import ast
import contextlib
import copy
import io
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
WORK=ROOT/".trabajo-temporal"
WORK.mkdir(exist_ok=True)
for name,folder in [("MPLCONFIGDIR","mpl"),("IPYTHONDIR","ipython"),("JUPYTER_CONFIG_DIR","jupyter-config"),("JUPYTER_DATA_DIR","jupyter-data"),("JUPYTER_RUNTIME_DIR","jupyter-runtime"),("TEMP","tmp"),("TMP","tmp")]:
    (WORK/folder).mkdir(exist_ok=True)
    os.environ[name]=str(WORK/folder)
os.environ["MPLBACKEND"]="Agg"
os.environ["PYTHONIOENCODING"]="utf-8"
import matplotlib.pyplot as plt
import nbformat
import yaml
from nbclient import NotebookClient
from jupyter_client import KernelManager
from contenido import CONCEPTS,GENERATORS,NOTE_NAMES,FOLDERS
from ejercicios import EXERCISES
from proyecto import PROJECT,FIGURES
REPORT={"errores":[],"avisos":[],"codigo_bloques":0,"ejercicios":0,"notebooks":[],"longitudes":{},"tiempos":[],"figuras":[]}

def check(ok,message):
    if not ok: REPORT["errores"].append(message)
def run(code,ns):
    out=io.StringIO()
    with contextlib.redirect_stdout(out):exec(compile(code,"<nota>","exec"),ns)
    REPORT["codigo_bloques"]+=1
    return out.getvalue().strip()
def blocks(text):
    current=None; buf=[]; result=[]
    for lineno,line in enumerate(text.splitlines(),1):
        plain=re.sub(r"^(?:> ?)+","",line)
        if plain.startswith(chr(96)*3):
            if current is None:current=(plain[3:],lineno);buf=[]
            else:
                result.append((current[0],"\n".join(buf),current[1]))
                current=None
        elif current is not None:buf.append(plain)
    check(current is None,"Valla sin cierre")
    return result
def body(text):return text.split("---",2)[2].strip()
def static():
    files=[p for p in ROOT.rglob("*") if p.is_file() and not any(part.startswith(".") for part in p.relative_to(ROOT).parts)]
    names={p.stem for p in files}|{p.name for p in files}
    for p in files:
        if p.suffix not in [".md",".py",".ipynb",".txt",".json"]:continue
        data=p.read_bytes()
        check(not data.startswith(b"\xef\xbb\xbf"),f"BOM: {p.name}")
        check(b"\r" not in data,f"No LF: {p.name}")
        text=data.decode("utf-8")
        check(not any(l.rstrip()!=l for l in text.splitlines()),f"Espacios finales: {p.name}")
        if p.suffix!=".md":continue
        for marker in [chr(8249),chr(8250),"{"+'{title}}',"{"+'{date',"TO"+"DO"]:
            check(marker not in text,f"Marcador en {p.name}: {marker}")
        check("\n\n\n" not in text,f"Saltos duplicados: {p.name}")
        try:
            fm=yaml.safe_load(text.split("---",2)[1])
            required=["tipo","estado","dificultad","fecha","libreria","version","prerequisitos","reto","fuentes","tags","bloque","subtema","dia","orden","prioridad","nivel","tiempo_estimado","aliases"]
            check(all(k in fm for k in required),f"Campos YAML faltantes: {p.name}")
            check({"bloque-p","python","flashcards"}<=set(fm["tags"]),f"Tags: {p.name}")
            check(fm["estado"]=="borrador" and fm["bloque"]=="P",f"Estado/bloque: {p.name}")
        except Exception as exc:REPORT["errores"].append(f"YAML {p.name}: {exc}");continue
        prose=[];in_fence=False
        for line in text.splitlines():
            plain=re.sub(r"^(?:> ?)+","",line)
            if plain.startswith(chr(96)*3):in_fence=not in_fence;continue
            if not in_fence:prose.append(re.sub(chr(96)+r"[^"+chr(96)+r"]*"+chr(96),"",line))
        for dest in re.findall(r"\[\[([^\]]+)\]\]","\n".join(prose)):
            target=dest.split("|")[0].split("#")[0]
            check(target in names,f"Enlace inexistente en {p.name}: {target}")
            if not target.endswith(".png"):check("|" in dest,f"Enlace sin alias: {p.name}: {dest}")
        bs=blocks(text)
        for lang,code,line in bs:
            if lang=="mermaid":
                check("[[" not in code,f"Wikilink en Mermaid: {p.name}")
                check("classDef" in code and "fill:#" in code,f"Sin color Mermaid: {p.name}")
            if lang=="python":check(len(code.splitlines())<35,f"Bloque largo {p.name}:{line} ({len(code.splitlines())})")
        # Filas separadas por una línea en blanco: incluso dentro de callouts.
        stripped=[re.sub(r"^(?:> ?)+","",l) for l in text.splitlines()]
        for i in range(1,len(stripped)-1):
            if not stripped[i].strip() and stripped[i-1].startswith("|") and stripped[i+1].startswith("|"):
                check(False,f"Tabla interrumpida: {p.name}:{i+1}")
        if fm["tipo"]=="python":
            b=body(text);inside=False;count=0
            for l in b.splitlines():
                plain=re.sub(r"^(?:> ?)+","",l)
                if plain.startswith(chr(96)*3):inside=not inside
                elif not inside:count+=1
            REPORT["longitudes"][p.stem]=count
            check(count<=80,f"Nota larga: {p.name}: {count}")
    for d in range(1,6):
        check(sum(n.startswith(f"P{d}.") for n in REPORT["longitudes"])==3,f"No son tres conceptos en P{d}")
        p=next(ROOT.rglob(f"P{d}.E*.md"));text=p.read_text(encoding="utf-8")
        rows=re.findall(r"> \[!question\] (P\d\.E-\d+) · ([◆➕]) · (⭐+) · ([^·]+) · (\d+) min",text)
        core=sum(int(r[4]) for r in rows if r[1]=="◆");amp=sum(int(r[4]) for r in rows if r[1]=="➕")
        nc=sum(r[1]=="◆" for r in rows);na=sum(r[1]=="➕" for r in rows)
        tierra=sum(int(r[4]) for r in rows if r[1]=="◆" and r[3].strip()=="Reto Tierra")
        total=(30 if d==1 else 15)+75+core+10+(95 if d==5 else 0)
        total_amp=amp+(90 if d<5 else 180)
        check(216<=total<=264 and 216<=total_amp<=264,f"Tiempo diario fuera de rango P{d}")
        check(core==[125,140,140,140,45][d-1] and amp==(150 if d<5 else 60),f"Tiempo ejercicios P{d}")
        check(tierra/core>=(.15 if d==1 else .30),f"Retos Tierra insuficientes P{d}")
        fm=yaml.safe_load(text.split("---",2)[1]);check(fm["tiempo_nucleo"]==core and fm["tiempo_ampliacion"]==amp,f"Tiempo YAML P{d}")
        REPORT["tiempos"].append(dict(dia=d,ejercicios_nucleo=nc,ejercicios_ampliacion=na,min_ejercicios_nucleo=core,min_ejercicios_ampliacion=amp,nucleo=total,ampliacion=total_amp,plan=240,tierra_min=tierra))
    pngs=list(ROOT.glob("assets/*.png"))
    check(0<len(pngs)<=8,"Número de figuras")
    for p in pngs:
        size=p.stat().st_size
        check(size<150000,f"Figura supera 150 KB: {p.name}")
        REPORT["figuras"].append(dict(nombre=p.name,bytes=size))
    check(not list(ROOT.glob("*.png")),"PNG fuera de assets")
    # Registro de los temas introducidos, para la revisión humana del orden.
    REPORT["orden_pedagogico"]="Mapa explícito por nota; ejercicios tras las tres notas del día. Diagnóstico y soporte suministrado rotulados. Revisión manual complementaria."

def code_checks():
    with tempfile.TemporaryDirectory(dir=WORK,prefix="codigo-") as td:
        work=Path(td)/"assets";work.mkdir();old=Path.cwd();os.chdir(work);sys.path.insert(0,str(work))
        try:
            for i,c in enumerate(CONCEPTS):
                p=ROOT/FOLDERS[c["day"]-1]/(NOTE_NAMES[i]+".md")
                bs=blocks(p.read_text(encoding="utf-8"));ns={}
                for gen in GENERATORS:run(gen,ns)
                expect_output=None
                for lang,code,line in bs:
                    if lang=="python":
                        if code.strip() in [c["error"].strip()]+[bad for bad,_ in c.get("errors_extra",[])]:
                            try:run(code,dict(ns))
                            except Exception:pass
                            else:check(False,f"Error intencional no falló {p.name}")
                            expect_output=None
                        else:
                            try:expect_output=run(code,ns)
                            except Exception as exc:check(False,f"Código {p.name}:{line}: {type(exc).__name__}: {exc}");expect_output=None
                    elif lang=="text" and expect_output is not None:
                        check(code.strip()==expect_output or code.strip()=="(sin salida)" and expect_output=="",f"Salida no coincide {p.name}:{line}")
                        expect_output=None
                plt.close("all")
            for e in EXERCISES:
                ns={}
                for g in GENERATORS:run(g,ns)
                p=next(ROOT.rglob(f"P{e['day']}.E*.md"))
                text=p.read_text(encoding="utf-8")
                section=text.split(f"> [!question] {e['id']} ·",1)[1].split("> [!question]",1)[0]
                py=[b for lang,b,_ in blocks(section) if lang=="python"][:3]
                check(len(py)==3,f"Tres bloques de ejercicio {e['id']}")
                if len(py)!=3:continue
                check(py[1]==e["check"],f"Comprobación diferente {e['id']}")
                check(py[2]==((e["setup"]+"\n" if e["setup"] else "")+e["solution"]),f"Solución diferente {e['id']}")
                try:
                    run(py[0],ns);run(py[2],ns);run(py[1],ns)
                    REPORT["ejercicios"]+=1
                except Exception as exc:check(False,f"{e['id']}: {type(exc).__name__}: {exc}")
                plt.close("all")
            ns={}
            for g in GENERATORS:run(g,ns)
            for e in PROJECT:
                try:
                    run(e["solution"],ns);run(e["check"],ns);REPORT["ejercicios"]+=1
                except Exception as exc:check(False,f"{e['id']}: {type(exc).__name__}: {exc}");break
            plt.close("all")
            # Otros bloques Python: P.D y diagnóstico, con los datos embebidos.
            for name in ["P.D Datos sintéticos de práctica.md","P.0 Empezar aquí.md"]:
                ns={}
                for gen in GENERATORS:run(gen,ns)
                for lang,code,line in blocks((ROOT/name).read_text(encoding="utf-8")):
                    if lang=="python":
                        try:run(code,ns)
                        except Exception as exc:check(False,f"{name}:{line}: {exc}")
                plt.close("all")
            testpath=work/"test_conversion.py"
            if testpath.exists():
                r=subprocess.run([sys.executable,"-m","pytest",str(testpath),"-q","-p","no:cacheprovider"],capture_output=True,text=True)
                check(r.returncode==0,"pytest básico falló: "+r.stdout+r.stderr)
                REPORT["pytest"]=r.stdout.strip()
        finally:
            sys.path.remove(str(work));os.chdir(old);plt.close("all")

def notebooks():
    lookup={e["id"]:e for e in EXERCISES+PROJECT}
    for p in sorted((ROOT/"notebooks").glob("*.ipynb")):
        print("Ejecutando notebook",p.name,flush=True)
        nb=nbformat.read(p,as_version=4);nbformat.validate(nb)
        exercises=[c for c in nb.cells if c.metadata.get("role")=="respuesta"]
        checks=[c for c in nb.cells if c.metadata.get("role")=="comprobacion"]
        check(len(exercises)==len(checks),f"Cantidad de checks {p.name}")
        expected=PROJECT if p.name.startswith("PZ") else [e for e in EXERCISES if e["day"]==int(p.name[1])]
        check(len(exercises)==len(expected),f"Cantidad de ejercicios {p.name}")
        md=[c for c in nb.cells if c.cell_type=="markdown" and "exercise_id" in c.metadata]
        check(sum(c.metadata.minutes for c in md)==sum(e["minutes"] for e in expected),f"Minutos notebook {p.name}")
        solved=copy.deepcopy(nb)
        for c in solved.cells:
            role=c.metadata.get("role")
            if role=="respuesta":
                e=lookup[c.metadata["exercise_id"]]
                c.source=(e["setup"]+"\n" if e["setup"] else "")+e["solution"]
            elif role=="comprobacion":
                e=lookup[c.metadata["exercise_id"]];check(c.source==e["check"],f"Check notebook {e['id']}")
            elif role=="instalacion":
                c.metadata["tags"]=["skip-execution"]
        with tempfile.TemporaryDirectory(dir=WORK,prefix="notebook-") as td:
            kernel=KernelManager(kernel_name="python3")
            kernel.kernel_spec.argv=[sys.executable,"-m","ipykernel_launcher","-f","{connection_file}"]
            try:
                client=NotebookClient(solved,km=kernel,timeout=180,resources={"metadata":{"path":td}},allow_errors=False)
                client.execute()
                nbformat.validate(solved)
                # Copia temporal con soluciones y salidas, descartada al salir.
                nbformat.write(solved,Path(td)/p.name)
                errors=[o for c in solved.cells if c.cell_type=="code" for o in c.get("outputs",[]) if o.output_type=="error"]
                check(not errors,f"Salida error {p.name}")
                REPORT["notebooks"].append(dict(nombre=p.name,ejercicios=len(exercises),estado="válido y ejecutado con soluciones"))
            except Exception as exc:
                check(False,f"Notebook {p.name}: {exc}")
                REPORT["notebooks"].append(dict(nombre=p.name,estado="falló"))
            finally:
                if kernel.has_kernel:
                    kernel.shutdown_kernel(now=True)
        print("Notebook terminado",p.name,flush=True)

if __name__=="__main__":
    static()
    print("Estructura revisada; ejecutando código",flush=True)
    code_checks()
    print("Errores antes de notebooks:",REPORT["errores"],flush=True)
    notebooks()
    (ROOT/"assets"/"verificacion.json").write_text(json.dumps(REPORT,ensure_ascii=False,indent=2)+"\n",encoding="utf-8",newline="\n")
    print(json.dumps(REPORT,ensure_ascii=False,indent=2))
    sys.exit(bool(REPORT["errores"]))
