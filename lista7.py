# 3- Faça um programa que leia e monte dois vetores de números inteiros com 20 
# números cada. Depois de montados, gere um terceiro vetor formado pela 
# diferença dos dois vetores lidos, um quarto vetor formado pela soma dos dois 
# vetores lidos e por último um quinto vetor formado pela multiplicação dos dois
# vetores lidos.

numeros1 = []
numeros2 = []
for i in range(20):
    num1 = int(input(f"Digite o {i+1}º número do primeiro vetor: "))
    numeros1.append(num1)
    num2 = int(input(f"Digite o {i+1}º número do segundo vetor: "))
    numeros2.append(num2)

diferenca = []
soma = []
multiplicacao = []

for i in range(20):
    diferenca.append(numeros1[i] - numeros2[i])
    soma.append(numeros1[i] + numeros2[i])
    multiplicacao.append(numeros1[i] * numeros2[i])

print(f"Vetor da diferença: {diferenca}")
print(f"Vetor da soma: {soma}")
print(f"Vetor da multiplicação: {multiplicacao}")