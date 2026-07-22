def verificacao(login, senha):
    #Aqui você pode colocar a lógica de verificação do login e senha
    #Por exemplo, verificar se o login é "admin" e a senha é "1234"
    if login == "admin" and senha == "1234":
        return True
    else:
        return False



#Pedir login
login = input("Digite seu login: ")
#Pedir senha
senha = input("Digite sua senha: ")

#Enquanto verificacao(login, senha) for False:
while not verificacao(login, senha):
    #    Avisar "login ou senha incorretos, tente novamente"
    print("Login ou senha incorretos, tente novamente")
    #    Pedir login
    login = input("Digite seu login: ")
    #    Pedir senha
    senha = input("Digite sua senha: ")

#Mostrar "Login realizado com sucesso!"
print("Login realizado com sucesso!")