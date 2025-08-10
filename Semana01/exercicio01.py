numeros= []

for i in range(5):
    n= int(input("Digite um número:"))
    numeros.append(n)
if 0 in numeros:
    numeros.remove(0)
    numeros.append(0)


print("numeros:", numeros)
