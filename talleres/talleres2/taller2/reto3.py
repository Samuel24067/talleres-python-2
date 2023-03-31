class Persona:
    def __init__(self):
        self._tipoDoc = ""
        self._documento = ""
        self._nombre = ""
        self._apellido = ""
        self._peso = 0.0
        self._estatura = 0.0
        self._edad = 0
        self._sexo = ""

    def get_tipoDoc(self):
        return self._tipoDoc

    def set_tipoDoc(self, tipoDoc):
        self._tipoDoc = tipoDoc
    
    def get_documento(self):
        return self._documento

    def set_documento(self, documento):
        self._documento = documento
        
    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre
        
    def get_apellido(self):
        return self._apellido

    def set_apellido(self, apellido):
        self._apellido = apellido
        
    def get_peso(self):
        return self._peso

    def set_peso(self, peso):
        self._peso = peso
        
    def get_estatura(self):
        return self._estatura

    def set_estatura(self, estatura):
        self._estatura = estatura
        
    def get_edad(self):
        return self._edad

    def set_edad(self, edad):
        self._edad = edad
        
    def get_sexo(self):
        return self._sexo

    def set_sexo(self, sexo):
        self._sexo = sexo  

    def pedirDatos(self):
        self.set_tipoDoc(input(" Tipo de documento: "))
        self.set_documento(input("Número de documento: "))
        self.set_nombre(input(" Nombre de la persona: "))
        self.set_apellido(input(" Apellido de la persona: "))
        self.set_peso(float(input(" dgite el peso de la persona en kilogramos: ")))
        self.set_estatura(float(input("Digite la estatura de la persona en metros: ")))
        self.set_edad(int(input("Digite la edad de la persona: ")))
        self.set_sexo(input("cual es el sexo de la persona (M/F): ").upper())

    def mostrarPersona(self):
        print("Tipo de documento:", self.get_tipoDoc(), "\n"
              "Número de documento:", self.get_documento(), "\n"
              "Nombre:", self.get_nombre(), "\n"
              "Apellido:", self.get_apellido(), "\n"
              "Peso:", self.get_peso(), "\n"
              "Estatura:", self.get_estatura(), "\n"
              "Edad:", self.get_edad(), "\n"
              "Sexo:", self.get_sexo(), "\n")
        
    def calcularImc(self):
        pesoActual = self.get_peso() / (self.get_estatura() ** 2)
        if pesoActual < 20:
            print("el peso de la persona está por debajo ")
        elif pesoActual >= 20 and pesoActual <= 25:
            print("El peso es el optimo")
        else:
            print("Esta en sobrepeso")

    def mayorEdad(self):
        if self.get_edad() >= 18:
            print("Es mayor de edad")
        else:
            print("Es menor de edad")