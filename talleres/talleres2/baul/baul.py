baul = [] 

while True:
    opcion = int(input("Que desea realizar:\n 1. Agregar un articulo al baul \n 2. Ver los articulos en el baul \n 3. Borrar el ultimo articulo \n4. Borrar un articulo del baul \n5. Salir \n "))

    if opcion == 1:
        articulo = input("Nombre del articulo: ")
        baul.append(articulo)
        print("El articulo", articulo, "se ha agregado al baul")

    elif opcion == 2:
        if len(baul) == 0:
            print("El baul no tiene nada!")
        else:
            for i in range(len(baul)):
                print("articulo en el baul",i+1, baul[i],)

    elif opcion == 3:
        if len(baul) == 0:
            print("El baul no tiene nada! \n")
        else:
            ultimoArticulo = baul.pop()
            print("El articulo", ultimoArticulo, "se ha eliminado del baul ")

    elif opcion == 4:
        if len(baul) == 0:
            print("El baul no tiene nada ! ")
        else:
            print("Articulos en el baul:  ")
            for i in range(len(baul)):
                print(i+1, ".", baul[i])
            borrar = int(input("numero del articulo a borrar: "))
            if borrar > 0 and borrar <= len(baul):
                articuloEliminado = baul.pop(borrar-1)
                print("El articulo", articuloEliminado, "ha sido eliminado del baul ")
            else:
                print("numero invalido ")

    elif opcion == 5:
        print("Saliendo...")
        break

    else:
        print("opcion invalida")