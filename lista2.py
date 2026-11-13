# 2- Faça um programa em Py que leia um vetor de seis elementos numéricos 
# inteiros, calcule e mostre: 
# a) A quantidade de números pares 
# b) Quais os números pares 
# c) A quantidade de números ímpares 
# d) Quais os números ímpares

numeros = []
for i in range(6):
    num = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(num)

pares = []
impares = []

for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(f"a) A quantidade de números pares é: {len(pares)}")
print(f"b) Os números pares são: {pares}")
print(f"c) A quantidade de números ímpares é: {len(impares)}")
print(f"d) Os números ímpares são: {impares}")
