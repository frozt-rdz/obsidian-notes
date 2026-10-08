"""Revisión de archivos creados en esta tarea; no toca materiales previos."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"assets"))
import generar_bloque as g
owned={p.resolve() for p in ROOT.rglob("*") if p.is_file() and not any(part.startswith(".") for part in p.relative_to(ROOT).parts)}
def revise(rel,text):
    p=(ROOT/rel).resolve()
    assert p.is_relative_to(ROOT.resolve()),"Fuera del bloque"
    assert not p.exists() or p in owned,"No se sobrescribe contenido previo"
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(g.normalize(text),encoding="utf-8",newline="\n")
g.write=revise
g.bibliography();g.concepts();g.exercises();g.data_note();g.project_note();g.indices();g.start();g.supporting()
print("Revisión completa de entregables propios")
