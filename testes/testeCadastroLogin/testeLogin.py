import bcrypt
import getpass

import json # colocar na versão final

usuarios = [] 

# login teste
def login(email, senha):
    with open('testes/testeCadastroLogin/usuarios.json', 'r', encoding='utf-8') as arquivo: 
        usuarios = json.load(arquivo)
        
    encontrouUsuario = False
    senhaCorreta = False
    for usuario in usuarios:
        if usuario['email'] == email:
            encontrouUsuario = True
            if bcrypt.checkpw(senha.encode("utf-8"), usuario["senha"].encode("utf-8")):
                print(f"Bem-vindo, {usuario['apelido']}!")  
                senhaCorreta = True
                return True
            
    if not encontrouUsuario:
        print("Email não cadastrado em nosso sistema. Por favor, verifique o email digitado.")
        return False
    
    if encontrouUsuario and not senhaCorreta:
        print("A senha está incorreta! Tente novamente!")
        return False

emailLogin = input("Digite seu email: ")
senhaLogin = getpass.getpass("Digite sua senha: ")

login(emailLogin, senhaLogin)
