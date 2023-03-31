class Persona:
    tipoDoc=""
    documento=""
    nombre=""
    apellido=""
    peso=""
    estatura=""
    edad=0
    sexo=""
    
    def __init__(self,tipoDoc, documento, nombre, apellido, peso, estatura, edad, sexo):
        self.tipoDoc=tipoDoc
        self.documento=documento
        self.nombre=nombre
        self.apellido=apellido
        self.peso=peso
        self.estatura=estatura
        self.edad=edad
        self.sexo=sexo
    
    def registrarPersona(self):
        self.tipoDoc=input("ingrese el tipo de documento: ")
        self.documento=int(input("ingrese el numero de documento: "))
        self.nombre= input("ingrese el nombre: ")
        self.apellido= input("ingrese el apellido: ")
        self.peso=int (input("ingrese su peso: "))
        self.estatura=int(input("ingrese su estatura: "))
        self.edad=int (input("ingrese su edad: "))
        self.sexo= input("ingrese su genero: ")
        
    def mostrarPersona(self):
        print(f"\nlos datos ingresados son:\nTipo de documento {self.documento} \nNombre {self.nombre} \nApellido {self.apellido} \nPeso{self.peso} \nEstatura{self.estatura} \nEdad {self.edad} \nSexo {self.sexo} ")
    
    def calcularLmc(self):
        pesoActual=self.peso/(self.estatura*self.estatura)
        if pesoActual < 20 :
            print("El peso esta por debajo de lo normal")
        elif pesoActual >=20 and pesoActual <=25:
            print ("El peso es el optimo") 
        else:
            print("Esta en sobrepeso")
        return pesoActual
    
    def mayorEdad(self):
        if self.edad >= 18:
            print("Es mayor de edad")
        else:
            print("Es menor de edad")