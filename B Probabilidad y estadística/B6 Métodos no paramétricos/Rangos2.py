from scipy.stats import rankdata

datos = [15, 12, 18, 12, 20]

rangos = rankdata(datos)

for dato, rango in zip(datos, rangos):
    print(f"{dato} → rango {rango}")