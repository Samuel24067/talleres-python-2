Fruver = {}

while True:
    
    opcion = input("Elija una opcion: \n 1. Agregar/modificar \n 2. Buscar \n 3. Borrar \n 4. Listar \n 5. Salir \n ")
    
    if opcion == "1":
        nombre = input("seleccione una fruta: ")
        precio = float(input("Digite el precio de la fruta: "))
        if nombre in Fruver:
            print("La fruta", nombre, " ya esta registrada",Fruver[nombre])
        else:
            Fruver[nombre] = precio
            print("La fruta ", nombre ," se encuentra con un predio de:  ", precio)
            
    elif opcion == "2":
        busqueda = input("buscar: ")
        resultados = [nombre for nombre in Fruver if nombre.startswith(busqueda)]
        if resultados:
            print("Resultados de busqueda: ",busqueda )
            for nombre in resultados:
                print(nombre, Fruver[nombre])
        else:
            print("No se encontraron resultados que comiencen con", busqueda)
            
    elif opcion == "3":
        nombre = input("Ingrese el nombre de la fruta que se eliminara: ")
        if nombre in Fruver:
            confirmacion = input ("seguro que desea borrar ", nombre , "(si/no)" )
            if confirmacion.lower() == "si" or "Si" or "SI" :
                del Fruver[nombre]
                print("La fruta",nombre, "se ha borrado")
            else:
                print("No se ha borrado la fruta",nombre)
        else:
            print("La fruta ", nombre ,"no se encuentra ")
            
    elif opcion == "4":
        if Fruver:
            print("Listado de frutas:")
            for nombre, precio in Fruver.items():
                print(nombre , precio)
        else:
            print("No hay frutas ")
            
    elif opcion == "5":
        print("saliendo...")
        break
        
    else:
        print("Opción no válida")