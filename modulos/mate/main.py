from operaciones import suma as s
from operaciones import resta as r
from operaciones import multiplicacion as m
from operaciones import division as d

num1= int(input("Ingresa un número: "))
num2= int(input("Ingresa un número: "))

print(f"La suma de {num1} + {num2} es: {s(num1,num2)}")
print(f"La suma de {num1} - {num2} es: {r(num1,num2)}")
print(f"La suma de {num1} x {num2} es: {m(num1,num2)}")
print(f"La suma de {num1} / {num2} es: {d(num1,num2)}")