notas = []
materia = int(input("cuantas notas se evaluaran: "))

for i in range(materia):
    nota = int(input("Ingrese la nota:  "))
    while nota < 1 or nota > 5:
        nota = int(input("Ingrese una nota válida entre 1 y 5 para mostar el promedio"))
    notas.append(nota)

promedio = sum(notas) / materia

if promedio < 3:
    print("Nota final:",promedio, "reprobaste")
    
elif promedio >= 3 and promedio < 4:
    print("Pasaste ",promedio)

else:
    print("pasaste por encima del promedio",promedio)