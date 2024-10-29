lenguajes=["python", "c++", "go", "java","javascript"]
#print(type(lenguajes))
print(lenguajes[0])
print(lenguajes[1])
lenguajes[1]="ruby"
print(lenguajes[1])
print(lenguajes)

print(lenguajes[1:4])
print(lenguajes[:3])
print(lenguajes[2:])
print(lenguajes[-1])
lenguajes2=["python", "c++",2, ["a","b","c"], "go", "java","javascript"]
print(lenguajes2[3])

#invertido
print(lenguajes[-3])
print(lenguajes[2])
lenguajes.insert(3,"dart")
print(lenguajes)
lenguajes.remove("dart")
print(lenguajes)
print("go" in lenguajes)
print(len(lenguajes))