"""
Temperatura ingresada por el usuario de Farenheit a Celcius o de Celsius a Farenheit
dependiendo de la escala proporcionada
"""
print ("Conversión")
print ("Elija una opción:")
print ("1. C° a F°")
print ("2. F° a C°")
Opcion=int(input())
print ("Escriba la Temperatura: ")
Temperatura=int(input())

if Opcion==1:
    operacion=(Temperatura * 9/5) + 32
    print("La temperatura en F° es: ",operacion)
else:
    operacion=(Temperatura - 32) * 5/9
    print("La temperatura en C° es: ",operacion)



