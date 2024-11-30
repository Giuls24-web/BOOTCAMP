"""class CuentaBancaria:
    def __init__(self, nombre, saldo):
        self.nombre=nombre
        self._saldo=saldo

    def depositar (self, cantidad):
        self._saldo +=cantidad

    def retirar(self, cantidad):
        self._saldo -=cantidad
    
    def __str__(self):
        return (f"Cuenta bancaria de {self.nombre} con saldo {self._saldo}")
    
cuenta1=CuentaBancaria("Diego Saavedra",10)
cuenta1=CuentaBancaria.depositar(20)
cuenta1=CuentaBancaria.retirar(10)

print(cuenta1.saldo)"""

class Computer:
    def __init__(self):
        self.__maxprice=900
    def sell(self):
        print(f"El precio de venta es: {self.__maxprice}")

    def set_maxprice(self,price):
        self.__maxprice=price
computer1=Computer()
computer1.sell()
#modificado
computer1.__maxprice=1000
computer1.sell()

computer1.set_maxprice(1000)
computer1.sell()
