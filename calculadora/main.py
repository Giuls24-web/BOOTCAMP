def suma(a,b):
#Devuelve la suma de dos números
    return a+b

def resta(a,b):
    #Devuelve la resta de dos números
    return a-b

def multiplicacion(a,b):
    #Devuelve la multiplicacion de dos números
    return a*b

def division(a,b):
    #Devuelve la division de dos números. Manejo división /0
    try:
     return a/b
    except ZeroDivisionError:
     return "No se puede dividir para cero"
    
    
def radicacion(a,b):
    #Devuelve la division de dos números. Manejo división /0
    try:
     return a**(1/b)
    except ZeroDivisionError:
     return "El indice de la raíz no puede ser cero"
    
def potenciacion(a,b):
    #Devuelve la potencia dado un exponente
     return a**b

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
