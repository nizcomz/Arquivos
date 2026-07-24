import re
import time

def fazer_login():
    email = input("Digite seu e-mail: ")
    time.sleep(1)
    senha = input("Digite sua senha: ")
    time.sleep(1)
    
    
    if re.search(r"@|\.com", email):
        print("Email (OK)")
        time.sleep(1)
        
    else:
        print(
            "\nEmail inválido !"
            "\nAcesso negado !"
            )
        time.sleep(1)
        
while True:  
    time.sleep(1)   
    print(
    "\nBem vindo !" 
    "\nVamos Iniciar seu login."
    "\nPor favor, preencha os requisitos a seguir:"
    )
    time.sleep(1)
    
    fazer_login()


