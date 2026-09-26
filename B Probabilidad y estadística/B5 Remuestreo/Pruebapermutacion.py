import numpy as np
import matplotlib.pyplot as plt
#Grupos observados
grupo_A = np.array([10, 11, 12, 13, 14])
grupo_B = np.array([20, 21, 22, 23, 24])

#Media observada
observada = np.mean(grupo_B) - np.mean(grupo_A)

#Concatenamos los datos de ambos grupos
todos = np.concatenate([grupo_A, grupo_B])

#Generador
rng = np.random.default_rng(42)
permutaciones = []

#Permutaciones
for _ in range(10000):

    mezclados = rng.permutation(todos)

    #Formamos las permutaciones
    A_perm = mezclados[:len(grupo_A)]
    B_perm = mezclados[len(grupo_A):]

    diferencia = np.mean(B_perm) - np.mean(A_perm)
    permutaciones.append(diferencia)


permutaciones = np.array(permutaciones)

p_valor = np.mean(np.abs(permutaciones) >= abs(observada))

print("Diferencia observada:", observada)
print("p-valor", p_valor)

# 1. Dibujamos el histograma de las permutaciones (Distribución bajo el azar)
# Recogemos los datos de los contenedores (bins) para poder iluminar las colas después
n_counts, bins, patches = plt.hist(permutaciones, bins=30, edgecolor='black', alpha=0.6, 
                                   label='Diferencias bajo Hipótesis Nula (Azar)', color='gray')

# 2. Iluminamos de color rojo las zonas que representan el p-valor (valores más extremos)
for i in range(len(patches)):
    # Si el centro del contenedor es más extremo (positivo o negativo) que la observada
    bin_center = (bins[i] + bins[i+1]) / 2
    if abs(bin_center) >= abs(observada):
        patches[i].set_facecolor('red')
        patches[i].set_alpha(0.8)

# 3. Dibujamos las líneas de la diferencia observada real (e inversa para dos colas)
plt.axvline(observada, color='darkred', linestyle='--', linewidth=2, 
            label= f'Diferencia Observada Real ({observada:.1f})')
plt.axvline(-observada, color='darkred', linestyle='--', linewidth=2, 
            label= f'Límite Extremo Opuesto ({-observada:.1f})')

# Personalización matemática y etiquetas
plt.title(f'Prueba de Permutación\nDistribución de Diferencias (p-valor = {p_valor:.4f})', fontsize=14)
plt.xlabel('Diferencia de Medias (Grupo B - Grupo A)', fontsize=12)
plt.ylabel('Frecuencia (Cantidad de veces)', fontsize=12)
plt.grid(axis='y', alpha=0.3)
plt.legend(loc='upper right')

plt.tight_layout()
plt.show()