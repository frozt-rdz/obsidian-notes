"""Regenera las seis figuras originales dentro de assets."""
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
            codigo="\n".join(l for l in etapa["solution"].splitlines() if "resultados_simulados.csv" not in l)
            exec(codigo,ns)
    exec(figura["code"],ns)
    ns["fig"].savefig(ROOT/figura["name"],dpi=100,bbox_inches="tight")
    plt.close("all")
    print(figura["name"],(ROOT/figura["name"]).stat().st_size)
