class Animaux:
    def __init__(self,nombre):
        self.nombre=nombre

    def hablar(self):
        pass

class Perro(Animaux):
    def hablar(self):
        print(f"{self.nombre} puede ladrar")

class Gato(Animaux):
    def hablar(self):
        print(f"{self.nombre} puede maullar")

animal1=Perro("firulais")
animal2=Gato("Garfield")

animal1.hablar()
animal2.hablar()