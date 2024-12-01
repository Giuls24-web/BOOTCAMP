# #comprensión de lista
# cuadrado = [x**2 for x in range(5)]
# print(cuadrado)

#Generadores
# def contador():
#     for i in range (5):
#         yield i**2

# gen=contador()
# for valor in gen:
#     print(valor)

# Lista de palabras
palabras = ["python", "django", "flask", "javascript"]

# Comprensión de lista para obtener las longitudes de las palabras
longitudes = [len(palabra) for palabra in palabras]
print(f"Longitudes de las palabras: {longitudes}")

# Comprensión de diccionario para contar las frecuencias de las letras
frecuencia = {letra: palabras[0].count(letra) for letra in palabras[0]}
print(f"Frecuencia de letras en la primera palabra: {frecuencia}")

# Generador para números pares
def generador_pares():
    for i in range(0, 20, 2):
        yield i

# Mostrar los números generados
for numero in generador_pares():
    print(numero)

