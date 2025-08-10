numeros = []
numerosprimos = []


for i in range(5):
    n = int(input("Digite um número: "))
    numeros.append(n)

    if n > 1:  
        for divisor in range(2, n):
            if n % divisor == 0:
                break
        else:
            numerosprimos.append(n)
        
print("Lista de números:", numeros)
print("Lista de números primos:", numerosprimos)
