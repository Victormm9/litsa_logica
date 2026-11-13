# 4-Em uma classe há n alunos, cada um dos quais realizou k provas com pesos
# distintos. Dados n , k, os pesos das k provas e as notas de cada aluno, 
# calcular a média ponderada das provas para cada aluno e a média aritmética da
# classe em cada uma das provas

alunos = int(input("Digite o número de alunos: "))
provas = int(input("Digite o número de provas: "))

for i in range(alunos):
    print(f"\nAluno {i + 1}:")
    notas = []
    pesos = []
    
    for j in range(provas):
        nota = float(input(f"Digite a nota da prova {j + 1}: "))
        peso = float(input(f"Digite o peso da prova {j + 1}: "))
        notas.append(nota)
        pesos.append(peso)
    
    media_ponderada = sum(n * p for n, p in zip(notas, pesos)) / sum(pesos)
    print(f"Média ponderada do aluno {i + 1}: {media_ponderada:.2f}")
    print(f"Média aritmética da classe na prova {j + 1}: {sum(notas) / len(notas):.2f}")
