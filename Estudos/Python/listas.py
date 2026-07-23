# def = define uma função, exemplo: def saudacao(): imprime "Olá"
def historico(historico_transacoes):
    # print() = mostra texto na tela, exemplo: print("Bem-vindo")
    print("Histórico de transações:")
    # for = repete um bloco para cada item, exemplo: for numero in [1,2,3]: print(numero)
    for transacao in historico_transacoes:
        # cada transacao é exibida, exemplo: transacao = "Depósito de 100 reais"
        print(transacao)


# = atribui um valor, exemplo: nome = "João" armazena "João" na variável nome
# [ ] = cria uma lista vazia, exemplo: compras = [ ] cria uma lista para adicionar itens
historico_transacoes = [ ]


# while True = cria um loop infinito, exemplo: while True: faz o programa repetir forever até break
while True:
    # print() = mostra texto na tela, exemplo: print("Escolha:") mostra opções ao usuário
    print("Menu:")
    print("1. Adicionar transação")
    print("2. Ver histórico de transações")
    print("3. Sair")

    # input() = permite o usuário digitar algo, exemplo: nome = input("Qual seu nome?") guarda resposta
    opcao = input("Escolha uma opção: ")

    # if = verifica uma condição, exemplo: if opcao == "1": executa se a condição for verdadeira
    if opcao == "1":
        
        # transacao = armazena o que o usuário digita, exemplo: "Saque de 50 reais"
        escolha = input("Qual transação você seja realizar (Saque/Depósito): ")

        if escolha == "Saque": #Se a transação for "Saque", executa o bloco abaixo
            valor_saque = float(input("Qual valor você deseja sacar ? ")) #V
            if valor_saque > 0:
                transacao = -valor_saque  # retorna o valor que foi sacado
            else:
                print("Valor inválido para saque.")
            
        elif escolha == "deposito": # se a escolha receber o valor deposito 
            valor_deposito = float(input("Qual valor você deseja depositar ? ")) 
            if valor_deposito > 0:
                transacao = valor_deposito
            else:
                print("Valor inválido !")
        # .append() = adiciona item ao final da lista, exemplo: lista.append("novo item")

        historico_transacoes.append(transacao)
        print("Transação adicionada com sucesso!")  

    # elif = "se não, se", exemplo: elif opcao == "2": verifica outra condição
    elif opcao == "2":
        # historico() = chama a função definida antes, exemplo: historico(minhas_transacoes)
        historico(historico_transacoes)

    elif opcao == "3":
        print("Saindo do programa...")
        # break = sai do loop, exemplo: break encerra o while True
        break
    else:
        # else = "se nenhuma opção acima", exemplo: else: print("Inválido") para opções não esperadas
        print("Opção inválida. Tente novamente.")
        