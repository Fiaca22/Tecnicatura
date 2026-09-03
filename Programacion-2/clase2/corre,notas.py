# tengo que darle 5 puntos a todas las notas en un lista menos a los que tengan 96 o mas

notas = [90, 85, 96, 88, 92, 97, 89]
for i in range(len(notas)):
    if notas[i] < 96:
        notas[i] += 5
print(notas)
