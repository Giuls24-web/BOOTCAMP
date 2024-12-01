from functools import reduce
#uso de lambda y map
numeros= [1,2,3,4,5]
dobles=list(map(lambda x: x*2, numeros))
print(dobles)

#Uso de filer
pares= list(filter(lambda x: x%2==0,numeros))
print(pares)

impares= list(filter(lambda x: x%2==1,numeros))
print(impares)

#uso de reduce
suma= reduce(lambda x,y:x+y,numeros)
print(suma)
