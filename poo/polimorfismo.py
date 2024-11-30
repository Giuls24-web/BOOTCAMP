class Deporte:
    def jugar(self):
        pass
class Futbol(Deporte):
    def jugar(self):
        print(f"Jugando Futbol")
class Basket(Deporte):
    def jugar(self):
        print(f"Jugando Basket")
class Tennis(Deporte):
    def jugar(self):
        print(f"Jugando Teniss")

deporte1=Futbol()
deporte1.jugar()

deporte2=Basket()
deporte2.jugar()

deporte3=Tennis()
deporte3.jugar()
