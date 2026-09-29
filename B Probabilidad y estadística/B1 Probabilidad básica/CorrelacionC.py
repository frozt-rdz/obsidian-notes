import numpy as np

horas = np.array([1, 2, 3, 4, 5])
calificaciones = np.array([60, 65, 72, 80, 88])

correlacion  = np.corrcoef(horas, calificaciones)[0, 1]
print("Correlación:", correlacion)