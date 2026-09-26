from scipy.stats import wilcoxon

antes = [10, 10, 10, 10, 10]
despues = [12, 12, 12, 13, 15]

resultado = wilcoxon(antes, despues)

print(resultado)