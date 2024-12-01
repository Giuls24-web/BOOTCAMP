from operaciones import suma, resta, multiplicacion, division, radicacion, potenciacion
#Punto de Entrada
if __name__ =='__main__':
   print("Bienvenido a la calculadora básica")
   num1 = float(input("Ingresar el primer número: "))
   num2 = float(input("Ingresar el segundo número: "))

   print (f"Suma: {suma(num1,num2)}")
   print (f"Resta: {resta(num1,num2)}")
   print (f"Multiplicacion: {multiplicacion(num1,num2)}")
   print (f"Division: {division(num1,num2)}")
   print (f"Radicación: {radicacion(num1,num2)}")
   print (f"Potenciación: {potenciacion(num1,num2)}")
