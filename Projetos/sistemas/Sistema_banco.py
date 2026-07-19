import time
import sys

print("Olá, seja bem vindo ao caixa do BancoGPT.py")
nome = input("Digite seu nome: ").strip()
time.sleep(2)

while not nome.replace(" ", "").isalpha():
    print("Digite um nome válido ! :/")
    nome = input("Digite seu nome: ").strip()

print(f"Seja bem vindo ao caixa do BancoGPT.py {nome}! ")
time.sleep(2)
    
num_acesso = int(input("Digite seu número de acesso: ").strip())

if num_acesso != 28032002:
    print("Número não encontrado!")
    sys.exit()
else:
    print("Número identificado!")

time.sleep(2) 

senha = int(input("Digite sua senha (Números): "))
print("Aguarde ! :)")

if senha == 1234:
    print("Senha correta!")

else:
    print("Senha incorreta !")
    sys.exit()

time.sleep(2)

print("Escolha uma opção !")

saldo = float(1000.00)

# alt = alternativas 

while True:
    time.sleep(2)
    alt = input(
        "\n(1) Mostrar Saldo"
        "\n(2) Realizar Depósito"
        "\n(3) Realizar Saque"
        "\n(4) Sair"
        "\n(5) Transferência"
        "\nEscolha uma opção: "
    )

    if alt == "1":
        time.sleep(2)
        print(f"Seu saldo é de R${saldo:.2f}")

    elif alt == "2":
        time.sleep(2)
        vlr_dep = float(input("Quanto você deseja depositar? "))
        if vlr_dep > 0:
            saldo += vlr_dep
            print("Depósito realizado!")
            print(f"Seu saldo atual é de R${saldo:.2f}")
        else:
            print("Valor de depósito inválido!")

    elif alt == "3":
        time.sleep(2)
        vlr_saque = float(input("Quanto você deseja sacar? "))

        if vlr_saque > 0 and vlr_saque <= saldo:
            saldo -= vlr_saque
            print(f"Saque realizado!")
            print(f"Seu saldo atual é de R${saldo:.2f}")
        else:
            print("Saldo insuficiente!") 
            
    elif alt == "4":
        print("Encerrando o programa...")
        break
    
    elif alt == "5":
        
        num_conta = int(input("Digite o número da conta: "))

        if num_conta == 12345:
            
         print("Conta identificada!")

         valor_tr = float(input("Quanto deseja transferir? R$ "))

         if valor_tr > 0 and valor_tr <= saldo:
             
             saldo -= valor_tr

             print(f"Você transferiu R${valor_tr:.2f}")
             print(f"Saldo atual: R${saldo:.2f}")
             
         else:
            print("Valor inválido ou saldo insuficiente.")
              
        else:                       
            print("Conta não identificada.")
        
else:
    time.sleep(2)
    print("Opção inválida!")






