from scipy.stats import norm

# Puntaje z para un nivel de confianza del 95%
z = 1.96

cola_derecha = 1 - norm.cdf(z)

# Prueba de dos colas
p_value = 2 * cola_derecha

print(f"Cola derecha: {cola_derecha:.3f}")
print(f"p-value: {p_value:.3f}")


for z in [1, 1.5, 1.96, 2, 2.58, 3]:
    p = 2* (1-norm.cdf(z))
    print(f"Z = {z:.2f}, p = {p:.5f}")