import numpy as np

valores = np.array([1, 2, 3, 4, 5, 6])

probabilidades = np.array([1/6]*6)
#O lo que es lo mismo
#proabilidades = np.array([1/6, 1/6, 1/6, 1/6, 1/6, 1/6])

#esto hace 1*1/6 + 2*1/6 + 3*1/6 + 4*1/6 + 5*1/6 + 6*1/6
esperanza = np.sum(valores * probabilidades)

print("Esperanza:", esperanza)