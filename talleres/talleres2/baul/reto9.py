competidor = {}
num_competidores = int(input("cantidad de competidores: "))

for i in range(num_competidores):
    nombre = input("Nombre del competidor {}: ".format(i+1))
    competidor[nombre] = None

for nombre in competidor:
    tiempo = float(input("Registre el tiempo {}: ".format(nombre)))
    competidor[nombre] = tiempo

print("Tiempos registrados:")
for nombre, tiempo in competidor.items():
    print("{}: {}".format(nombre, tiempo))

ganador = min(competidor, key=competidor.get)
print("El ganador es: {} con un tiempo de {} ".format(ganador, competidor[ganador]))