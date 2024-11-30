class Animal:
    def __init__(self, nombre, edad, especie):
        self.nombre=nombre
        self.edad=edad
        self.especie=especie

    def comer (self):
        return(f"El animal {self.nombre} tiene aproximadamente {self.edad} y es de la especir {self.especie} está comiendo")

    def __del__(self):
        print (f"El animal {self.nombre} ha sido eliminado")

gato=Animal("Pepito","2","gato") 
print(gato.comer())  

perro=Animal("Juanita","1","perro") 
print(perro.comer()) 