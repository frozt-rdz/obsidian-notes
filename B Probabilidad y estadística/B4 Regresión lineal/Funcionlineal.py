import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# Datos observados
years = np.array([2010, 2015, 2020])
sea_level = np.array([20, 35, 50])

# Ajuste de regresión lineal
res = linregress(years, sea_level)

#Grafico
plt.figure(figsize=(8,5))

#Puntos
plt.scatter(
    years, sea_level, color="navy", s=60, label="Observaciones (Nivel del mar)", zorder=5
)

#Linea ajustada
plt.plot(years, res.intercept + res.slope * years, color="crimson", linestyle="--", linewidth=2, label=f"Tendencia ({res.slope:.1f} mm/año)", )

#Formato profesional
plt.title( "Tendencia del Nivel del Mar (2010 - 2020)", fontsize=12, fontweight="bold" )
plt.xlabel("Año", fontsize=10) 
plt.ylabel("Nivel del Mar (mm)", fontsize=10) 
plt.grid(True, linestyle=":", alpha=0.6) 
plt.legend()

#Guardar
plt.savefig("sea_level_trend.png", dpi=300, bbox_inches="tight") 
plt.close()

#Imprimir resultados
print(f"Pendiente (b):{res.slope:.2f} mm/año")
print(f"Intercepto (a):{res.intercept:.2f}")
print(f"R-cuadrado (R²):{res.rvalue**2:.4f}")
print(f"p-valor: {res.pvalue:.4f}") 
print(f"Error estándar de la pendiente: {res.stderr:.4f}")