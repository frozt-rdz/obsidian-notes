import numpy as np
import matplotlib.pyplot as plt

x = np.arange(2015, 2021)

y = np.array([
    0.42,
    0.43,
    0.41,
    0.45,
    0.47,
    0.48
])

pendiente_observada = np.polyfit(x, y, 1)[0]

rng = np.random.default_rng(42)

pendientes_perm = []

for _ in range(10000):

    y_perm = rng.permutation(y)

    pendiente = np.polyfit(x, y_perm, 1)[0]

    pendientes_perm.append(pendiente)

pendientes_perm = np.array(pendientes_perm)

p_valor = np.mean(
    np.abs(pendientes_perm) >= abs(pendiente_observada)
)

print("Pendiente observada:", pendiente_observada)
print("p-valor:", p_valor)

plt.hist(pendientes_perm, bins=40)

plt.axvline(
    pendiente_observada,
    linestyle="--",
    linewidth=2
)

plt.xlabel("Pendiente")
plt.ylabel("Frecuencia")
plt.title("Prueba de permutación de la tendencia")

plt.show()