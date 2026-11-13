# 1- Faça um programa em Py que receba o total das vendas de cada vendedor e armazenadas em um vetor. 
# Receba também o percentual de comissão de cada vendedor e armazene-os em outro vetor. Receba os nomes 
# desses vendedores e armazene ­os em um terceiro vetor. Existem apenas dez vendedores. Calcule e mostre: 
# a) Um relatório com os nomes dos vendedores e os valores a receber; 
# b) O total das vendas de todos os vendedores; 
# c) O maior valor a receber e quem o receberá; 
# d) O menor valor a receber e quem o receberá.

nomes = []
vendas = []
comissoes = []
for i in range(10):
    nome = input(f"Digite o nome do vendedor {i+1}: ")
    nomes.append(nome)
    venda = float(input(f"Digite o total das vendas do vendedor {i+1}: "))
    vendas.append(venda)
    comissao = float(input(f"Digite o percentual de comissão do vendedor {i+1}: "))
    comissoes.append(comissao)

print("\nRelatório de Vendas e Comissões:")
total_vendas = 0
for i in range(10):
    total_vendas += vendas[i]
    valor_receber = vendas[i] * comissoes[i] / 100
    print(f"{nomes[i]}: R$ {valor_receber:.2f}")

print(f"\nTotal das vendas: R$ {total_vendas:.2f}")

maior_valor = 0
menor_valor = float('inf')
for i in range(10):
    valor_receber = vendas[i] * comissoes[i] / 100
    if valor_receber > maior_valor:
        maior_valor = valor_receber
    if valor_receber < menor_valor:
        menor_valor = valor_receber

print(f"\nMaior valor a receber: R$ {maior_valor:.2f}")
print(f"Menor valor a receber: R$ {menor_valor:.2f}")
