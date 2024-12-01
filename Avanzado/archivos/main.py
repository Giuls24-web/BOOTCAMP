# #Escritura del archivo
# with open ('archivo.txt', 'w') as f:
#     f.write("Hola mundo developers !\n")

# #Lectura del archivo
# with open ('archivo.txt', 'r') as f:
#     contenido=f.read()
#     print(contenido)

# with open ('Avanzado\archivos\Moreta.png', 'r') as file:
#     datos =file.read()

# #with open ('saludo.txt', 'w') as file:
#   file.write("Hola mundo")
# with open ('saludo.txt', 'r') as file:
#   for line in file:
#     print(line.strip())

txt=str(input("Ingrese texto: "))
with open ('entrada.txt', 'w') as file:
 file.write(txt)
with open ('entrada.txt', 'r') as file:
 contenido=file.read()
 print(contenido)