import bcrypt
import getpass

import json # colocar na versão final

usuarios = [] 

def login():
    """
        Função criada para simular o login do usuário através do arquivo JSON contendo os dados dos usuários
        e a senha criptografada, em que o próprio sistema consegue descriptografar e fazer o acesso caso os dados
        estejam corretos.
    """

    with open('testes/testeCadastroLogin/usuarios.json', 'r', encoding='utf-8') as arquivo: 
        usuarios = json.load(arquivo)
        
    global apelidoUsuario # Para facilitar comunicação com o usuário logado
    global emailUsuario # Para facilitar pegar o email nas demais funções

    encontrouUsuario = False
    senhaCorreta = False
    
    email: str = input("Digite seu email: ")

    for usuario in usuarios:
        emailUsuario = usuario['email']
        if emailUsuario == email:
            encontrouUsuario = True
            senha: str = getpass.getpass("Digite sua senha: ")
            if bcrypt.checkpw(senha.encode("utf-8"), usuario["senha"].encode("utf-8")):
                apelidoUsuario = usuario["apelido"]
                #time.sleep(1)
                print(f"Bem-vindo, {apelidoUsuario}!")  
                senhaCorreta = True
                return True
            
    if not encontrouUsuario: # caso não exista esse cadastro em nosso sistema
        print("Email não cadastrado em nosso sistema. Por favor, verifique o email digitado.")
        #time.sleep(1)
        return False
    
    if encontrouUsuario and not senhaCorreta: # Caso exista o email mas a senha está incorreta
        print("A senha está incorreta! Tente novamente!")
        #time.sleep(1)
        return False

login()

#print(f"Olá {apelidoUsuario}")
