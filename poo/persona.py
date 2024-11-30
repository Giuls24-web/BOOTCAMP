class Persona:

 def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad
 def saludar (self):
    return (f"Hola, mi nombre es {self.nombre} y tengo {self.edad}")
 
persona1=Persona("Diego",36)
print(persona1.nombre)
print (persona1.edad)
print (persona1.saludar())

persona2=Persona("María",45)
print(persona2.nombre)
print (persona2.edad)
print (persona2.saludar())