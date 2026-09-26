from scipy.stats import wilcoxon

antes = [10, 12, 11, 15, 13]
despues = [12, 14, 13, 16, 15]

estadistico, p = wilcoxon(antes, despues)

print("Estadístico:", estadistico)
print("p-value:", p)