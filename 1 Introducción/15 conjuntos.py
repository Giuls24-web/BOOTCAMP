lenguajes={"python", "c++", "go", "java","java","javascript"}
print(type(lenguajes))

print(lenguajes)

#no funciona: print(lenguajes[0])
print(lenguajes.add("php"))
print(lenguajes)

#print(lenguajes.clear())
#print(lenguajes)

lenguajes2=lenguajes.copy()
print(lenguajes2)

lenguajes2.pop() #eliminar el primer dato del conjunto
print(lenguajes2)
print(lenguajes)
lenguajes2.pop() 
print(lenguajes2)

print(lenguajes2.intersection(lenguajes2))