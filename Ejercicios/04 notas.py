"""
Crear una función que puda al usuario 2 notas y devuelva la mayor de ellas
"""
print("Nota 1: ")
Nota1=int(input())
print("Nota 2: ")
Nota2=int(input())
def mayor(nota1,nota2):
    if(nota1>nota2):
        return nota1
    else:
        return nota2

notaMayor=mayor(Nota1,Nota2)
print(" La nota más alta es: ",notaMayor)
