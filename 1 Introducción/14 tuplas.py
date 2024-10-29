lenguajes=("python", "c++", "go", "java","javascript")
#lenguajes=("python", "c++",5,(1,2,3), "go", "java","javascript")
print(type(lenguajes))

print(lenguajes[1])
print(lenguajes[1:])
print(lenguajes[-1])
print(lenguajes[:])

#no funciona en tuplas: lenguajes.insert("ruby")
#no funciona en tuplas: lenguajes.remove("go")
print("go" in lenguajes)
print(len(lenguajes))