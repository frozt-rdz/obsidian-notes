import random

N=10000
favorables = 0

for _ in range(N):
    dado = random.randint(1, 6)

    if dado > 4:
        favorables += 1

probabilidad = favorables / N

print("Probabilidad experimental:", probabilidad)