# try : 
#      numero=int(input("Ingrese número: "))
# except ValueError as e: 
#      print(f"Error: {e} Introduce un número válido: ")
# else:
#       print(f"El número es {numero}")  
# finally: 
#      print("Fin del programa")  

# numero=int(input("Ingrese número: "))
# print(f"El número es {numero}")  

# class MiError(Exception):
#     def __init__(self, mensaje):
#         self.mensaje=mensaje
#         super().__init__(self.mensaje)

# try:
#     raise MiError("Mi mensaje de error")
# except MiError as e:
#     print(f"Error: {e}")

# try: 
#     num= int(input("Ingrese un número: "))
#     resultado=10/num
#     print(f"El resultado es {resultado}")
# except ValueError:
#     print("Debes introducir ubn número: ")
# except ZeroDivisionError:
#     print("No se puede dividir entre o")

try: 
 num= int(input("Ingrese un número: "))
except ValueError:
 print("Error! Debes introducir un número: ")
else :
 print(f"El número es: {num}")
finally: 
 print("Adiós")