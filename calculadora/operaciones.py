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
     resultado= a/b
    except ZeroDivisionError:
     print ("operacion de división intentada")
     return "No se puede dividir para cero"
    else:
       return resultado
    finally:
       pass
    
def radicacion(a,b):
    #Devuelve la division de dos números. Manejo división /0
    try:
     return a**(1/b)
    except ZeroDivisionError:
     return "El indice de la raíz no puede ser cero"
    
def potenciacion(a,b):
    #Devuelve la potencia dado un exponente
     return a**b
