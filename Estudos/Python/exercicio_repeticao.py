while True:  # Inicia um loop infinito que continuará até que um break seja executado.
    saque = float(input("Qual o valor do saque? :"))  # Pede ao usuário um valor e converte a entrada para número decimal.
    if saque > 0:  # Verifica se o valor informado é maior que zero.
        print(f"Você efetuou o saque de R${saque:.2f}")  # Exibe uma mensagem confirmando o saque realizado.

        break  # Encerra o loop quando o valor informado for válido.

    else:  # Executa esta parte quando o valor informado não for maior que zero.
        print(
            "\n Ocorreu um erro com o valor solicitado !"  # Mensagem de erro exibida ao usuário.
            "\n Tente novamente."  # Solicita que o usuário tente novamente.
        )
        