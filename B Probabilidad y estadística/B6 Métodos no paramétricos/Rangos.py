from scipy.stats import rankdata

datos = [12, 5, 20, 8]

# Calcular los rangos
rangos = rankdata(datos)

print(rangos)

datos_empate = [5, 8, 8, 12]

rangos_empate = rankdata(datos_empate)

print(rangos_empate)
