# def = define uma função (um bloco de código que pode ser usado várias vezes)
def verificacao(login, senha):
    # if = se essa condição for verdadeira, execute o código abaixo
    # "@" in login = verifica se tem o símbolo @ no login, ex: "hugo@" contém @
    # ".com" in login = verifica se tem ".com" no login, ex: "hugo@gmail.com" contém .com
    # and = E (precisa que TUDO seja verdadeiro), ex: quente AND úmido
    if "@" in login and ".com" in login and senha == "1234": 
        # return True = retorna (devolve) "verdadeiro" - login correto!
        return True
    
    # return False = retorna (devolve) "falso" - login incorreto!
    return False

# input() = aguarda o usuário digitar algo e guarda na variável
login = input("Digite seu login: ")
senha = input("Digite sua senha: ")
 
# if = testa se verificacao() retornou True (login correto)
if verificacao(login, senha):
    # print() = mostra mensagem na tela para o usuário
    print("Login realizado com sucesso !")

# else = se não (se verificacao retornou False)
else:
    print("Login ou senha incorretos !")
    
    
    # Exemplo de login correto: hugo@gmail.com com senha: 1234 