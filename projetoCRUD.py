dic_alunos = {}


# Função para cadastrar aluno
def cadastrar_aluno():
    matricula = int(input("Digite a matrícula do aluno: "))
    nome = input("Digite o nome do aluno: ")
    dic_alunos[matricula] = nome
    print("Aluno cadastrado com sucesso!")


# Função para listar alunos
def listar_alunos():
    if dic_alunos:
        for matricula, nome in dic_alunos.items():
            print(f"Matrícula: {matricula} - Nome: {nome}")
    else:
        print("Nenhum aluno cadastrado.")


# Função para buscar aluno pelo nome
def buscar_aluno():
    nome = input("Digite o nome do aluno: ")
    encontrados = [matricula for matricula, aluno_nome in dic_alunos.items() if aluno_nome == nome]

    if encontrados:
        for matricula in encontrados:
            print(f"Matrícula: {matricula} - Nome: {nome}")
    else:
        print("Aluno não encontrado.")


# Função para excluir aluno
def excluir_aluno():
    matricula = int(input("Digite a matrícula do aluno: "))
    if matricula in dic_alunos:
        del dic_alunos[matricula]
        print("Aluno excluído com sucesso.")
    else:
        print("Aluno não encontrado.")


# Função para alterar dados do aluno
def alterar_aluno():
    matricula = input("Digite a matrícula do aluno: ")
    if matricula in dic_alunos:
        print(f"Nome atual: {dic_alunos[matricula]}")
        novo_nome = input("Digite o novo nome do aluno: ")
        dic_alunos[matricula] = novo_nome
        print("Nome alterado com sucesso.")
    else:
        print("Aluno não encontrado.")

def ler_nota(msg):
    while True:
        try:
            nota = float(input(msg))
            if nota < 0 or  nota > 10:
                print("Digite um número válido. ")
            else:
                return nota

        except ValueError:
            print("Digite um número válido. ")






def nota_aluno():
    matricula = int(input("digite a matricula do aluno: "))
    if matricula in dic_alunos:
        aluno_cadastrado = dic_alunos[matricula]
        print(f"aluno encontrado: {aluno_cadastrado}")
        print ("Informe as notas do aluno:")

        n1 = ler_nota('Informe a primeira nota:  ')
        n2 = ler_nota('Informe a segunda nota:  ')
        n3 = ler_nota('Informe a terceira nota:  ')
        n4 = ler_nota('Informe a quarta nota:  ')
        soma = (n1 + n2 + n3 + n4) /4
        if soma >= 7:
            print("Aluno foi aprovado!!!!!!")
        else:
            print("Aluno reprovado")
    else:
        print("aluno não encontrado")


# Menu principal
while True:
    print("\nCADASTRO DE ALUNOS")
    print("1 - Cadastrar Aluno")
    print("2 - Listar Alunos")
    print("3 - Buscar Aluno")
    print("4 - Excluir Aluno")
    print("5 - Alterar Aluno")
    print("6- lançar a nota do aluno")
    print("7 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_aluno()
    elif opcao == "2":
        listar_alunos()
    elif opcao == "3":
        buscar_aluno()
    elif opcao == "4":
        excluir_aluno()
    elif opcao == "5":
        alterar_aluno()
    elif opcao == "6":
        nota_aluno()
    elif opcao == "7":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida! Tente novamente.")