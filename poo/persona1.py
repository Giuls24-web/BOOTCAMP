#atributos nombre edad, profesión, metodos: saludar y despedirse, crear 2 
# instancias de las clases y mostrar el nombre y el método
class Persona1:

 def __init__(self, nombre, edad,profesion):
    self.nombre = nombre
    self.edad = edad
    self.profesion=profesion
 def saludar (self):
    return (f"Hola, mi nombre es {self.nombre}, tengo {self.edad} y soy {self.profesion}")
 def despedirse(self):
    return (f"Adiós")
 
persona=Persona1("Diego",36, "profesor")
print(persona.nombre)
print (persona.saludar())
print (persona.despedirse())
