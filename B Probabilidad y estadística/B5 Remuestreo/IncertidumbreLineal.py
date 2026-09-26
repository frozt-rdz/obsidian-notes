import numpy as np
#Datos
x = np.array([2019, 2020, 2021, 2022, 2023])
y = np.array([20.1, 20.4, 20.5, 20.8, 21.0])

#Generador
rng = np.random.default_rng(42)

pendientes = []

for _ in range(10000):
    indices = rng.choice(len(x), size=len(x), replace=True)
    x_boot = x[indices]
    y_boot = y[indices]

    #El tercer 1 para una linea recta, 
    #Ajustamos los datos a una funcion polinomica
    #Guardamos la pendiente m con [0]
    pendiente = np.polyfit(x_boot, y_boot, 1)[0]
    pendientes.append(pendiente)


pendientes = np.array(pendientes)

ic=np.percentile(pendientes, [2.5, 97.5])
print("Pendiente original:", np.polyfit(x,y,1)[0])
print("IC 95%:", ic)
