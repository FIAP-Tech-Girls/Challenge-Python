'''
    A rota precisa ter 
    1. Ponto de origem
    2. Ponto de destino
    3. Qual nome deseja salvar para a rota
'''

usuarios = []

import json
import bcrypt
import getpass



def login(email: str, senha: str):
    '''
        Função criada para simular o login do usuário através do arquivo JSON contendo os dados dos usuários
        e a senha criptografada, em que o próprio sistema consegue descriptografar e fazer o acesso caso os dados
        estejam corretos.
    '''
    with open('testes/testeCadastroLogin/usuarios.json', 'r', encoding='utf-8') as arquivo: 
        usuarios = json.load(arquivo)
        
    global apelidoUsuario
    global emailUsuario
    encontrouUsuario = False
    senhaCorreta = False
    for usuario in usuarios:
        emailUsuario = usuario['email']
        if emailUsuario == email:
            encontrouUsuario = True
            if bcrypt.checkpw(senha.encode("utf-8"), usuario["senha"].encode("utf-8")):
                apelidoUsuario = usuario["apelido"]
                print(f"Bem-vindo, {apelidoUsuario}!")  
                senhaCorreta = True
                return True
            
    if not encontrouUsuario:
        print("Email não cadastrado em nosso sistema. Por favor, verifique o email digitado.")
        return False
    
    if encontrouUsuario and not senhaCorreta:
        print("A senha está incorreta! Tente novamente!")
        return False

def rotaFavorita(emailUsuario: str, pontoOrigem: str, pontoDestino: str, tituloRotaFav: str):
    with open('testes/testeCadastroLogin/rotasFavoritas.json', 'r', encoding='utf-8') as arquivo: 
        rotasFav = json.load(arquivo)
    
    if emailUsuario not in rotasFav:
        rotasFav[emailUsuario] = {}
    
    rotasUsuario = rotasFav[emailUsuario]
    rota = {
        "Ponto Origem": pontoOrigem,
        "Ponto Destino": pontoDestino
    }
    rotasUsuario[tituloRotaFav] = rota 

    with open('testes/testeCadastroLogin/rotasFavoritas.json', 'w', encoding='utf-8') as arquivo: 
        json.dump(rotasFav, arquivo, indent=4, ensure_ascii=False)

    print("Rota cadastrada com sucesso!")

    
    
emailLogin: str = input("Digite seu email: ")
senhaLogin: str = getpass.getpass("Digite sua senha: ")

login(emailLogin, senhaLogin)

print(f"Olá {apelidoUsuario}")

pontoOrigem = input("Digite o ponto de origem: ")
pontoDestino = input("Digite o ponto de destino: ")
tituloRota = input("Digite o título da rota: ")
rotaFavorita(emailLogin, pontoOrigem, pontoDestino, tituloRota)
