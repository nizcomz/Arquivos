# def = cria uma função (um bloco de código reutilizável)
# verificacao = nome da função, ex: calcular_idade
def verificacao(login, senha):
    # if = se essa condição for verdadeira
    # == = compara se são iguais, ex: 5 == 5 é verdadeiro
    # and = E lógico (ambas precisam ser verdadeiras), ex: idade > 18 and tem_carteira
    if login == "admin" and senha == "1234":
        # return True = retorna (devolve) a resposta "verdadeiro"
        return True
    else:
        # else = senão (se a condição acima for falsa)
        # return False = retorna (devolve) a resposta "falso"
        return False



# input() = pega o que o usuário digita no teclado, ex: nome = input("Qual é seu nome?")
# = atribui (guarda) o valor na variável
login = input("Digite seu login: ")
senha = input("Digite sua senha: ")

# while = enquanto (repete enquanto a condição for verdadeira)
# not = não (inverte o resultado), ex: not True = False
# Se verificacao retornar False, "not False" vira True e o loop executa
while not verificacao(login, senha):
    # print() = mostra texto na tela para o usuário ler
    print("Login ou senha incorretos, tente novamente")
    # Pede novamente porque as credenciais estavam erradas
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")

# Quando a senha estiver correta, sai do loop e mostra sucesso
print("Login realizado com sucesso!")
