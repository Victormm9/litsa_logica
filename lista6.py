# 2- Utilizando vetores, crie um programa que organize uma 
# quantidade qualquer de números inteiros fornecidos pelo usuário da seguinte forma: primeiro os números pares em 
# ordem crescente e depois os números ímpares em ordem decrescente. 

pares = []
ímpares = []


while True:
    num = int(input("Digite numeros: \n(Ao digitar 0, fehca o programa!)"))
    if num == 0:
     break
    if num % 2 == 0:
        pares.append(num)
    else:
     ímpares.append(num)

pares.sort()
ímpares.sort(reverse=True)
print(f"Seus numeros são {pares} e {ímpares}")
