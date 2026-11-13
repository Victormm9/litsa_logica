# 4- Faça um programa em Py que alimente um vetor, com um número de posições 
# definidas pelo usuário. Este vetor deverá armazenar um conjunto de nomes em
#  diferentes posições. Crie um mecanismo para alimentar elementos no vetor e 
# pesquisar por um valor existente.
#  ======== MENU ======== 
# 1) Cadastrar nome 
# 2) Pesquisar nome 
# 3) Listar todos os nome 
# 0) Sair do programa 
# ——————– 
# Digite sua escolha:

nome_vetor = []
while True:
    print("\n======== MENU ========")
    print("1) Cadastrar nome")
    print("2) Pesquisar nome")
    print("3) Listar todos os nomes")
    print("0) Sair do programa")
    escolha = input("Digite sua escolha: ")

    if escolha == '1':
        nome = input("Digite o nome a ser cadastrado: ")
        nome_vetor.append(nome)
        print(f"Nome '{nome}' cadastrado com sucesso.")
    elif escolha == '2':
        nome_pesquisa = input("Digite o nome a ser pesquisado: ")
        if nome_pesquisa in nome_vetor:
            print(f"Nome '{nome_pesquisa}' encontrado no vetor.")
        else:
            print(f"Nome '{nome_pesquisa}' não encontrado no vetor.")
    elif escolha == '3':
        if nome_vetor:
            print("Nomes cadastrados:")
            for i, nome in enumerate(nome_vetor, start=1):
                print(f"{i}. {nome}")
        else:
            print("Nenhum nome cadastrado.")
    elif escolha == '0':
        print("Saindo do programa...")
        break
    else:
        print("Escolha inválida. Por favor, tente novamente.")

