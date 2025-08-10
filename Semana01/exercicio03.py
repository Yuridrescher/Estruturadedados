numeros = []

for i in range(5):
    numeros.append(int(input("Digite um número: ")))

for n in set(numeros):
    print(f"O número {n} aparece {numeros.count(n)} vezes.")
