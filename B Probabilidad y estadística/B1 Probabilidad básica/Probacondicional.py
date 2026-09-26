import random

N = 10000

casos_par = 0
casos_mayor3_y_par = 0

for _ in range(N):
    dado = random.randint(1, 6)

    if dado % 2 == 0:
        casos_par += 1

        if dado > 3:
            casos_mayor3_y_par += 1

probabilidad_condicional = casos_mayor3_y_par / casos_par

print(probabilidad_condicional)