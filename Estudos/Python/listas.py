def historico(historico_transacoes):
    print("Histórico de transações:")
    for transacao in historico_transacoes:
        print(transacao)


historico_transacoes = [ ]


while True:
    print("Menu:")
    print("1. Adicionar transação")
    print("2. Ver histórico de transações")
    print("3. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        transacao = input("Digite a transação: ")
        historico_transacoes.append(transacao)
        print("Transação adicionada com sucesso!")  

    elif opcao == "2":
        historico(historico_transacoes)

    elif opcao == "3":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")
        