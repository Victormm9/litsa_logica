# 1- Faça um algoritmo que leia a nota de 10 alunos de uma turma e 
# guarde-as em um vetor. No final, mostre:
# a) Qual é a média da turma
# b) Quantos alunos estão acima da média da turma 
# c) Qual foi a maior nota digitada
# d) Em que posições a maior nota aparece

notas = []
contador = 0
for alunos in range (10):
    nota = float(input("Digite a sua nota: "))
    if nota < 0 or nota > 10:
        print("Nota inválida. Digite uma nota entre 0 e 10.")
        continue
    notas.append(nota)
    if nota >= 7:
        contador += 1
maior_nota = max(notas)
total_nota = 0
posição = notas.index(maior_nota) + 1
for i in range (10):
    total_nota += notas[i]
    media = total_nota / 10
print(f"A media da turma é {media}")
print(f"A quantidade de alunos que esta acima da media é {contador}")
print(f"A maior nota alcançada é {maior_nota}")
print(f"A maior nota aparece na posição: {posição}")



