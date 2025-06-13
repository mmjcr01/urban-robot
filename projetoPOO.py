avioes = {}

limite = 20
controle_geral = 0


class passageiro():
    def __init__(self, nome, id_aviao):
        self.nome = nome
        self.id_aviao = id_aviao




def registrar_avioes():
    if  controle_geral > 0:
        print("NÃO É POSSÍVEL ALTERAR ID APÓS UMA RESERVA!")

    else:
        for i in range(4):
            id_aviao = int(input(f"Informe o ID do avião {i + 1}"))
            avioes[id_aviao] = {
                'passageiros' : [],
                'vagas' : 0
            }


def quantidade_assento():

    qtd_assentos = avioes
    for id_aviao, assentos_livres in qtd_assentos.items():
        print(f"ID DO AVIÃO: {id_aviao}. assentos disponiveis:({assentos_livres['vagas']}/20)")


def reservar_passagem():
    global controle_geral
    id_aviao = int(input("Informe o ID do avião desejado:  "))
    if id_aviao in avioes:
        nome = input("Informe o nome do passageiro: ")
        cliente = passageiro(nome, id_aviao)
        if avioes[id_aviao]["vagas"] < limite:
            avioes[id_aviao]["passageiros"].append(cliente)
            avioes[id_aviao]["vagas"] += 1
            print(f"""RESERVA CONCLUÍDA! 
            Cliente: {cliente.nome}
            ID do avião: {cliente.id_aviao}""")
            controle_geral += 1


    else:
        print("ID NÃO ENCONTRADO")


def consultar_passageiro():
    achou = False
    nome_buscar = input("Informe o nome do passageiro: ")
    buscar = avioes
    for id_aviao, primeiro_dados in buscar.items():
        for segundo_dados in primeiro_dados['passageiros']:
            if segundo_dados.nome.lower() == nome_buscar.lower():
                print(f"Reserva do passageiro {nome_buscar} encontrada no avião: {id_aviao}")
                achou = True

    if not achou:
        print("Passageiro não encontrado")


def consultar_aviao():
    id_buscar = int(input("informe o ID do avião: "))


    if id_buscar in avioes:
        id_aviao = id_buscar
        print(f"Quantidade de assentos livres: ({avioes[id_aviao]['vagas']}/20)")

    else:
        print("ID NÃO ENCONTRADO!")







while True:
    print('================SEJA BEM VINDO AO SERVIDOR DA SWEET FLIGHT==============')

    print("1- REGISTRAR O NUMERO DE CADA AVIÃO")
    print("2- REGISTRAR O QUANTITATIVO DE ASSENTOS EM CADA AVIÃO")
    print("3- RESERVAR PASSAGEM AÉREA")
    print("4- REALIZAR CONSULTA POR AVIÃO")
    print("5- REALIZAR CONSULTA POR PASSAGEIRO")
    print("6- ENCERRAR")
    opcao = int(input(""))

    if   opcao == 1:
        registrar_avioes()

    elif opcao == 2:
        quantidade_assento()

    elif opcao == 3:
        reservar_passagem()

    elif opcao == 4:
        consultar_aviao()

    elif opcao == 5:
        consultar_passageiro()

    elif opcao == 6:
        break


