def verificacao(login, senha):
    if "@" in login and ".com" in login and senha == "1234": 
        return True
    
    else:
        return False

login = input("Digite seu login: ")
senha = input("Digite sua senha: ")
 
if verificacao(login, senha):
    print("Login realizado com sucesso !")

else:
    print("Login ou senha incorretos !")
    
    
    # hugo@gmail.com  1234 