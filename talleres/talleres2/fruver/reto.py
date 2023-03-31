instructores = {}

while True:
    
    opcion = input("Que desea hacer:  \n 1 Agregar/modificar instructor \n 2 Buscar instructor \n 3 Borrar instructor \n 4 Listar instructores \n 5 Salir")

    if opcion == "1":
        nombre = input("Digite el nombre del instructor: ")
        if nombre in instructores:
            print("El instructor", nombre, "ya se encuentra registrado")
            print("Materia ", {instructores[nombre][materia]})
            telefono = input("Ingrese otro numero de celular o  presione enter para dejarlo igual")
            if telefono != "":
                instructores[nombre][telefono] = telefono
        else:
            materia = input("Ingrese la materia que ejerce: ")
            telefono = input("Ingrese el número de contacto: ")
            instructores[nombre] = {materia: materia, telefono: telefono}
            print("El instructor",nombre, "se ha registrado")

    elif opcion == "2":
        busqueda = input("Ingrese el nombre del instructor: ")
        resultados = []
        for nombre, datos in instructores.items():
            if nombre.startswith(busqueda):
                resultados.append(nombre)
        print("Resultados  ")
        for nombre in resultados:
            print("Nombre", nombre, "Materia" ,instructores[nombre][materia], "Telefono",instructores[nombre][telefono])

    elif opcion == "3":
        nombre = input("Ingrese el nombre del instructor que desea eliminar ")
        if nombre in instructores:
            confirmacion = input("Está seguro de borrar al instructor",nombre, "(si/no)")
            if confirmacion.lower() == "si" or "Si" or "SI":
                del instructores[nombre]
                print("El instructor" ,nombre, "ha sido borrado")
        else:
            print("No se encontró al instructor", nombre, "en la agenda")

    elif opcion == "4":
        print("Instructores ya registrados: ")
        for nombre, datos in instructores.items():
            print("Nombre", nombre, "Materia" ,instructores[nombre][materia], "Telefono",instructores[nombre][telefono])

    elif opcion == "5":
        print("Gracias por usar nuestros servicios")
        break

    else:
        print("Opcion invalida")